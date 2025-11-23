#!/usr/bin/env python3
"""
키워드 성과 추적 시스템
블로그 포스트의 성과를 추적하고 키워드별 통계를 제공합니다.
"""

import csv
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from collections import defaultdict
import re

PERFORMANCE_DB = Path("data/keyword_performance.json")
CONTENT_DIR = Path("content/post")

class KeywordPerformanceTracker:
    def __init__(self):
        self.performance_db = self.load_performance_db()
        self.content_dir = CONTENT_DIR
        self.content_dir.mkdir(parents=True, exist_ok=True)
        PERFORMANCE_DB.parent.mkdir(parents=True, exist_ok=True)
    
    def load_performance_db(self) -> Dict:
        """성과 데이터베이스 로드"""
        if PERFORMANCE_DB.exists():
            with open(PERFORMANCE_DB, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_performance_db(self):
        """성과 데이터베이스 저장"""
        with open(PERFORMANCE_DB, 'w', encoding='utf-8') as f:
            json.dump(self.performance_db, f, ensure_ascii=False, indent=2)
    
    def extract_keyword_from_filename(self, filename: str) -> Optional[str]:
        """파일명에서 키워드 추출"""
        # 파일명 형식: YYYY-MM-DD-keyword-slug-timestamp.md
        # 또는: YYYY-MM-DD-keyword-slug-timestamp.en.md
        match = re.match(r'\d{4}-\d{2}-\d{2}-(.+?)-(\d+|timestamp)', filename)
        if match:
            keyword_slug = match.group(1)
            # slug를 키워드로 변환 (하이픈을 공백으로)
            keyword = keyword_slug.replace('-', ' ')
            return keyword
        return None
    
    def get_post_files(self) -> List[Path]:
        """모든 포스트 파일 목록 가져오기"""
        if not self.content_dir.exists():
            return []
        
        return list(self.content_dir.glob("*.md"))
    
    def analyze_post(self, post_file: Path) -> Dict:
        """포스트 파일 분석"""
        try:
            import frontmatter
            
            with open(post_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # 키워드 추출
            keyword = post.metadata.get('title', '')
            if not keyword:
                keyword = self.extract_keyword_from_filename(post_file.name)
            
            # 메타데이터 추출
            return {
                'keyword': keyword,
                'title': post.metadata.get('title', ''),
                'date': post.metadata.get('date', ''),
                'categories': post.metadata.get('categories', []),
                'tags': post.metadata.get('tags', []),
                'description': post.metadata.get('description', ''),
                'content_length': len(post.content),
                'filename': post_file.name,
            }
        except Exception as e:
            print(f"⚠️  포스트 분석 실패 ({post_file.name}): {e}")
            return None
    
    def update_keyword_performance(self, keyword: str, metrics: Dict):
        """키워드 성과 업데이트"""
        if keyword not in self.performance_db:
            self.performance_db[keyword] = {
                'keyword': keyword,
                'post_count': 0,
                'total_views': 0,
                'total_shares': 0,
                'avg_content_length': 0,
                'first_post_date': None,
                'last_post_date': None,
                'categories': set(),
                'tags': set(),
            }
        
        kw_data = self.performance_db[keyword]
        kw_data['post_count'] += 1
        
        # 메트릭 업데이트
        if 'views' in metrics:
            kw_data['total_views'] += metrics['views']
        if 'shares' in metrics:
            kw_data['total_shares'] += metrics['shares']
        if 'content_length' in metrics:
            current_avg = kw_data['avg_content_length']
            post_count = kw_data['post_count']
            kw_data['avg_content_length'] = (
                (current_avg * (post_count - 1) + metrics['content_length']) / post_count
            )
        
        # 날짜 업데이트
        if 'date' in metrics:
            date_str = metrics['date']
            if not kw_data['first_post_date'] or date_str < kw_data['first_post_date']:
                kw_data['first_post_date'] = date_str
            if not kw_data['last_post_date'] or date_str > kw_data['last_post_date']:
                kw_data['last_post_date'] = date_str
        
        # 카테고리/태그 업데이트
        if 'categories' in metrics:
            if isinstance(kw_data['categories'], set):
                kw_data['categories'].update(metrics['categories'])
            else:
                kw_data['categories'] = set(metrics['categories'])
        
        if 'tags' in metrics:
            if isinstance(kw_data['tags'], set):
                kw_data['tags'].update(metrics['tags'])
            else:
                kw_data['tags'] = set(metrics['tags'])
        
        # set을 list로 변환 (JSON 직렬화를 위해)
        kw_data['categories'] = list(kw_data.get('categories', set()))
        kw_data['tags'] = list(kw_data.get('tags', set()))
    
    def scan_all_posts(self):
        """모든 포스트 스캔 및 성과 업데이트"""
        print("🔍 포스트 스캔 시작...")
        
        post_files = self.get_post_files()
        print(f"📊 발견된 포스트: {len(post_files)}개")
        
        for post_file in post_files:
            analysis = self.analyze_post(post_file)
            if analysis:
                metrics = {
                    'content_length': analysis['content_length'],
                    'date': analysis['date'],
                    'categories': analysis['categories'],
                    'tags': analysis['tags'],
                }
                self.update_keyword_performance(analysis['keyword'], metrics)
        
        self.save_performance_db()
        print(f"✅ 스캔 완료: {len(self.performance_db)}개 키워드 추적 중")
    
    def get_top_keywords(self, metric: str = 'post_count', limit: int = 10) -> List[Dict]:
        """상위 키워드 가져오기"""
        if not self.performance_db:
            return []
        
        sorted_keywords = sorted(
            self.performance_db.items(),
            key=lambda x: x[1].get(metric, 0),
            reverse=True
        )
        
        return [
            {'keyword': kw, **data}
            for kw, data in sorted_keywords[:limit]
        ]
    
    def print_statistics(self):
        """통계 출력"""
        if not self.performance_db:
            print("📊 추적 중인 키워드가 없습니다.")
            return
        
        total_keywords = len(self.performance_db)
        total_posts = sum(kw['post_count'] for kw in self.performance_db.values())
        
        print(f"\n📊 키워드 성과 통계:")
        print(f"   추적 중인 키워드: {total_keywords}개")
        print(f"   총 포스트 수: {total_posts}개")
        print(f"   평균 포스트/키워드: {total_posts/total_keywords:.1f}개")
        
        # 상위 키워드 출력
        print(f"\n🏆 포스트 수 상위 10개 키워드:")
        top_keywords = self.get_top_keywords('post_count', 10)
        for i, kw_data in enumerate(top_keywords, 1):
            print(f"   {i}. {kw_data['keyword']}: {kw_data['post_count']}개 포스트")
    
    def export_to_csv(self, output_file: Path = Path("data/keyword_performance.csv")):
        """성과 데이터를 CSV로 내보내기"""
        if not self.performance_db:
            print("⚠️  내보낼 데이터가 없습니다.")
            return
        
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['키워드', '포스트수', '총조회수', '총공유수', '평균내용길이', 
                         '첫포스트일자', '마지막포스트일자', '카테고리', '태그']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for keyword, data in self.performance_db.items():
                writer.writerow({
                    '키워드': keyword,
                    '포스트수': data.get('post_count', 0),
                    '총조회수': data.get('total_views', 0),
                    '총공유수': data.get('total_shares', 0),
                    '평균내용길이': int(data.get('avg_content_length', 0)),
                    '첫포스트일자': data.get('first_post_date', ''),
                    '마지막포스트일자': data.get('last_post_date', ''),
                    '카테고리': ', '.join(data.get('categories', [])),
                    '태그': ', '.join(data.get('tags', [])),
                })
        
        print(f"✅ CSV 내보내기 완료: {output_file}")

if __name__ == "__main__":
    tracker = KeywordPerformanceTracker()
    
    # 모든 포스트 스캔
    tracker.scan_all_posts()
    
    # 통계 출력
    tracker.print_statistics()
    
    # CSV 내보내기
    tracker.export_to_csv()
