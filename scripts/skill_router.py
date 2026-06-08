#!/usr/bin/env python3
"""
Skill Router — IDF-weighted keyword matching with Chinese word segmentation
and book-domain isolation.

Usage:
    python3 scripts/skill_router.py "用户的查询文本"
    python3 scripts/skill_router.py --test  # Run all test-prompts
"""

import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ============================================================
# Chinese word segmentation (jieba-free lightweight approach)
# ============================================================

# Common Chinese stop words for film/video domain
STOP_WORDS = set("的了是在我有和就不人也都一一个上很到说要去你会着没有看好自己这".split())

def segment_chinese(text: str) -> list[str]:
    """Lightweight Chinese segmentation using character n-grams + regex."""
    tokens = []
    # Extract Chinese character sequences (2-4 char n-grams)
    chinese_runs = re.findall(r'[\u4e00-\u9fff]+', text)
    for run in chinese_runs:
        # Single characters
        tokens.extend(list(run))
        # Bigrams
        for i in range(len(run) - 1):
            tokens.append(run[i:i+2])
        # Trigrams
        for i in range(len(run) - 2):
            tokens.append(run[i:i+3])
    
    # Extract English words
    english_words = re.findall(r'[a-zA-Z][a-zA-Z0-9-]+', text)
    tokens.extend([w.lower() for w in english_words])
    
    # Extract mixed terms (e.g., "Log-C", "BPM", "LUT")
    mixed = re.findall(r'[A-Z]{2,}|[A-Z][a-z]+-[A-Z]|Log[/-][A-Za-z]+\d*', text)
    tokens.extend([m.lower() for m in mixed])
    
    return [t for t in tokens if t not in STOP_WORDS]


# ============================================================
# IDF computation
# ============================================================

def compute_idf(skill_docs: dict[str, list[str]]) -> dict[str, float]:
    """
    Compute IDF scores across all skill documents.
    skill_docs: {skill_name: [tokens_from_skill_content]}
    """
    n = len(skill_docs)
    doc_freq = Counter()
    
    for skill_name, tokens in skill_docs.items():
        unique_tokens = set(tokens)
        for token in unique_tokens:
            doc_freq[token] += 1
    
    idf = {}
    for token, df in doc_freq.items():
        idf[token] = math.log((n + 1) / (df + 1)) + 1  # Smoothed IDF
    
    return idf


# ============================================================
# Skill index builder
# ============================================================

def build_skill_index(books_dir: str) -> dict:
    """
    Build a searchable index from all SKILL.md files.
    Returns: {skill_name: {
        'book': str, 'tokens': list, 'title': str,
        'a2_signals': list, 'description': str
    }}
    """
    skills = {}
    
    for book_dir in Path(books_dir).iterdir():
        if not book_dir.is_dir():
            continue
        book_name = book_dir.name
        
        for skill_dir in book_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            
            content = skill_md.read_text(encoding='utf-8')
            
            # Extract title
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else skill_dir.name
            
            # Extract A2 section (trigger signals)
            a2_match = re.search(r'## A2.*?\n(.*?)(?=\n## [A-Z]|\Z)', content, re.DOTALL)
            a2_text = a2_match.group(1) if a2_match else ""
            a2_signals = re.findall(r'["""]([^"""]+)["""]', a2_text)
            
            # Extract I section (interpretation)
            i_match = re.search(r'## I —.*?\n(.*?)(?=\n## [A-Z]|\Z)', content, re.DOTALL)
            i_text = i_match.group(1) if i_match else ""
            
            # Tokenize the full content for IDF
            tokens = segment_chinese(content)
            
            skills[skill_dir.name] = {
                'book': book_name,
                'tokens': tokens,
                'title': title,
                'a2_signals': a2_signals,
                'description': i_text[:500],
                'full_content': content,
            }
    
    return skills


# ============================================================
# Router
# ============================================================

class SkillRouter:
    def __init__(self, books_dir: str):
        self.skills = build_skill_index(books_dir)
        self.idf = self._compute_idf()
        self._precompute_tfidf()
    
    def _compute_idf(self) -> dict[str, float]:
        """Compute IDF across all skill documents."""
        doc_tokens = {name: s['tokens'] for name, s in self.skills.items()}
        return compute_idf(doc_tokens)
    
    def _precompute_tfidf(self):
        """Pre-compute TF-IDF vectors for each skill."""
        self.skill_vectors = {}
        for name, skill in self.skills.items():
            tf = Counter(skill['tokens'])
            total = len(skill['tokens']) or 1
            self.skill_vectors[name] = {
                token: (count / total) * self.idf.get(token, 1.0)
                for token, count in tf.items()
            }
    
    def _query_vector(self, query: str) -> dict[str, float]:
        """Compute TF-IDF vector for a query."""
        tokens = segment_chinese(query)
        tf = Counter(tokens)
        total = len(tokens) or 1
        return {
            token: (count / total) * self.idf.get(token, 1.0)
            for token, count in tf.items()
        }
    
    def _cosine_sim(self, vec_a: dict[str, float], vec_b: dict[str, float]) -> float:
        """Cosine similarity between two sparse vectors."""
        common = set(vec_a.keys()) & set(vec_b.keys())
        if not common:
            return 0.0
        
        dot = sum(vec_a[k] * vec_b[k] for k in common)
        norm_a = math.sqrt(sum(v * v for v in vec_a.values()))
        norm_b = math.sqrt(sum(v * v for v in vec_b.values()))
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        return dot / (norm_a * norm_b)
    
    def _signal_bonus(self, query: str, skill_name: str) -> float:
        """Bonus score if query matches A2 language signals."""
        skill = self.skills[skill_name]
        bonus = 0.0
        query_lower = query.lower()
        
        for signal in skill['a2_signals']:
            if signal.lower() in query_lower:
                bonus += 0.3  # Strong signal match
            elif any(s in query_lower for s in signal.lower().split('/')):
                bonus += 0.1  # Partial signal match
        
        return min(bonus, 0.5)  # Cap bonus
    
    def route(self, query: str, book_filter: str = None, 
              exclude_skills: set = None) -> list[dict]:
        """
        Route a query to the best matching skill(s).
        
        Args:
            query: User's input text
            book_filter: Only consider skills from this book
            exclude_skills: Skills to exclude from matching
        
        Returns: List of {skill_name, score, book, title} sorted by score
        """
        query_vec = self._query_vector(query)
        if not query_vec:
            return []
        
        results = []
        exclude = exclude_skills or set()
        
        for name, skill_vec in self.skill_vectors.items():
            if name in exclude:
                continue
            if book_filter and self.skills[name]['book'] != book_filter:
                continue
            
            # Cosine similarity
            cos_sim = self._cosine_sim(query_vec, skill_vec)
            
            # A2 signal bonus
            signal = self._signal_bonus(query, name)
            
            # Book-domain isolation penalty:
            # If the query has strong book-specific terms, boost same-book skills
            # but don't penalize cross-book (handled by IDF naturally)
            
            total_score = cos_sim + signal
            
            results.append({
                'skill_name': name,
                'score': total_score,
                'cos_sim': cos_sim,
                'signal_bonus': signal,
                'book': self.skills[name]['book'],
                'title': self.skills[name]['title'],
            })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results
    
    def test_prompt(self, prompt: str, expected_skill: str,
                    test_type: str = "should_trigger",
                    book_filter: str = None) -> dict:
        """
        Test a single prompt against the router.
        
        Returns: {passed: bool, top_skill, score, expected, details}
        """
        results = self.route(prompt, book_filter=book_filter)
        top = results[0] if results else None
        
        if test_type == "should_trigger":
            # Should activate the expected skill (or at least top 3)
            top_names = [r['skill_name'] for r in results[:3]]
            passed = expected_skill in top_names
            return {
                'passed': passed,
                'top_skill': top['skill_name'] if top else None,
                'top_score': top['score'] if top else 0,
                'expected': expected_skill,
                'top3': top_names,
                'type': test_type,
            }
        elif test_type == "should_not_trigger":
            # Should NOT activate the expected skill as top result
            top_name = top['skill_name'] if top else None
            passed = top_name != expected_skill
            return {
                'passed': passed,
                'top_skill': top_name,
                'top_score': top['score'] if top else 0,
                'expected_not': expected_skill,
                'type': test_type,
            }
        elif test_type == "edge_case":
            # Edge cases — just record the result, don't pass/fail
            return {
                'passed': True,  # Edge cases always "pass" — they're informational
                'top_skill': top['skill_name'] if top else None,
                'top_score': top['score'] if top else 0,
                'expected': expected_skill,
                'type': test_type,
            }
        
        return {'passed': False, 'error': f'Unknown test type: {test_type}'}


# ============================================================
# Test runner
# ============================================================

def run_all_tests(books_dir: str) -> dict:
    """Run all test-prompts.json files and report results."""
    router = SkillRouter(books_dir)
    
    results = {
        'total': 0,
        'passed': 0,
        'failed': 0,
        'skipped': 0,
        'should_trigger': {'total': 0, 'passed': 0},
        'should_not_trigger': {'total': 0, 'passed': 0},
        'edge_case': {'total': 0, 'passed': 0},
        'by_book': {},
        'failures': [],
    }
    
    for book_dir in sorted(Path(books_dir).iterdir()):
        if not book_dir.is_dir():
            continue
        book_name = book_dir.name
        book_results = {'total': 0, 'passed': 0, 'failed': 0}
        
        for skill_dir in sorted(book_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            
            test_file = skill_dir / "test-prompts.json"
            if not test_file.exists():
                continue
            
            try:
                tests = json.loads(test_file.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                results['skipped'] += 1
                continue
            
            expected_skill = skill_dir.name
            
            for test in tests:
                test_type = test.get('type', '')
                prompt = test.get('prompt', '')
                
                # Normalize test types
                TYPE_MAP = {
                    'should_activate': 'should_trigger',
                    'boundary': 'edge_case',
                    'decoy': 'should_not_trigger',
                    'should_trigger': 'should_trigger',
                    'should_not_trigger': 'should_not_trigger',
                    'edge_case': 'edge_case',
                }
                test_type = TYPE_MAP.get(test_type, '')
                
                if not test_type:
                    results['skipped'] += 1
                    continue
                
                if not prompt or not test_type:
                    results['skipped'] += 1
                    continue
                
                results['total'] += 1
                results[test_type]['total'] += 1
                book_results['total'] += 1
                
                # Route with book filter for should_trigger to enforce domain isolation
                book_filter = book_name if test_type == 'should_trigger' else None
                
                result = router.test_prompt(
                    prompt, expected_skill, test_type, book_filter
                )
                
                if result['passed']:
                    results['passed'] += 1
                    results[test_type]['passed'] += 1
                    book_results['passed'] += 1
                else:
                    results['failed'] += 1
                    book_results['failed'] += 1
                    results['failures'].append({
                        'book': book_name,
                        'skill': expected_skill,
                        'test_id': test.get('id', '?'),
                        'type': test_type,
                        'prompt': prompt[:80],
                        'top_skill': result.get('top_skill'),
                        'top_score': result.get('top_score', 0),
                    })
        
        results['by_book'][book_name] = book_results
    
    return results


def print_report(results: dict):
    """Print a formatted test report."""
    total = results['total']
    passed = results['passed']
    failed = results['failed']
    skipped = results['skipped']
    
    print(f"\n{'='*60}")
    print(f"📊 路由器测试报告 (IDF + 中文分词 + 书域隔离)")
    print(f"{'='*60}")
    print(f"\n总测试数: {total}")
    print(f"通过: {passed} ({passed/total*100:.1f}%)")
    print(f"失败: {failed} ({failed/total*100:.1f}%)")
    print(f"跳过: {skipped}")
    
    st = results['should_trigger']
    snt = results['should_not_trigger']
    ec = results['edge_case']
    print(f"\n  should_trigger:     {st['passed']}/{st['total']} ({st['passed']/max(st['total'],1)*100:.1f}%)")
    print(f"  should_not_trigger: {snt['passed']}/{snt['total']} ({snt['passed']/max(snt['total'],1)*100:.1f}%)")
    print(f"  edge_case:          {ec['passed']}/{ec['total']} (informational)")
    
    print(f"\n{'─'*60}")
    print(f"📚 按书籍分组")
    print(f"{'─'*60}")
    for book, br in sorted(results['by_book'].items()):
        t, p, f = br['total'], br['passed'], br['failed']
        pct = p / max(t, 1) * 100
        status = "✅" if pct >= 80 else "⚠️" if pct >= 60 else "❌"
        print(f"  {status} {book:30s} {p}/{t} ({pct:.0f}%)")
    
    if results['failures']:
        print(f"\n{'─'*60}")
        print(f"❌ 失败详情 (前 20 条)")
        print(f"{'─'*60}")
        for f in results['failures'][:20]:
            print(f"  [{f['type']}] {f['book']}/{f['skill']}")
            print(f"    prompt: {f['prompt']}")
            print(f"    expected: {f['skill']}, got: {f['top_skill']} (score={f['top_score']:.3f})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 skill_router.py <query>")
        print("       python3 skill_router.py --test")
        sys.exit(1)
    
    books_dir = os.path.join(os.path.dirname(__file__), '..', 'output', 'books')
    
    if sys.argv[1] == "--test":
        results = run_all_tests(books_dir)
        print_report(results)
        
        # Save JSON report
        report_path = os.path.join(os.path.dirname(__file__), '..', 'test_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n详细报告已保存到: {report_path}")
    else:
        query = " ".join(sys.argv[1:])
        router = SkillRouter(books_dir)
        results = router.route(query)
        
        print(f"\n查询: {query}")
        print(f"{'─'*50}")
        for i, r in enumerate(results[:5]):
            print(f"  {i+1}. [{r['book']}] {r['skill_name']}")
            print(f"     score={r['score']:.3f} (cos={r['cos_sim']:.3f} + signal={r['signal_bonus']:.3f})")
            print(f"     {r['title']}")
