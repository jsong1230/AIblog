# Project TODOs

## In Progress
- [ ] Fix English navigation URL structure
    - Issue: English navigation links use `/en/AIblog/` instead of `/AIblog/en/`
    - Need to investigate Hugo multilingual URL configuration

## Backlog
- [ ] Review and optimize CSS for mobile devices
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
    - [x] Attempted to fix English navigation (partial - still has URL structure issue)
