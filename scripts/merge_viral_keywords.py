#!/usr/bin/env python3
"""
바이럴 키워드를 keywords.csv에 병합하는 스크립트
중복을 제거하고 기존 키워드와 병합합니다.
"""

import sys
import csv
from pathlib import Path

# 상위 디렉토리를 경로에 추가 (Path 사용 전에)
_script_dir = Path(__file__).parent
_project_root = _script_dir.parent
sys.path.insert(0, str(_project_root))

from keyword_manager import KeywordManager

def load_keywords_from_file(file_path: Path):
    """CSV 파일에서 키워드 로드 (주석 제외)"""
    keywords = []
    if not file_path.exists():
        print(f"⚠️  파일이 없습니다: {file_path}")
        return keywords
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 주석이나 빈 줄이 아니고, 헤더가 아닌 경우
            if line and not line.startswith('#') and not line.startswith('키워드'):
                parts = line.split(',')
                if len(parts) >= 2:
                    keyword = parts[0].strip()
                    category = parts[1].strip()
                    priority = parts[2].strip() if len(parts) > 2 and parts[2].strip() else '1'
                    keywords.append({
                        '키워드': keyword,
                        '카테고리': category,
                        '우선순위': priority
                    })
    
    return keywords

def merge_keywords():
    """바이럴 키워드를 기존 keywords.csv에 병합"""
    print("🔄 바이럴 키워드 병합 시작...")
    
    # 기존 키워드 매니저 로드
    manager = KeywordManager()
    existing_keywords = {kw['키워드']: kw for kw in manager.keywords}
    
    # 개선된 키워드 파일 로드
    viral_file = Path("keywords_viral_improved.csv")
    viral_keywords = load_keywords_from_file(viral_file)
    
    print(f"📊 기존 키워드: {len(existing_keywords)}개")
    print(f"📊 바이럴 키워드: {len(viral_keywords)}개")
    
    # 중복 제거 및 병합
    new_keywords_count = 0
    for viral_kw in viral_keywords:
        keyword = viral_kw['키워드']
        if keyword not in existing_keywords:
            # 새 키워드 추가
            manager.add_keyword(
                keyword=keyword,
                category=viral_kw['카테고리'],
                priority=int(viral_kw['우선순위'])
            )
            new_keywords_count += 1
    
    print(f"\n✅ 병합 완료!")
    print(f"   새로 추가된 키워드: {new_keywords_count}개")
    print(f"   총 키워드 수: {len(manager.keywords)}개")
    
    # 통계 출력
    manager.print_statistics()
    
    return new_keywords_count

if __name__ == "__main__":
    merge_keywords()
