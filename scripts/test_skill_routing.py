#!/usr/bin/env python3
"""
Skill Routing Test Framework
=============================
Tests whether each skill's test-prompts route correctly based on
keyword matching against SKILL.md front-matter (description + tags).

Usage:
    python3 scripts/test_skill_routing.py [--verbose] [--book BOOK_SLUG]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Skill:
    name: str
    description: str
    tags: list[str]
    book: str
    path: str
    keywords: list[str] = field(default_factory=list)


@dataclass
class TestPrompt:
    id: str
    type: str          # should_trigger | should_not_trigger | edge_case (plus legacy names)
    prompt: str
    expected_behavior: str
    skill_name: str
    book: str


@dataclass
class RouteResult:
    prompt: TestPrompt
    matched_skills: list[str]   # top-N skill names by score
    target_hit: bool            # whether the target skill appears in matches
    passed: bool                # whether the test passed
    score_map: dict = field(default_factory=dict)  # skill_name -> score


# ---------------------------------------------------------------------------
# YAML front-matter parser (handles --- delimited blocks)
# ---------------------------------------------------------------------------

_FRONT_MATTER_RE = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)


def parse_front_matter(text: str) -> dict | None:
    m = _FRONT_MATTER_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


# ---------------------------------------------------------------------------
# Keyword extraction
# ---------------------------------------------------------------------------

def extract_keywords(skill: Skill) -> list[str]:
    """Build a keyword list from description, tags, and name."""
    kws: set[str] = set()

    # Tags are high-signal
    for tag in skill.tags:
        if isinstance(tag, str):
            kws.add(tag.lower())

    # Extract quoted phrases from description (e.g. 'logline', "场景对比")
    for m in re.finditer(r'[\'""]([^\'""]{2,})[\'""]', skill.description):
        kws.add(m.group(1).lower())

    # Extract Chinese/English domain terms from description
    # Split on punctuation, keep meaningful tokens
    desc_tokens = re.findall(r'[一-鿿]{2,}|[a-zA-Z]{3,}', skill.description)
    for t in desc_tokens:
        kws.add(t.lower())

    # Name-derived tokens
    for part in skill.name.split('-'):
        if len(part) >= 2:
            kws.add(part.lower())

    return sorted(kws)


# ---------------------------------------------------------------------------
# Routing engine
# ---------------------------------------------------------------------------

class KeywordRouter:
    """Simple keyword-overlap router.

    For each prompt, compute how many keywords from each skill appear
    in the prompt text. Return skills sorted by score.
    """

    def __init__(self, skills: list[Skill]):
        self.skills = skills
        # Pre-compute keyword sets
        self._kw_sets: dict[str, set[str]] = {}
        for s in skills:
            self._kw_sets[s.name] = set(s.keywords)

    def route(self, prompt_text: str, top_n: int = 5) -> list[tuple[str, float]]:
        """Return top-N (skill_name, score) pairs."""
        text_lower = prompt_text.lower()
        scores: list[tuple[str, float]] = []
        for s in self.skills:
            kw_set = self._kw_sets[s.name]
            if not kw_set:
                scores.append((s.name, 0.0))
                continue
            # Count keyword hits
            hits = sum(1 for kw in kw_set if kw in text_lower)
            # Normalize by sqrt of keyword count to avoid long keyword lists dominating
            import math
            score = hits / math.sqrt(len(kw_set)) if kw_set else 0.0
            scores.append((s.name, score))
        scores.sort(key=lambda x: -x[1])
        return scores[:top_n]


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_skills(books_root: Path) -> list[Skill]:
    skills: list[Skill] = []
    for book_dir in sorted(books_root.iterdir()):
        if not book_dir.is_dir():
            continue
        book_name = book_dir.name
        for skill_dir in sorted(book_dir.iterdir()):
            skill_md = skill_dir / 'SKILL.md'
            if not skill_md.is_file():
                continue
            text = skill_md.read_text(encoding='utf-8')
            fm = parse_front_matter(text)
            if not fm:
                continue
            name = fm.get('name', skill_dir.name)
            desc = fm.get('description', '')
            if isinstance(desc, list):
                desc = ' '.join(desc)
            tags = fm.get('tags', []) or []
            s = Skill(
                name=name,
                description=str(desc),
                tags=[str(t) for t in tags],
                book=book_name,
                path=str(skill_dir),
            )
            s.keywords = extract_keywords(s)
            skills.append(s)
    return skills


def normalize_type(raw_type: str) -> str:
    """Map legacy type names to canonical ones."""
    mapping = {
        'should_activate': 'should_trigger',
        'decoy': 'should_not_trigger',
        'boundary': 'edge_case',
    }
    return mapping.get(raw_type, raw_type)


def load_test_prompts(books_root: Path) -> list[TestPrompt]:
    prompts: list[TestPrompt] = []
    for book_dir in sorted(books_root.iterdir()):
        if not book_dir.is_dir():
            continue
        book_name = book_dir.name
        for skill_dir in sorted(book_dir.iterdir()):
            tp_path = skill_dir / 'test-prompts.json'
            if not tp_path.is_file():
                continue
            try:
                data = json.loads(tp_path.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                continue
            for item in data:
                raw_type = item.get('type', '')
                tp = TestPrompt(
                    id=str(item.get('id', '')),
                    type=normalize_type(raw_type),
                    prompt=item.get('prompt', ''),
                    expected_behavior=item.get('expected_behavior', item.get('expected', '')),
                    skill_name=skill_dir.name,
                    book=book_name,
                )
                prompts.append(tp)
    return prompts


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------

def run_tests(
    skills: list[Skill],
    prompts: list[TestPrompt],
    router: KeywordRouter,
    top_n: int = 5,
) -> list[RouteResult]:
    results: list[RouteResult] = []
    skill_name_set = {s.name for s in skills}

    for tp in prompts:
        route_hits = router.route(tp.prompt, top_n=top_n)
        matched_names = [name for name, _ in route_hits]
        score_map = {name: score for name, score in route_hits}

        target = tp.skill_name
        target_hit = target in matched_names

        if tp.type == 'should_trigger':
            passed = target_hit
        elif tp.type == 'should_not_trigger':
            # Should NOT be the top-1 match (allow it to appear lower)
            passed = matched_names[0] != target if matched_names else True
        elif tp.type == 'edge_case':
            passed = True  # edge_cases are always "reviewed", not pass/fail
        else:
            passed = True  # unknown type, skip

        results.append(RouteResult(
            prompt=tp,
            matched_skills=matched_names,
            target_hit=target_hit,
            passed=passed,
            score_map=score_map,
        ))
    return results


# ---------------------------------------------------------------------------
# Report generator
# ---------------------------------------------------------------------------

def generate_report(results: list[RouteResult], skills: list[Skill]) -> str:
    lines: list[str] = []
    lines.append('# Skill Routing Test Report')
    lines.append('')
    lines.append(f'Generated: {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")}')
    lines.append('')

    # Summary
    total = len(results)
    by_type = defaultdict(list)
    for r in results:
        by_type[r.prompt.type].append(r)

    st = by_type.get('should_trigger', [])
    snt = by_type.get('should_not_trigger', [])
    ec = by_type.get('edge_case', [])

    st_pass = sum(1 for r in st if r.passed)
    snt_pass = sum(1 for r in snt if r.passed)

    lines.append('## Overall Summary')
    lines.append('')
    lines.append(f'| Metric | Value |')
    lines.append(f'|--------|-------|')
    lines.append(f'| Total prompts tested | {total} |')
    lines.append(f'| should_trigger | {len(st)} total, **{st_pass} passed** ({st_pass/len(st)*100:.0f}%) |') if st else lines.append(f'| should_trigger | 0 total |')
    lines.append(f'| should_not_trigger | {len(snt)} total, **{snt_pass} passed** ({snt_pass/len(snt)*100:.0f}%) |') if snt else lines.append(f'| should_not_trigger | 0 total |')
    lines.append(f'| edge_case (reviewed) | {len(ec)} |')
    denom = len(st) + len(snt)
    lines.append(f'| **Overall pass rate** | **{(st_pass+snt_pass)/denom*100:.1f}%** |') if denom else lines.append(f'| **Overall pass rate** | N/A |')
    lines.append('')

    # Per-book breakdown
    lines.append('## Per-Book Breakdown')
    lines.append('')
    lines.append('| Book | Skills | Prompts | ST Pass | SNT Pass | Overall |')
    lines.append('|------|--------|---------|---------|----------|---------|')

    books = sorted(set(r.prompt.book for r in results))
    for book in books:
        book_results = [r for r in results if r.prompt.book == book]
        book_skills = [s for s in skills if s.book == book]
        book_st = [r for r in book_results if r.prompt.type == 'should_trigger']
        book_snt = [r for r in book_results if r.prompt.type == 'should_not_trigger']
        st_p = sum(1 for r in book_st if r.passed)
        snt_p = sum(1 for r in book_snt if r.passed)
        denom = len(book_st) + len(book_snt)
        overall = f'{(st_p+snt_p)/denom*100:.0f}%' if denom > 0 else 'N/A'
        st_pct = f'{st_p}/{len(book_st)} ({st_p/len(book_st)*100:.0f}%)' if book_st else '-'
        snt_pct = f'{snt_p}/{len(book_snt)} ({snt_p/len(book_snt)*100:.0f}%)' if book_snt else '-'
        lines.append(f'| {book} | {len(book_skills)} | {len(book_results)} | {st_pct} | {snt_pct} | {overall} |')

    lines.append('')

    # Failed items detail
    failed_st = [r for r in st if not r.passed]
    failed_snt = [r for r in snt if not r.passed]

    if failed_st or failed_snt:
        lines.append('## Failed Tests Detail')
        lines.append('')

    if failed_st:
        lines.append('### should_trigger failures (target skill NOT in top-5)')
        lines.append('')
        for r in failed_st:
            p = r.prompt
            lines.append(f'**[{p.book}/{p.skill_name}] prompt #{p.id}**')
            lines.append(f'> {p.prompt}')
            lines.append(f'')
            lines.append(f'- Expected: `{p.skill_name}` should be in top-5')
            lines.append(f'- Got top-3: {", ".join(f"`{n}` (score={r.score_map.get(n,0):.2f})" for n in r.matched_skills[:3])}')
            lines.append(f'')

    if failed_snt:
        lines.append('### should_not_trigger failures (target skill IS top-1)')
        lines.append('')
        for r in failed_snt:
            p = r.prompt
            lines.append(f'**[{p.book}/{p.skill_name}] prompt #{p.id}**')
            lines.append(f'> {p.prompt}')
            lines.append(f'')
            lines.append(f'- Expected: `{p.skill_name}` should NOT be top-1')
            lines.append(f'- Got top-1: `{r.matched_skills[0]}` (score={r.score_map.get(r.matched_skills[0], 0):.2f})')
            lines.append(f'')

    # Edge cases summary
    if ec:
        lines.append('## Edge Cases (reviewed)')
        lines.append('')
        lines.append('| Book/Skill | Prompt (truncated) | Top-3 routed to |')
        lines.append('|-----------|-------------------|-----------------|')
        for r in ec:
            p = r.prompt
            top3 = ', '.join(f'`{n}`' for n in r.matched_skills[:3])
            trunc = p.prompt[:60] + ('...' if len(p.prompt) > 60 else '')
            lines.append(f'| {p.book}/{p.skill_name} | {trunc} | {top3} |')
        lines.append('')

    # Per-skill pass rate
    lines.append('## Per-Skill Pass Rate')
    lines.append('')
    lines.append('| Book | Skill | ST | SNT | Status |')
    lines.append('|------|-------|----|----|--------|')

    skill_names = sorted(set(r.prompt.skill_name for r in results))
    for sn in skill_names:
        sr = [r for r in results if r.prompt.skill_name == sn]
        book = sr[0].prompt.book
        st_r = [r for r in sr if r.prompt.type == 'should_trigger']
        snt_r = [r for r in sr if r.prompt.type == 'should_not_trigger']
        st_ok = f'{sum(1 for r in st_r if r.passed)}/{len(st_r)}' if st_r else '-'
        snt_ok = f'{sum(1 for r in snt_r if r.passed)}/{len(snt_r)}' if snt_r else '-'
        all_passable = [r for r in sr if r.prompt.type in ('should_trigger', 'should_not_trigger')]
        status = 'PASS' if all(r.passed for r in all_passable) else '**FAIL**'
        lines.append(f'| {book} | {sn} | {st_ok} | {snt_ok} | {status} |')

    lines.append('')

    # Root cause analysis
    lines.append('## Root Cause Analysis')
    lines.append('')

    # Count failures by pattern
    generic_st_failures = 0
    cross_domain_failures = 0
    for r in failed_st:
        p = r.prompt
        # Check if prompt is too generic (contains common filler but not skill-specific terms)
        skill_kws = set()
        for s in skills:
            if s.name == p.skill_name:
                skill_kws = set(s.keywords)
                break
        prompt_lower = p.prompt.lower()
        specific_hits = sum(1 for kw in skill_kws if kw in prompt_lower)
        if specific_hits < 2:
            generic_st_failures += 1
        # Check if top-1 is from a different book
        if r.matched_skills:
            top1_book = None
            for s in skills:
                if s.name == r.matched_skills[0]:
                    top1_book = s.book
                    break
            if top1_book and top1_book != p.book:
                cross_domain_failures += 1

    lines.append(f'### Failure Pattern Summary')
    lines.append(f'')
    lines.append(f'- **Total should_trigger failures**: {len(failed_st)}')
    lines.append(f'  - Prompts with <2 skill-specific keyword hits (possibly too generic): {generic_st_failures}')
    lines.append(f'  - Prompts routed to a different book\'s skill: {cross_domain_failures}')
    lines.append(f'- **Total should_not_trigger failures**: {len(failed_snt)}')
    lines.append(f'')

    lines.append('### Improvement Recommendations')
    lines.append('')
    lines.append('1. **test-prompts quality**: Prompts with few skill-specific keywords need rewriting')
    lines.append('   to include domain terms that uniquely identify the target skill.')
    lines.append('2. **Skill description/tags**: Skills that frequently lose to neighbors need more')
    lines.append('   distinctive tags or a clearer description boundary.')
    lines.append('3. **Router algorithm**: Current keyword-overlap is a baseline. Consider adding')
    lines.append('   negative keywords (from should_not_trigger patterns) and weighted tag matching.')
    lines.append('')

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Skill Routing Test Framework')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--book', type=str, default=None, help='Test only one book')
    parser.add_argument('--top-n', type=int, default=5, help='Top-N skills for routing')
    parser.add_argument('--report', type=str, default=None, help='Write report to file')
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    books_root = project_root / 'output' / 'books'

    if not books_root.is_dir():
        print(f'ERROR: books root not found at {books_root}', file=sys.stderr)
        sys.exit(1)

    # Load
    print('Loading skills...')
    skills = load_skills(books_root)
    if args.book:
        skills = [s for s in skills if s.book == args.book]
    print(f'  Loaded {len(skills)} skills')

    print('Loading test prompts...')
    prompts = load_test_prompts(books_root)
    if args.book:
        prompts = [p for p in prompts if p.book == args.book]
    print(f'  Loaded {len(prompts)} test prompts')

    # Route
    print('Running routing tests...')
    router = KeywordRouter(skills)
    results = run_tests(skills, prompts, router, top_n=args.top_n)

    # Quick stats
    st = [r for r in results if r.prompt.type == 'should_trigger']
    snt = [r for r in results if r.prompt.type == 'should_not_trigger']
    ec = [r for r in results if r.prompt.type == 'edge_case']

    st_pass = sum(1 for r in st if r.passed)
    snt_pass = sum(1 for r in snt if r.passed)

    print(f'\n{"="*60}')
    print(f'Results:')
    print(f'  should_trigger:     {st_pass}/{len(st)} passed ({st_pass/len(st)*100:.0f}%)' if st else '  should_trigger:     N/A')
    print(f'  should_not_trigger: {snt_pass}/{len(snt)} passed ({snt_pass/len(snt)*100:.0f}%)' if snt else '  should_not_trigger: N/A')
    print(f'  edge_case:          {len(ec)} reviewed')
    total_passable = len(st) + len(snt)
    total_passed = st_pass + snt_pass
    if total_passable:
        print(f'  ** Overall:         {total_passed}/{total_passable} ({total_passed/total_passable*100:.1f}%) **')
    print(f'{"="*60}')

    if args.verbose:
        print('\nFailed should_trigger:')
        for r in st:
            if not r.passed:
                p = r.prompt
                print(f'  [{p.book}/{p.skill_name}] #{p.id}: top3={r.matched_skills[:3]}')
        print('\nFailed should_not_trigger:')
        for r in snt:
            if not r.passed:
                p = r.prompt
                print(f'  [{p.book}/{p.skill_name}] #{p.id}: top1={r.matched_skills[0]}')

    # Generate report
    report = generate_report(results, skills)
    if args.report:
        report_path = Path(args.report)
    else:
        report_path = project_root / 'scripts' / 'routing_test_report.md'
    report_path.write_text(report, encoding='utf-8')
    print(f'\nReport written to: {report_path}')


if __name__ == '__main__':
    main()
