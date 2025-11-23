# CSV 파일 관리 가이드

## 📁 CSV 파일 구조

### 메인 키워드 파일
- **위치**: `keywords.csv` (프로젝트 루트)
- **용도**: 블로그 포스트 생성에 사용되는 메인 키워드 데이터베이스
- **형식**: CSV (키워드, 카테고리, 우선순위, 사용여부, 사용일자)
- **상태**: ✅ Git에 커밋됨 (필수 파일)

### 성과 추적 파일
- **위치**: `data/keyword_performance.csv`
- **용도**: 키워드별 성과 통계 (포스트 수, 조회수, 공유수 등)
- **생성**: `scripts/keyword_performance_tracker.py` 실행 시 자동 생성
- **상태**: ⚠️ Git에 커밋되지 않음 (자동 생성 파일)

### 성과 데이터베이스
- **위치**: `data/keyword_performance.json`
- **용도**: 키워드 성과 데이터베이스 (JSON 형식)
- **생성**: `scripts/keyword_performance_tracker.py` 실행 시 자동 생성
- **상태**: ⚠️ Git에 커밋되지 않음 (자동 생성 파일)

## 🗑️ 임시 파일 (자동 무시됨)

다음 패턴의 파일은 `.gitignore`에 의해 자동으로 무시됩니다:
- `keywords_viral_*.csv` - 바이럴 키워드 임시 파일
- `*_sample.csv` - 샘플 파일
- `*_converted.csv` - 변환된 파일

이러한 파일들은 스크립트 실행 시 생성되지만 Git에 커밋되지 않습니다.

## 📝 파일 관리 규칙

### 유지해야 하는 파일
1. ✅ `keywords.csv` - 메인 키워드 데이터베이스 (필수)

### 자동 생성 파일 (Git 무시)
1. ⚠️ `data/keyword_performance.csv` - 성과 통계
2. ⚠️ `data/keyword_performance.json` - 성과 데이터베이스

### 삭제해도 되는 파일
1. ❌ `keywords_viral_improved.csv` - 이미 병합됨
2. ❌ `keywords_viral_converted_sample.csv` - 샘플 파일
3. ❌ 기타 `*_sample.csv`, `*_converted.csv` 패턴 파일

## 🔄 파일 생성/업데이트

### 키워드 성과 추적
```bash
# 성과 추적 실행 (CSV 및 JSON 자동 생성)
python3 scripts/keyword_performance_tracker.py
```

**생성되는 파일:**
- `data/keyword_performance.json` (업데이트)
- `data/keyword_performance.csv` (생성/업데이트)

### 키워드 변환 (임시 파일 생성)
```bash
# 변환된 키워드 파일 생성 (임시)
python3 scripts/convert_to_viral.py keywords.csv output.csv
```

**주의**: 생성된 파일은 Git에 커밋되지 않습니다.

## 📊 파일 크기 참고

- `keywords.csv`: ~17KB (342개 키워드)
- `data/keyword_performance.csv`: ~26KB (149개 포스트 추적)
- `data/keyword_performance.json`: ~변동 (JSON 형식)

## 🧹 정리 명령어

### 임시 파일 확인
```bash
ls -lh keywords_viral_*.csv *_sample.csv *_converted.csv 2>/dev/null
```

### 임시 파일 삭제
```bash
rm -f keywords_viral_*.csv *_sample.csv *_converted.csv
```

### 성과 파일 재생성
```bash
python3 scripts/keyword_performance_tracker.py
```

## ⚠️ 주의사항

1. **`keywords.csv`는 절대 삭제하지 마세요**
   - 모든 키워드 데이터가 저장된 메인 파일입니다.

2. **성과 추적 파일은 자동 생성됩니다**
   - 수동으로 편집할 필요가 없습니다.
   - 스크립트 실행 시 자동으로 업데이트됩니다.

3. **임시 파일은 정기적으로 정리하세요**
   - `.gitignore`에 의해 Git에 커밋되지 않지만, 로컬에 남아있을 수 있습니다.
