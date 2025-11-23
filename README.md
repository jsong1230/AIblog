# AI 자동 블로그 생성 시스템

ChatGPT와 Unsplash API를 활용하여 자동으로 블로그 포스트를 생성하고 Hugo로 배포하는 시스템입니다.

## 🚀 기능

- **자동 콘텐츠 생성**: ChatGPT API를 사용하여 SEO 최적화된 블로그 포스트 자동 생성
- **자동 이미지 삽입**: Unsplash API를 사용하여 관련 이미지 자동 삽입
- **자동 배포**: GitHub Actions를 통한 자동 배포 (GitHub Pages / Cloudflare Pages)
- **스케줄링**: 하루 10개 포스트 자동 발행
- **SEO 최적화**: 메타 태그, sitemap, robots.txt 자동 생성
- **수익화**: Google AdSense 및 제휴 링크 지원

## 📋 요구사항

- Python 3.8+
- Hugo (Extended 버전)
- OpenAI API 키
- Unsplash API 키
- GitHub 계정

## 🛠️ 설치

1. 저장소 클론:
```bash
git clone <your-repo-url>
cd AIblog
```

2. Python 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정:
```bash
cp env.example .env
# .env 파일을 편집하여 API 키 입력
```

4. Hugo 설치 (macOS):
```bash
brew install hugo
```

5. Hugo 사이트 초기화 (처음 한 번만):
```bash
hugo new site . --force
```

## ⚙️ 설정

### 초기 설정

**상세 가이드:** [설치 및 설정 가이드](./docs/setup/SETUP_GUIDE.md)

### 자동화 설정

**상세 가이드:** [자동화 시스템 가이드](./docs/setup/README_AUTOMATION.md)

### .env 파일 설정

```env
OPENAI_API_KEY=your_openai_api_key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
BLOG_TITLE=AI 자동 블로그
BLOG_DESCRIPTION=AI가 자동으로 생성하는 블로그
BLOG_URL=https://your-blog-domain.com
POSTS_PER_DAY=10
```

### config.yaml 설정

`config.yaml` 파일에서 블로그 제목, 설명, URL 등을 설정합니다.

## 📝 사용법

### 단일 포스트 생성

```bash
python generate_post.py
```

### 배치 포스트 생성 (하루치)

```bash
python scheduler.py
```

### 자동 스케줄링 실행

```bash
python scheduler.py
```

스케줄러는 매일 자정에 자동으로 포스트를 생성합니다.

### 로컬에서 Hugo 사이트 미리보기

```bash
hugo server -D
```

브라우저에서 `http://localhost:1313` 접속

### 배포

변경사항을 GitHub에 푸시하면 GitHub Actions가 자동으로 배포합니다:

```bash
git add .
git commit -m "새 포스트 추가"
git push
```

또는 자동 배포 스크립트 사용:

```bash
python deploy.py
```

## 🔄 워크플로우

1. **포스트 생성**: `generate_post.py`가 ChatGPT로 콘텐츠 생성
2. **이미지 추가**: Unsplash에서 관련 이미지 가져오기
3. **파일 저장**: `content/post/` 디렉토리에 마크다운 파일 저장
4. **자동 배포**: GitHub Actions가 Hugo로 빌드 후 배포

## 📁 프로젝트 구조

```
AIblog/
├── content/
│   └── post/          # 생성된 포스트 파일들
├── layouts/           # Hugo 템플릿
├── static/            # 정적 파일 (CSS, JS)
├── docs/              # 프로젝트 문서
│   ├── setup/         # 설치 및 설정 가이드
│   ├── monetization/  # 수익화 가이드
│   ├── analytics/     # Analytics 설정 가이드
│   ├── deployment/    # 배포 관련 문서
│   └── HISTORY.md     # 프로젝트 변경 이력
├── .github/
│   └── workflows/     # GitHub Actions 워크플로우
├── generate_post.py   # 포스트 생성 스크립트
├── scheduler.py       # 스케줄러
├── deploy.py          # 배포 스크립트
├── config.yaml        # Hugo 설정
├── requirements.txt   # Python 의존성
└── TODO.md            # 할 일 목록
```

**문서 인덱스:** [docs/README.md](./docs/README.md)

## 💰 수익화

### Google AdSense

1. Google AdSense 계정 생성 및 사이트 승인
2. `config.yaml`에 AdSense 정보 입력
3. 광고가 자동으로 포스트에 삽입됩니다

**상세 가이드:** [AdSense 설정 가이드](./docs/monetization/ADSENSE_SETUP.md)

### 제휴 링크

- 아마존 어소시에이트
- 알리익스프레스 파트너 프로그램

제휴 링크는 포스트 하단에 자동으로 표시됩니다.

**상세 가이드:**
- [제휴 링크 설정](./docs/monetization/AFFILIATE_SETUP.md)
- [알리익스프레스 파트너 가이드](./docs/monetization/ALIEXPRESS_PARTNER_GUIDE.md)

## 📊 Analytics 설정

방문자 통계를 추적하려면 Analytics를 설정하세요:

- **[Analytics 설정 가이드](./docs/analytics/ANALYTICS_SETUP.md)** - Google Analytics 및 Plausible Analytics 설정 방법

## 🔒 법적 고려사항

- AI 생성 콘텐츠임을 명시 (선택사항)
- Unsplash 이미지 크레딧 표시 (자동 처리됨)
- 제휴 링크는 `rel="nofollow sponsored"` 속성 사용
- 개인정보보호정책 및 이용약관 페이지 추가 권장

## 📈 SEO 최적화

- 자동 생성되는 메타 태그
- Open Graph 태그
- Twitter Card 태그
- Sitemap 자동 생성
- robots.txt 설정

## 🐛 문제 해결

### OpenAI API 오류
- API 키가 올바른지 확인
- API 사용량 한도 확인

### Unsplash API 오류
- API 키 확인
- 네트워크 연결 확인

### Hugo 빌드 오류
- Hugo Extended 버전 설치 확인
- `config.yaml` 문법 확인

### 마크다운이 포스트 설명에 표시되는 경우
- `fix_existing_posts.py` 스크립트 실행:
  ```bash
  python fix_existing_posts.py
  ```
- 새 포스트는 자동으로 마크다운이 제거됩니다

### 포스트 이미지가 너무 큰 경우
- `static/css/main.css`에서 `.post-image` 스타일 확인
- `max-height` 값 조정 (기본값: 400px)

### 영문 네비게이션 404 오류
- 현재 알려진 이슈: Hugo multilingual URL 구조 문제
- 임시 해결책: 영문 사이트는 `/AIblog/en/`에서 접근 가능

## 🛠️ 유틸리티 스크립트

### fix_existing_posts.py
기존 포스트의 frontmatter에서 마크다운 문법을 제거하는 스크립트:
```bash
python fix_existing_posts.py
```

## 📝 라이선스

MIT License

## 🤝 기여

이슈 및 풀 리퀘스트 환영합니다!

