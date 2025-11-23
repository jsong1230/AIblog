# 개발 환경 일관성 가이드

다른 머신이나 IDE에서 작업할 때 프로젝트의 일관성을 유지하기 위한 가이드입니다.

## 📋 필수 사항

### 1. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 변수들을 설정하세요:

```bash
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Unsplash API Key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here

# Blog Configuration
BLOG_TITLE=AI 자동 블로그
BLOG_DESCRIPTION=AI가 자동으로 생성하는 블로그
BLOG_URL=https://jsong1230.github.io/AIblog
BLOG_AUTHOR=AI Blogger

# Post Generation
POSTS_PER_DAY=10
CONTENT_LANGUAGE=ko

# Analytics (Optional)
GOOGLE_ANALYTICS_ID=G-E8EV0XPYJH
PLAUSIBLE_DOMAIN=

# Google AdSense (Optional)
ADSENSE_CLIENT_ID=ca-pub-5954947755126324
ADSENSE_SLOT_ID=

# Affiliate Links (Optional)
AMAZON_AFFILIATE_TAG=
ALIEXPRESS_AFFILIATE_ID=
```

**참고**: `.env` 파일은 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.  
새 환경에서는 `env.example`을 참고하여 `.env` 파일을 생성하세요.

### 2. Python 환경 설정

#### 필수 패키지 설치
```bash
pip install -r requirements.txt
```

또는 개별 설치:
```bash
pip install openai python-dotenv frontmatter pyyaml requests
```

#### Python 버전
- Python 3.8 이상 권장

### 3. Hugo 설치

#### macOS
```bash
brew install hugo
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install hugo

# 또는 snap
sudo snap install hugo
```

#### Windows
- https://github.com/gohugoio/hugo/releases 에서 다운로드
- 또는 `choco install hugo` (Chocolatey 사용 시)

#### 버전 확인
```bash
hugo version
```

### 4. Git 설정

#### 저장소 클론
```bash
git clone https://github.com/jsong1230/AIblog.git
cd AIblog
```

#### 브랜치 확인
```bash
git branch
# main 브랜치에서 작업
```

## 📁 프로젝트 구조 이해

### 핵심 디렉토리

```
AIblog/
├── content/post/          # 블로그 포스트 (마크다운 파일)
├── layouts/               # Hugo 템플릿
│   ├── _default/         # 기본 템플릿
│   └── partials/         # 부분 템플릿 (adsense, affiliate 등)
├── static/                # 정적 파일 (CSS, JS, 이미지)
├── scripts/                # 유틸리티 스크립트
│   ├── merge_viral_keywords.py
│   ├── convert_to_viral.py
│   └── keyword_performance_tracker.py
├── docs/                  # 문서
│   ├── keywords/         # 키워드 관리 가이드
│   ├── monetization/     # 수익화 가이드
│   └── setup/            # 설정 가이드
├── data/                  # 데이터 파일 (자동 생성)
│   └── keyword_performance.json
├── keywords.csv           # 메인 키워드 데이터베이스
├── config.yaml            # Hugo 설정 파일
└── .env                   # 환경 변수 (로컬에 생성 필요)
```

### 중요 파일

#### 키워드 관리
- `keywords.csv`: 메인 키워드 데이터베이스 (342개 키워드)
- `keyword_manager.py`: 키워드 관리 클래스
- `scripts/merge_viral_keywords.py`: 바이럴 키워드 병합
- `scripts/convert_to_viral.py`: 키워드 바이럴 변환
- `scripts/keyword_performance_tracker.py`: 성과 추적

#### 설정 파일
- `config.yaml`: Hugo 사이트 설정 (광고, 분석 등)
- `.env`: 환경 변수 (Git에 커밋되지 않음)
- `env.example`: 환경 변수 예시

#### 문서
- `docs/keywords/KEYWORD_MANAGEMENT.md`: 키워드 관리 가이드
- `docs/monetization/AD_INTEGRATION_STATUS.md`: 광고 연동 현황
- `docs/README.md`: 전체 문서 인덱스

## 🔧 개발 워크플로우

### 1. 로컬 개발 서버 실행

```bash
# Hugo 서버 시작
hugo server

# 또는 포트 지정
hugo server -p 1313

# 미리보기 URL: http://localhost:1313
```

### 2. 포스트 생성

```bash
# 단일 포스트 생성
python3 generate_post.py

# 자동 발행 (N개 포스트 + 빌드 + 배포)
python3 auto_publish.py
```

### 3. 키워드 관리

```bash
# 키워드 통계 확인
python3 keyword_manager.py

# 바이럴 키워드 병합
python3 scripts/merge_viral_keywords.py

# 키워드 성과 추적
python3 scripts/keyword_performance_tracker.py
```

### 4. 빌드 및 배포

```bash
# 로컬 빌드
hugo --minify

# 빌드 결과: public/ 디렉토리

# GitHub Pages 배포는 자동화됨 (.github/workflows/deploy.yml)
```

## ⚙️ 설정 확인 체크리스트

새 환경에서 작업 시작 전 확인사항:

- [ ] `.env` 파일 생성 및 환경 변수 설정
- [ ] Python 패키지 설치 (`pip install -r requirements.txt`)
- [ ] Hugo 설치 및 버전 확인 (`hugo version`)
- [ ] Git 저장소 클론 및 브랜치 확인
- [ ] `keywords.csv` 파일 존재 확인
- [ ] `config.yaml` 설정 확인
- [ ] 로컬 서버 실행 테스트 (`hugo server`)

## 🔐 GitHub Secrets (CI/CD용)

GitHub Actions에서 사용하는 Secrets는 저장소 설정에서 관리됩니다:

**현재 등록된 Secrets:**
- `OPENAI_API_KEY` (github-pages 환경)
- `POSTS_PER_DAY` (github-pages 환경)
- `UNSPLASH_ACCESS_KEY` (github-pages 환경)

**설정 위치:**
GitHub 저장소 → Settings → Secrets and variables → Actions

## 📊 데이터 파일 관리

### 자동 생성 파일 (Git 무시됨)

다음 파일들은 자동 생성되며 Git에 커밋되지 않습니다:

- `data/keyword_performance.json`: 키워드 성과 데이터베이스
- `data/keyword_performance.csv`: 키워드 성과 통계
- `public/`: Hugo 빌드 결과물
- `.hugo/`: Hugo 캐시

### 임시 파일 (Git 무시됨)

`.gitignore`에 의해 자동으로 무시되는 파일:

- `keywords_viral_*.csv`: 바이럴 키워드 임시 파일
- `*_sample.csv`: 샘플 파일
- `*_converted.csv`: 변환된 파일

## 🐛 문제 해결

### 일반적인 문제

#### 1. Python 모듈을 찾을 수 없음
```bash
# 가상 환경 활성화 (권장)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

#### 2. Hugo 명령어를 찾을 수 없음
```bash
# Hugo 설치 확인
which hugo  # macOS/Linux
where hugo  # Windows

# PATH에 추가되지 않은 경우 전체 경로 사용
/usr/local/bin/hugo server
```

#### 3. 환경 변수 로드 실패
```bash
# .env 파일 존재 확인
ls -la .env

# env.example을 복사하여 생성
cp env.example .env
# 그 다음 .env 파일 편집
```

#### 4. 키워드 파일 없음
```bash
# keywords.csv 파일 확인
ls -lh keywords.csv

# 없으면 Git에서 확인
git status
git checkout keywords.csv
```

## 📚 추가 리소스

### 문서
- [전체 문서 인덱스](./README.md)
- [키워드 관리 가이드](./keywords/KEYWORD_MANAGEMENT.md)
- [광고 연동 현황](./monetization/AD_INTEGRATION_STATUS.md)
- [자동화 가이드](./setup/README_AUTOMATION.md)

### 외부 링크
- [Hugo 공식 문서](https://gohugo.io/documentation/)
- [GitHub Actions 문서](https://docs.github.com/en/actions)

## 💡 팁

1. **가상 환경 사용**: Python 프로젝트는 가상 환경 사용을 권장합니다.
2. **정기적 동기화**: 작업 전 `git pull`로 최신 변경사항 가져오기
3. **로컬 테스트**: 변경사항은 로컬에서 테스트 후 커밋
4. **문서 참고**: 문제 발생 시 `docs/` 디렉토리의 가이드 참고

## 🔄 환경 동기화

다른 환경으로 전환할 때:

1. **현재 환경에서 커밋/푸시**
   ```bash
   git add .
   git commit -m "작업 내용"
   git push origin main
   ```

2. **새 환경에서 풀**
   ```bash
   git pull origin main
   ```

3. **환경 변수 설정**
   - `.env` 파일 생성 및 설정

4. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

5. **테스트**
   ```bash
   python3 keyword_manager.py  # 키워드 관리 테스트
   hugo server                  # 서버 실행 테스트
   ```
