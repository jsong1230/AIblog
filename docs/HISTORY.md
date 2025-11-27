# Project History

## 2025-11-28

### GitHub Actions 워크플로우 푸시 오류 수정
- **Issue**: 워크플로우가 포스트 생성 후 푸시할 때 원격 저장소에 새로운 커밋이 있어서 충돌 발생. 또한 커밋 메시지 날짜가 UTC로 표시됨
- **Solution**: 
  - `git push` 전에 `git fetch`와 `git pull`을 추가하여 원격 변경사항을 먼저 가져오도록 수정
  - 커밋 메시지 날짜를 한국시간(KST)으로 표시하도록 `TZ='Asia/Seoul'` 환경변수 추가
  - rebase 실패 시 no-rebase로 fallback 처리
- **Files Modified**:
  - `.github/workflows/schedule.yml`
- **Commits**:
  - (아직 커밋 전)

### 새로운 키워드 200개 추가
- **Issue**: 기존 키워드가 소진될 가능성, 더 다양한 주제의 포스트 생성 필요
- **Solution**: 
  - 다양한 카테고리로 흥미로운 키워드 197개 생성 및 추가
  - 기술(30개), AI(20개), 비즈니스(25개), 마케팅(25개), 금융(20개), 생산성(20개), 건강(15개), 교육(15개), 디자인(10개), 블록체인(10개), 라이프(10개) 등 균형있게 구성
  - 키워드 생성 스크립트 작성 (`scripts/generate_new_keywords.py`)
  - 중복 키워드 자동 제거 기능 포함
- **Files Modified**:
  - `keywords.csv` (342개 → 539개)
  - `scripts/generate_new_keywords.py` (신규 생성)
- **Commits**:
  - (아직 커밋 전)

## 2025-11-26

### 영어 포스트 태그 통합
- **Issue**: 영어 포스트의 태그가 너무 많아 관리가 어려움 (97개의 다양한 태그)
- **Solution**: 
  - 세부 태그를 주제별 카테고리로 통합하는 스크립트 작성 (`scripts/consolidate_english_tags.py`)
  - 54개 영어 포스트의 태그를 12개 주제 카테고리로 통합:
    * AI Automation (11개)
    * Development (12개)
    * Blockchain (11개)
    * Online Business (6개)
    * Learning (4개)
    * Finance (3개)
    * Lifestyle (3개)
    * 기타: Design, Education, Career, Productivity
- **Files Modified**:
  - `scripts/consolidate_english_tags.py` (신규 생성)
  - `content/post/*.en.md` (54개 파일)
- **Commits**:
  - `7c0ceff` - "Refactor: 영어 포스트 태그 주제별 통합"

### Cursor Rules 업데이트
- **Issue**: 커밋 전 필수 작업(TODO.md, HISTORY.md 업데이트)이 누락되는 경우 발생, 날짜 기록이 부정확함, 자동 커밋/푸시로 인한 문제
- **Solution**:
  - `.cursorrules` 파일에 커밋 전 필수 작업 규칙 강화
  - TODO.md, HISTORY.md, README.md 업데이트를 커밋 전 필수 작업으로 명시
  - 날짜 기록 규칙 추가 (YYYY-MM-DD 형식, 정확한 날짜 사용)
  - 커밋/푸시 전 사용자 승인 필수 규칙 추가
  - Git 저장소 초기화 규칙 추가 (로컬/원격 저장소 확인)
- **Files Modified**:
  - `.cursorrules`
- **Commits**:
  - (아직 커밋 전)

## 2025-11-23 (오늘 작업 - 후반)

### 다국어 날짜 포맷 및 UI 수정
- **Issue**: 영문 사이트에서 날짜가 한글로 표시되고, 로고 링크가 잘못된 경로로 이동
- **Solution**:
  - 로고 링크를 언어별로 명시적 경로 설정 (`/AIblog/` 또는 `/AIblog/en/`)
  - 영문 사이트 날짜 포맷을 서수 형식으로 변경 ("Nov 22nd, 2025")
  - Summary에서 마크다운 헤더(`#`) 제거
  - 모든 페이지(메인, Categories, Tags, 포스트 상세)에 언어별 날짜 포맷 적용
- **Files Modified**:
  - `layouts/_default/baseof.html`
  - `layouts/index.html`
  - `layouts/_default/list.html`
  - `layouts/taxonomy/term.html`
  - `layouts/taxonomy/list.html`
  - `layouts/_default/single.html`
- **Commits**:
  - `323e5dc` - "Fix: Update logo links, date formats, and remove markdown headers from summaries"
  - `6b405d1` - "Fix: Correct logo links, date formats, and markdown removal in summaries"
  - `920ab15` - "Fix: Use .Language.Lang instead of .Site.LanguageCode for date format detection"
  - `c48d741` - "Fix: Use $ to access parent context language in date format"
  - `03aa1de` - "Fix: Apply language-specific date format to single post pages"

## 2025-11-23 (오늘 작업 - 전반)

### CSS 스타일링 문제 해결
- **Issue**: 한글/영문 사이트 모두에서 CSS가 적용되지 않아 텍스트만 표시됨
- **Root Cause**: CSS/JS 파일 경로에 공백이 있어 경로가 잘못 생성됨 (`{{ " css/main.css" }}` → 잘못된 경로)
- **Solution**: 
  - CSS/JS 경로에서 공백 제거 (`{{ "/css/main.css" | absURL }}`)
  - 최종적으로 `.Site.BaseURL`을 직접 사용하여 명시적 경로 설정
  - 언어별 폰트 추가 (한글: Noto Sans KR, 영문: Inter)
- **Files Modified**: 
  - `layouts/_default/baseof.html`
  - `static/css/main.css`
- **Commits**:
  - `fa5635e` - "Fix: Remove spaces from CSS/JS paths to fix styling issues"
  - `e018ac9` - "Fix: Use explicit BaseURL for CSS/JS to ensure correct paths"
  - `4a2026b` - "Fix: Add slash between BaseURL and CSS/JS paths"

### 영어 사이트 네비게이션 링크 수정
- **Issue**: 영어 사이트(`/AIblog/en/`)에서 Home, Categories, Tags 링크가 올바르게 작동하지 않음
- **Solution**: 
  - 영어 메뉴 URL을 상대 경로로 설정 (`en/`, `en/categories/`, `en/tags/`)
  - 메뉴 링크에 `absLangURL` 사용하여 baseURL과 올바르게 결합
- **Files Modified**:
  - `config.yaml`
  - `layouts/_default/baseof.html`
- **Commits**:
  - `59c4d87` - "Fix: Set explicit /en/ paths for English menu URLs"
  - `a1d062f` - "Fix: Use absLangURL for menu links to properly handle multilingual URLs"

### 키워드 CSV 업데이트
- **Action**: `keywords.csv` 파일 업데이트 후 GitHub에 푸시
- **Commit**: `b4554de` - "Update keywords.csv"

## 2025-11-23 (이전 작업)

### Post Image Display Fix
- **Issue**: Header images in posts were displayed at full size, taking up entire viewport and pushing text below the fold
- **Solution**: Added CSS rules to limit `.post-image` height to 400px with `object-fit: cover`
- **Files Modified**: `static/css/main.css`
- **Commit**: `dbddb47` - "Fix: Limit post header image height to 400px to ensure text visibility"

### Markdown Rendering Fix
- **Issue**: Post descriptions contained markdown syntax (`#`, `##`, etc.) displayed as raw text instead of HTML
- **Root Cause**: `generate_post.py` was copying raw markdown content into `description` and `seo.description` fields
- **Solution**: 
  - Added `strip_markdown_for_description()` function to remove all markdown syntax
  - Added `remove_duplicate_h1_from_content()` to remove redundant H1 headers
  - Created `fix_existing_posts.py` script to fix 87 existing posts
- **Files Modified**: 
  - `generate_post.py`
  - All 87 Korean post files in `content/post/`
- **Commits**:
  - `399afac` - "Fix: Remove markdown from descriptions and fix English navigation URLs"
  - `01caf48` - "Fix: Remove markdown from descriptions in all existing posts"

### Navigation Issues
- **Issue**: English navigation links (Home, Categories, Tags) leading to 404 pages
- **Attempted Solutions**:
  - Changed English menu URLs from `/en/categories/` to `/categories/` (to work with `relLangURL`)
  - Added `defaultContentLanguageInSubdir: false` to config
  - Attempted language-specific `baseURL` configuration (reverted due to Korean homepage 404)
  - Fixed broken HTML syntax in `baseof.html` logo link
- **Current Status**: Partially resolved - Korean navigation works, English navigation still has URL structure issues (`/en/AIblog/` instead of `/AIblog/en/`)
- **Files Modified**:
  - `config.yaml`
  - `layouts/_default/baseof.html`
- **Commits**:
  - `72c6fee` - "Fix: Home/logo link to use relLangURL for multilingual support"
  - `eb3e9c2` - "Fix: Correct language URL structure to use AIblog/en instead of en/AIblog"
  - `9cf5b2f` - "Fix: Set language-specific baseURLs to correct URL structure"
  - `03f00d0` - "Fix: Use absLangURL for logo link to respect language-specific baseURL"
  - `1e8a952` - "Revert: Remove language-specific baseURLs to fix Korean homepage"

### Files Created
- `fix_existing_posts.py` - Script to batch-fix markdown in existing post frontmatter

## Previous History

### 2025-11-15 - Initial Setup
- **System**: Created AI automated blog system with Hugo
- **Setup**: Configured multilingual support (Korean/English)
- **Features**: ChatGPT integration, Unsplash image API, automated deployment
