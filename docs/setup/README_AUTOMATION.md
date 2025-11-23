# 자동화 시스템 가이드

## 🎯 핵심 자동화 루프

```
키워드 리스트 (CSV) 
  ↓
스크립트가 키워드 선택
  ↓
LLM 호출 (ChatGPT) → 글 + 제목 + 메타정보 생성
  ↓
Unsplash API → 이미지 자동 삽입
  ↓
Markdown 파일로 저장 (content/post/)
  ↓
Hugo 정적 사이트 빌드
  ↓
GitHub Actions로 자동 배포
```

## 📋 키워드 관리

### 키워드 CSV 파일 구조

`keywords.csv` 파일 형식:
```csv
키워드,카테고리,우선순위,사용여부,사용일자
AI 블로그 자동화,기술,1,false,
ChatGPT 활용법,기술,1,false,
```

### 키워드 추가

#### 방법 1: 스크립트 사용
```bash
python3 add_keyword.py "새 키워드" "카테고리" 1
```

#### 방법 2: CSV 파일 직접 편집
`keywords.csv` 파일을 열어서 새 행 추가

#### 방법 3: Python 스크립트
```python
from keyword_manager import KeywordManager

manager = KeywordManager()
manager.add_keyword("새 키워드", "카테고리", 1)
```

### 키워드 통계 확인

```bash
python3 keyword_manager.py
```

### 모든 키워드 재사용

```python
from keyword_manager import KeywordManager

manager = KeywordManager()
manager.reset_all_keywords()
```

## 🤖 자동 발행 시스템

### 로컬에서 실행

#### 단일 포스트 생성
```bash
python3 generate_post.py
```

#### 자동 발행 (N개 포스트 + 빌드 + 배포)
```bash
python3 auto_publish.py
```

환경 변수로 제어:
- `POSTS_PER_DAY`: 생성할 포스트 수 (기본: 10)
- `AUTO_BUILD`: 자동 빌드 여부 (기본: true)
- `AUTO_DEPLOY`: 자동 배포 여부 (기본: true)

### 스케줄러 사용 (로컬)

```bash
python3 scheduler.py
```

매일 자정에 자동으로 포스트 생성

### GitHub Actions 자동화

`.github/workflows/schedule.yml`이 매일 자동으로 실행됩니다.

#### 수동 실행
GitHub 저장소의 Actions 탭에서 "Scheduled Post Generation & Deploy" 워크플로우를 수동으로 실행할 수 있습니다.

#### 스케줄 변경
`.github/workflows/schedule.yml`의 `cron` 설정을 수정:
```yaml
schedule:
  - cron: '0 15 * * *'  # 매일 UTC 15:00 (한국시간 자정)
```

## 🔄 전체 워크플로우

### 1. 키워드 준비
```bash
# 키워드 추가
python3 add_keyword.py "Python 기초" 기술 1

# 키워드 확인
python3 keyword_manager.py
```

### 2. 포스트 생성 및 배포

#### 자동 (권장)
```bash
python3 auto_publish.py
```

이 스크립트는 다음을 자동으로 수행합니다:
1. 키워드 선택 (미사용 키워드 중에서)
2. ChatGPT로 글 생성
3. Unsplash에서 이미지 가져오기
4. Markdown 파일 저장
5. 키워드 사용 표시
6. Hugo 사이트 빌드
7. Git 커밋 및 푸시

#### 수동 단계별
```bash
# 1. 포스트 생성
python3 generate_post.py

# 2. Hugo 빌드
hugo --minify

# 3. Git 배포
git add .
git commit -m "새 포스트"
git push
```

## 📊 모니터링

### 키워드 사용 현황
```bash
python3 keyword_manager.py
```

출력 예시:
```
📊 키워드 통계:
   전체: 25개
   사용됨: 10개
   미사용: 15개
   사용률: 40.0%
```

### 키워드 사용 로그
`keywords_used.log` 파일에서 키워드 사용 이력을 확인할 수 있습니다.

## ⚙️ 환경 변수 설정

`.env` 파일:
```env
# 포스트 생성
POSTS_PER_DAY=10
CONTENT_LANGUAGE=ko

# 자동화 설정
AUTO_BUILD=true
AUTO_DEPLOY=true

# API 키
OPENAI_API_KEY=sk-...
UNSPLASH_ACCESS_KEY=...
```

## 🚀 배포 옵션

### GitHub Pages (무료)
- GitHub Actions가 자동으로 배포
- `gh-pages` 브랜치에 빌드된 사이트 배포

### Cloudflare Pages (무료)
1. Cloudflare 대시보드에서 Pages 프로젝트 생성
2. GitHub 저장소 연결
3. 빌드 설정:
   - Build command: `hugo --minify`
   - Build output directory: `public`
4. 자동 배포 활성화

### Vercel (무료)
1. Vercel에 GitHub 저장소 연결
2. 빌드 설정 자동 감지
3. 자동 배포

## 🔧 문제 해결

### 키워드가 모두 사용됨
```python
from keyword_manager import KeywordManager

manager = KeywordManager()
manager.reset_all_keywords()  # 모든 키워드 재사용
```

### 빌드 실패
- Hugo가 설치되어 있는지 확인: `hugo version`
- `config.yaml` 문법 확인
- 빌드 로그 확인

### 배포 실패
- Git 설정 확인
- GitHub 토큰 확인
- 저장소 권한 확인

## 📈 최적화 팁

1. **키워드 품질**: SEO에 유리한 키워드 선택
2. **우선순위 관리**: 중요한 키워드에 낮은 우선순위 번호 부여
3. **카테고리 분류**: 일관된 카테고리 사용
4. **API 레이트 리밋**: 포스트 간 30초 대기 시간 유지
5. **정기적 모니터링**: 키워드 통계를 주기적으로 확인

## 🎯 수익화 연동

### Google AdSense
`config.yaml`에 설정:
```yaml
params:
  adsense:
    enabled: true
    clientId: "your-client-id"
    slotId: "your-slot-id"
```

### 제휴 링크
`config.yaml`에 설정:
```yaml
params:
  affiliate:
    amazon:
      enabled: true
      tag: "your-tag"
    aliexpress:
      enabled: true
      id: "your-id"
```

## 📝 체크리스트

- [ ] 키워드 CSV 파일 준비
- [ ] API 키 설정 (.env)
- [ ] Hugo 설치 확인
- [ ] GitHub 저장소 설정
- [ ] GitHub Actions 워크플로우 확인
- [ ] 테스트 포스트 생성
- [ ] 자동 배포 테스트
- [ ] AdSense/제휴 링크 설정

