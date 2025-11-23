# Project TODOs

## In Progress
- 현재 진행 중인 작업 없음

## Backlog
- [ ] Add more keywords to keywords.csv
- [ ] Implement automated testing for post generation
- [ ] Add analytics tracking

## Done
- [x] Project Setup & Synchronization
    - [x] Pull latest changes from GitHub
    - [x] Create TODO.md
    - [x] Create HISTORY.md
    - [x] Verify environment consistency
    - [x] Implement multilingual support (Korean/English)
- [x] Fix Post Image Display Issue (2025-11-23)
    - [x] Limited header image height to 400px
    - [x] Ensured text content visible without scrolling
- [x] Fix Markdown Rendering in Descriptions (2025-11-23)
    - [x] Updated `generate_post.py` to strip markdown from descriptions
    - [x] Created `fix_existing_posts.py` to fix 87 existing posts
    - [x] Removed duplicate H1 headers from post content
- [x] Fix Navigation Issues (2025-11-23)
    - [x] Fixed Korean menu URLs
    - [x] Fixed English navigation URL structure
    - [x] Fixed logo links to use correct paths (/AIblog/ and /AIblog/en/)
- [x] Multilingual Date Format & UI Fixes (2025-11-23)
    - [x] Fixed logo links for both Korean and English sites
    - [x] Implemented English ordinal date format (Nov 22nd, 2025)
    - [x] Removed markdown headers (#) from post summaries
    - [x] Applied language-specific date formats to all pages (index, categories, tags, single)
    - [x] Fixed date format detection using $.Language.Lang in range loops
- [x] Bilingual Posting Setup (2025-11-23)
    - [x] Modified generate_post() to generate English content directly (not just translate)
    - [x] Ensured both Korean and English posts are always created
    - [x] Added fallback to translation if direct English generation fails
