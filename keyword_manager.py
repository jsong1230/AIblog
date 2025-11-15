#!/usr/bin/env python3
"""
키워드 관리 시스템
CSV 파일에서 키워드를 읽고, 사용 여부를 추적합니다.
"""

import csv
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import random

KEYWORDS_CSV = Path("keywords.csv")
KEYWORDS_USED_LOG = Path("keywords_used.log")


class KeywordManager:
    def __init__(self, csv_file: str = "keywords.csv"):
        self.csv_file = Path(csv_file)
        self.keywords = []
        self.load_keywords()
    
    def load_keywords(self):
        """CSV 파일에서 키워드 로드"""
        if not self.csv_file.exists():
            print(f"⚠️  키워드 파일이 없습니다: {self.csv_file}")
            return
        
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.keywords = list(reader)
        
        print(f"📚 {len(self.keywords)}개의 키워드 로드 완료")
    
    def get_unused_keywords(self) -> List[Dict]:
        """사용하지 않은 키워드 목록 반환"""
        unused = [kw for kw in self.keywords if kw.get('사용여부', 'false').lower() == 'false']
        return unused
    
    def get_keyword_by_priority(self) -> Optional[Dict]:
        """우선순위가 높은 미사용 키워드 반환"""
        unused = self.get_unused_keywords()
        if not unused:
            return None
        
        # 우선순위별로 정렬 (숫자가 낮을수록 높은 우선순위)
        try:
            unused.sort(key=lambda x: int(x.get('우선순위', '999')))
        except ValueError:
            pass
        
        # 우선순위가 같은 것 중에서 랜덤 선택
        top_priority = int(unused[0].get('우선순위', '1'))
        same_priority = [kw for kw in unused if int(kw.get('우선순위', '999')) == top_priority]
        
        return random.choice(same_priority)
    
    def get_random_keyword(self) -> Optional[str]:
        """랜덤으로 미사용 키워드 선택"""
        unused = self.get_unused_keywords()
        if not unused:
            print("⚠️  사용 가능한 키워드가 없습니다. 모든 키워드를 재사용합니다.")
            # 모든 키워드 재사용
            self.reset_all_keywords()
            unused = self.get_unused_keywords()
        
        keyword = random.choice(unused)
        return keyword.get('키워드')
    
    def mark_keyword_as_used(self, keyword: str):
        """키워드를 사용됨으로 표시"""
        for kw in self.keywords:
            if kw.get('키워드') == keyword:
                kw['사용여부'] = 'true'
                kw['사용일자'] = datetime.now().strftime('%Y-%m-%d')
                break
        
        self.save_keywords()
        self.log_keyword_usage(keyword)
    
    def reset_all_keywords(self):
        """모든 키워드를 미사용 상태로 리셋"""
        for kw in self.keywords:
            kw['사용여부'] = 'false'
            kw['사용일자'] = ''
        self.save_keywords()
        print("🔄 모든 키워드가 재사용 가능 상태로 리셋되었습니다.")
    
    def save_keywords(self):
        """키워드를 CSV 파일에 저장"""
        if not self.keywords:
            return
        
        fieldnames = ['키워드', '카테고리', '우선순위', '사용여부', '사용일자']
        
        with open(self.csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.keywords)
    
    def log_keyword_usage(self, keyword: str):
        """키워드 사용 로그 기록"""
        with open(KEYWORDS_USED_LOG, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{keyword}\n")
    
    def add_keyword(self, keyword: str, category: str = "일반", priority: int = 1):
        """새 키워드 추가"""
        new_keyword = {
            '키워드': keyword,
            '카테고리': category,
            '우선순위': str(priority),
            '사용여부': 'false',
            '사용일자': ''
        }
        self.keywords.append(new_keyword)
        self.save_keywords()
        print(f"✅ 키워드 추가: {keyword}")
    
    def get_statistics(self) -> Dict:
        """키워드 통계 반환"""
        total = len(self.keywords)
        used = len([kw for kw in self.keywords if kw.get('사용여부', 'false').lower() == 'true'])
        unused = total - used
        
        return {
            'total': total,
            'used': used,
            'unused': unused,
            'usage_rate': (used / total * 100) if total > 0 else 0
        }
    
    def print_statistics(self):
        """키워드 통계 출력"""
        stats = self.get_statistics()
        print(f"\n📊 키워드 통계:")
        print(f"   전체: {stats['total']}개")
        print(f"   사용됨: {stats['used']}개")
        print(f"   미사용: {stats['unused']}개")
        print(f"   사용률: {stats['usage_rate']:.1f}%\n")


if __name__ == "__main__":
    manager = KeywordManager()
    manager.print_statistics()
    
    # 테스트: 키워드 선택
    keyword = manager.get_random_keyword()
    print(f"선택된 키워드: {keyword}")
    
    if keyword:
        manager.mark_keyword_as_used(keyword)
        print(f"✅ '{keyword}' 키워드가 사용됨으로 표시되었습니다.")

