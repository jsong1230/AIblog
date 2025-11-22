# Project History

## 2025-11-23

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
