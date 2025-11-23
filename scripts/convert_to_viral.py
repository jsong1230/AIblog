#!/usr/bin/env python3
"""
기존 키워드를 바이럴 형태로 변환하는 스크립트
다양한 변환 패턴을 적용하여 더 매력적인 키워드로 변환합니다.
"""

import csv
import random
from pathlib import Path
from typing import List, Dict

# 바이럴 변환 패턴
VIRAL_PATTERNS = {
    # 숫자 + 결과 패턴
    'number_result': [
        "{keyword}로 월 {amount}만원 버는 법",
        "{keyword}로 하루 {time}시간 절약하기",
        "{keyword} {number}단계 완벽 가이드",
        "{keyword} {number}가지 실수 피하기",
        "{keyword} TOP {number}",
    ],
    
    # 비교 패턴
    'comparison': [
        "{keyword} vs {alternative} 실전 비교",
        "{keyword}로 배운 것 vs 안 배운 것",
        "{keyword} vs {alternative} 어떤 게 나을까",
    ],
    
    # 후기/사례 패턴
    'case_study': [
        "{keyword}로 성공한 실제 후기",
        "{keyword} 첫 수익 낸 후기",
        "{keyword} {period}만에 성공한 사례",
        "{keyword}로 인생 바꾼 사람들",
    ],
    
    # 비밀/노하우 패턴
    'secret': [
        "{keyword} 성공 비밀",
        "{keyword} 전문가가 말하지 않는 비법",
        "{keyword} 숨겨진 노하우",
        "{keyword}로 {result} 달성하는 비밀",
    ],
    
    # 실패 방지 패턴
    'failure_prevention': [
        "{keyword} 초보자가 놓치기 쉬운 {number}가지 실수",
        "{keyword} 실패 피하는 {number}가지 체크리스트",
        "{keyword} 전에 알아야 할 {number}가지",
    ],
    
    # 트렌드/시의성 패턴
    'trend': [
        "{year}년 가장 핫한 {keyword}",
        "{keyword} {year} 트렌드 완벽 분석",
        "지금 바로 시작해야 할 {keyword}",
        "앞으로 {period}간 바꿀 {keyword}",
    ],
    
    # 로드맵 패턴
    'roadmap': [
        "{keyword} {period} 로드맵",
        "{keyword} 완벽 마스터 가이드",
        "{keyword} 따라하면 되는 가이드",
        "{keyword} 시작하는 첫 단계",
    ],
}

# 카테고리별 대체 키워드
ALTERNATIVES = {
    '기술': ['React', 'Vue', 'Python', 'JavaScript', 'Node.js'],
    '수익': ['부업', '투잡', '패시브 인컴', '온라인 비즈니스'],
    '금융': ['주식', '부동산', 'ETF', '암호화폐'],
    '커리어': ['프리랜서', '원격 근무', '이직', '취업'],
    '교육': ['독학', '부트캠프', '온라인 강의', '튜토리얼'],
}

# 숫자/시간 변수
AMOUNTS = ['10', '50', '100', '200', '500']
TIMES = ['1', '2', '3', '10']
PERIODS = ['3개월', '6개월', '1년', '10년']
NUMBERS = ['5', '7', '10', '20']
YEARS = ['2025', '2026']

def get_viral_pattern(keyword: str, category: str) -> str:
    """키워드에 적합한 바이럴 패턴 선택"""
    keyword_lower = keyword.lower()
    
    # 카테고리와 키워드 내용에 따라 패턴 선택
    if '비교' in keyword or 'vs' in keyword_lower:
        return None  # 이미 비교형
    
    if '초보' in keyword or '입문' in keyword:
        pattern_type = random.choice(['failure_prevention', 'roadmap'])
    elif '투자' in keyword or '수익' in keyword or '돈' in keyword:
        pattern_type = random.choice(['number_result', 'case_study', 'secret'])
    elif '학습' in keyword or '공부' in keyword or '교육' in keyword:
        pattern_type = random.choice(['roadmap', 'comparison', 'number_result'])
    elif '도구' in keyword or '기술' in keyword:
        pattern_type = random.choice(['trend', 'comparison', 'number_result'])
    else:
        pattern_type = random.choice(list(VIRAL_PATTERNS.keys()))
    
    patterns = VIRAL_PATTERNS[pattern_type]
    pattern = random.choice(patterns)
    
    # 패턴에 맞게 변수 치환
    if '{amount}' in pattern:
        pattern = pattern.replace('{amount}', random.choice(AMOUNTS))
    if '{time}' in pattern:
        pattern = pattern.replace('{time}', random.choice(TIMES))
    if '{number}' in pattern:
        pattern = pattern.replace('{number}', random.choice(NUMBERS))
    if '{period}' in pattern:
        pattern = pattern.replace('{period}', random.choice(PERIODS))
    if '{year}' in pattern:
        pattern = pattern.replace('{year}', random.choice(YEARS))
    if '{alternative}' in pattern:
        alternatives = ALTERNATIVES.get(category, ['대안'])
        pattern = pattern.replace('{alternative}', random.choice(alternatives))
    if '{result}' in pattern:
        results = ['성공', '수익', '효율 향상', '생산성 향상']
        pattern = pattern.replace('{result}', random.choice(results))
    
    # 키워드 삽입
    if '{keyword}' in pattern:
        pattern = pattern.replace('{keyword}', keyword)
    
    return pattern

def convert_keyword_to_viral(keyword: str, category: str) -> str:
    """단일 키워드를 바이럴 형태로 변환"""
    # 이미 바이럴 형태인지 확인 (숫자, 비교, 후기 등이 포함된 경우)
    has_number = any(char.isdigit() for char in keyword)
    has_comparison = 'vs' in keyword.lower() or '비교' in keyword
    has_case = '후기' in keyword or '사례' in keyword or '비밀' in keyword
    
    if has_number or has_comparison or has_case:
        # 이미 바이럴 형태면 그대로 반환
        return keyword
    
    # 바이럴 패턴 적용
    viral_keyword = get_viral_pattern(keyword, category)
    
    if viral_keyword:
        return viral_keyword
    
    # 패턴 적용 실패 시 원본 반환
    return keyword

def convert_keywords_file(input_file: Path, output_file: Path):
    """키워드 파일 전체를 바이럴 형태로 변환"""
    print(f"🔄 키워드 변환 시작: {input_file}")
    
    converted_keywords = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original_keyword = row['키워드']
            category = row.get('카테고리', '일반')
            
            # 바이럴 형태로 변환
            viral_keyword = convert_keyword_to_viral(original_keyword, category)
            
            converted_keywords.append({
                '키워드': viral_keyword,
                '카테고리': category,
                '우선순위': row.get('우선순위', '1'),
                '사용여부': row.get('사용여부', 'False'),
                '사용일자': row.get('사용일자', ''),
            })
    
    # 변환된 키워드 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['키워드', '카테고리', '우선순위', '사용여부', '사용일자']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(converted_keywords)
    
    print(f"✅ 변환 완료: {output_file}")
    print(f"   변환된 키워드: {len(converted_keywords)}개")
    
    return converted_keywords

if __name__ == "__main__":
    import sys
    
    input_file = Path("keywords.csv")
    output_file = Path("keywords_viral_converted.csv")
    
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    
    convert_keywords_file(input_file, output_file)
    
    # 샘플 출력
    print("\n📝 변환 샘플 (처음 10개):")
    with open(output_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i < 10:
                print(f"   {row['키워드']}")
