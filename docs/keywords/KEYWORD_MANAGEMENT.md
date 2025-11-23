# 키워드 관리 가이드

## 📋 개요

이 문서는 AI 블로그의 키워드 관리 시스템에 대한 종합 가이드입니다. 바이럴 가능성이 높은 키워드 생성, 변환, 성과 추적 방법을 다룹니다.

## 🎯 키워드 관리 시스템 구성

### 1. 키워드 파일
- `keywords.csv`: 메인 키워드 데이터베이스
- `keywords_viral_improved.csv`: 바이럴 형태로 개선된 키워드
- `keywords_viral_converted.csv`: 기존 키워드를 변환한 바이럴 키워드

### 2. 관리 스크립트
- `keyword_manager.py`: 기본 키워드 관리 (추가, 사용 표시, 통계)
- `scripts/merge_viral_keywords.py`: 바이럴 키워드 병합
- `scripts/convert_to_viral.py`: 기존 키워드를 바이럴 형태로 변환
- `scripts/keyword_performance_tracker.py`: 키워드 성과 추적

## 🚀 사용 방법

### 바이럴 키워드 병합

기존 `keywords.csv`에 바이럴 키워드를 추가합니다:

```bash
python3 scripts/merge_viral_keywords.py
```

**기능:**
- 중복 키워드 자동 제거
- 기존 키워드와 병합
- 통계 출력

### 키워드 바이럴 변환

기존 키워드를 바이럴 형태로 변환합니다:

```bash
# 기본 사용
python3 scripts/convert_to_viral.py

# 입력/출력 파일 지정
python3 scripts/convert_to_viral.py keywords.csv keywords_viral_converted.csv
```

**변환 패턴:**
- 숫자 + 결과: "월 100만원 버는 법"
- 비교형: "A vs B 실전 비교"
- 후기/사례: "성공한 실제 후기"
- 비밀/노하우: "성공 비밀"
- 실패 방지: "놓치기 쉬운 7가지 실수"
- 트렌드: "2025년 가장 핫한"
- 로드맵: "완벽 마스터 가이드"

### 키워드 성과 추적

포스트의 성과를 추적하고 통계를 생성합니다:

```bash
python3 scripts/keyword_performance_tracker.py
```

**기능:**
- 모든 포스트 스캔
- 키워드별 통계 생성
- CSV 내보내기
- 상위 키워드 분석

**출력 파일:**
- `data/keyword_performance.json`: 성과 데이터베이스
- `keyword_performance.csv`: CSV 형식 통계

## 📊 키워드 통계 확인

```bash
python3 keyword_manager.py
```

**출력 정보:**
- 전체 키워드 수
- 사용된 키워드 수
- 미사용 키워드 수
- 사용률

## 🎨 바이럴 키워드 작성 가이드

### 핵심 원칙

1. **구체적인 숫자 포함**
   - ❌ "AI 돈 버는 법"
   - ✅ "AI로 월 100만원 버는 법"

2. **호기심 자극**
   - ❌ "생산성 향상"
   - ✅ "하루 2시간 절약하는 자동화 루틴"

3. **실제 사례 강조**
   - ❌ "부업 추천"
   - ✅ "부업 없이 AI로 월 50만원 버는 실제 사례"

4. **비교형 활용**
   - ❌ "프레임워크 비교"
   - ✅ "Claude vs ChatGPT 실전 비교"

5. **트렌드 반영**
   - ❌ "기술 트렌드"
   - ✅ "2025년 가장 핫한 AI 도구 TOP 10"

### 카테고리별 전략

#### 수익 창출
- 구체적 금액: "월 100만원", "월 50만원"
- 시간 효율: "하루 10분", "하루 2시간 절약"
- 성공 사례: "실제 후기", "성공 스토리"

#### 기술/교육
- 실용성: "완벽 가이드", "실전 팁"
- 단계별: "3단계", "5단계", "10가지"
- 비교: "A vs B 실전 비교"

#### 커리어
- 성과: "연봉 2배", "구독자 10만"
- 로드맵: "10년 로드맵", "1년 준비"
- 후기: "성공 후기", "실제 사례"

## 📈 성과 추적 메트릭

### 추적 항목
- **포스트 수**: 키워드별 생성된 포스트 수
- **총 조회수**: 키워드별 총 조회수 (수동 입력)
- **총 공유수**: 키워드별 총 공유수 (수동 입력)
- **평균 내용 길이**: 포스트 평균 길이
- **첫/마지막 포스트 일자**: 포스트 생성 기간
- **카테고리/태그**: 관련 카테고리 및 태그

### 성과 분석

```python
from scripts.keyword_performance_tracker import KeywordPerformanceTracker

tracker = KeywordPerformanceTracker()

# 상위 키워드 가져오기
top_keywords = tracker.get_top_keywords('post_count', 10)

# 통계 출력
tracker.print_statistics()

# CSV 내보내기
tracker.export_to_csv()
```

## 🔄 워크플로우

### 1. 새 키워드 추가
```bash
# 방법 1: 스크립트 사용
python3 add_keyword.py "새 키워드" "카테고리" 1

# 방법 2: CSV 직접 편집
# keywords.csv 파일을 열어서 새 행 추가
```

### 2. 바이럴 키워드 생성
```bash
# 개선된 키워드 병합
python3 scripts/merge_viral_keywords.py

# 또는 기존 키워드 변환
python3 scripts/convert_to_viral.py
```

### 3. 성과 추적
```bash
# 정기적으로 실행하여 성과 추적
python3 scripts/keyword_performance_tracker.py
```

### 4. 통계 확인
```bash
# 키워드 통계 확인
python3 keyword_manager.py

# 성과 통계 확인
python3 scripts/keyword_performance_tracker.py
```

## 📝 키워드 CSV 형식

```csv
키워드,카테고리,우선순위,사용여부,사용일자
ChatGPT로 월 100만원 버는 법,수익,1,False,
AI로 하루 10분만에 블로그 포스트 10개 만들기,수익,1,False,
```

**필드 설명:**
- `키워드`: 블로그 포스트 키워드
- `카테고리`: 키워드 카테고리 (기술, 수익, 금융 등)
- `우선순위`: 우선순위 (1이 가장 높음)
- `사용여부`: 사용 여부 (True/False)
- `사용일자`: 사용된 날짜 (YYYY-MM-DD)

## 🎯 최적화 팁

1. **정기적 성과 분석**
   - 주간/월간 성과 추적
   - 인기 키워드 패턴 분석
   - 저성과 키워드 개선

2. **바이럴 키워드 우선 사용**
   - 우선순위 1로 설정
   - 바이럴 키워드 먼저 소진

3. **카테고리 균형**
   - 다양한 카테고리에서 키워드 선택
   - 인기 카테고리 집중

4. **트렌드 반영**
   - 시의성 있는 키워드 추가
   - 계절/이벤트 관련 키워드

## 🔗 관련 문서

- [키워드 개선 가이드](./KEYWORD_IMPROVEMENT_GUIDE.md)
- [자동화 시스템 가이드](../setup/README_AUTOMATION.md)
