# AI 블로그 설정 가이드

## 1단계: API 키 발급

### OpenAI API 키
1. https://platform.openai.com/ 접속
2. 계정 생성 또는 로그인
3. API Keys 메뉴에서 새 키 생성
4. `.env` 파일의 `OPENAI_API_KEY`에 입력

### Unsplash API 키
1. https://unsplash.com/developers 접속
2. 계정 생성 또는 로그인
3. New Application 생성
4. Access Key를 `.env` 파일의 `UNSPLASH_ACCESS_KEY`에 입력

## 2단계: 초기 설정

```bash
# 실행 권한 부여
chmod +x setup.sh run.sh

# 초기 설정 실행
./setup.sh
```

또는 수동으로:

```bash
# Python 패키지 설치
pip install -r requirements.txt

# 환경 변수 파일 생성
cp env.example .env
# .env 파일 편집하여 API 키 입력
```

## 3단계: Hugo 설치

### macOS
```bash
brew install hugo
```

### Linux
```bash
sudo apt-get install hugo
# 또는
sudo snap install hugo
```

### Windows
Chocolatey 사용:
```bash
choco install hugo-extended
```

또는 https://gohugo.io/installation/ 에서 다운로드

## 4단계: Hugo 사이트 초기화

```bash
hugo new site . --force
```

## 5단계: 설정 파일 수정

### .env 파일
```env
OPENAI_API_KEY=sk-...
UNSPLASH_ACCESS_KEY=...
BLOG_TITLE=내 블로그 이름
BLOG_URL=https://my-blog.com
POSTS_PER_DAY=10
```

### config.yaml
- `baseURL`: 블로그 URL
- `title`: 블로그 제목
- `params.adsense`: AdSense 설정
- `params.affiliate`: 제휴 링크 설정

## 6단계: 테스트

### 단일 포스트 생성 테스트
```bash
python3 generate_post.py
```

생성된 포스트는 `content/post/` 디렉토리에 저장됩니다.

### 로컬 미리보기
```bash
hugo server -D
```

브라우저에서 http://localhost:1313 접속

## 7단계: GitHub 설정

### 저장소 생성
1. GitHub에서 새 저장소 생성
2. 로컬 저장소와 연결:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

### GitHub Pages 활성화
1. 저장소 Settings > Pages
2. Source를 "GitHub Actions"로 선택
3. `.github/workflows/deploy.yml`이 자동으로 실행됩니다

### Cloudflare Pages 사용 (선택사항)
1. Cloudflare 대시보드에서 Pages 프로젝트 생성
2. GitHub 저장소 연결
3. 빌드 설정:
   - Build command: `hugo --minify`
   - Build output directory: `public`

## 8단계: 자동화 설정

### 로컬 스케줄러 실행
```bash
python3 scheduler.py
```

### 서버에서 실행 (cron 사용)
```bash
crontab -e
```

다음 내용 추가:
```
0 0 * * * cd /path/to/AIblog && /usr/bin/python3 scheduler.py
```

또는 GitHub Actions로 스케줄링:
`.github/workflows/schedule.yml` 파일 생성 (예제 제공 필요)

## 9단계: 수익화 설정

### Google AdSense
1. https://www.google.com/adsense/ 접속
2. 사이트 등록 및 승인 대기
3. `config.yaml`에 클라이언트 ID와 슬롯 ID 입력

### 제휴 링크
- **아마존 어소시에이트**: https://affiliate.amazon.com/
- **알리익스프레스 파트너**: https://portals.aliexpress.com/

각 프로그램에 가입 후 태그/ID를 `config.yaml`에 입력

## 10단계: SEO 최적화

### Google Search Console
1. https://search.google.com/search-console 접속
2. 사이트 등록
3. sitemap 제출: `https://your-blog.com/sitemap.xml`

### Google Analytics (선택사항)
1. Google Analytics 계정 생성
2. 추적 코드를 `layouts/_default/baseof.html`에 추가

## 문제 해결

### OpenAI API 오류
- API 키 확인
- 사용량 한도 확인: https://platform.openai.com/usage
- 결제 정보 확인

### Unsplash API 오류
- API 키 확인
- Rate limit 확인 (시간당 50회)

### Hugo 빌드 오류
- Hugo Extended 버전 설치 확인
- `hugo version`으로 버전 확인
- `config.yaml` 문법 확인

### 배포 오류
- GitHub Actions 로그 확인
- `.github/workflows/deploy.yml` 설정 확인
- GitHub Pages 설정 확인

## 추가 팁

1. **키워드 선택**: `generate_post.py`의 `generate_keyword()` 함수를 수정하여 원하는 키워드 추가
2. **템플릿 커스터마이징**: `layouts/` 디렉토리의 파일 수정
3. **스타일 변경**: `static/css/` 파일 수정
4. **포스트 품질 향상**: `generate_post.py`의 프롬프트 수정

## 지원

문제가 발생하면 GitHub Issues에 등록하거나 문서를 참고하세요.

