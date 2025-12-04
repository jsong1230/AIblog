# Project TODOs

## In Progress

- [ ] 광고 연동 완료 (AdSense, Amazon, Aliexpress)

## Backlog

- [ ] 광고 배치 최적화 및 A/B 테스트
- [ ] 광고 성과 추적 시스템 구축

## Done (Recent)

- [x] HISTORY.md를 루트 디렉토리로 이동 (2025-12-01)
  - [x] docs/HISTORY.md → HISTORY.md로 이동
  - [x] 관련 문서 링크 업데이트
- [x] 프로젝트 폴더 구조 정리 (2025-12-01)
  - [x] add_keyword.py → scripts/ 폴더로 이동
  - [x] fix_existing_posts.py → scripts/ 폴더로 이동
  - [x] 이동한 스크립트의 import 경로 수정
  - [x] README.md 사용법 업데이트
- [x] 하루 포스트 생성 개수 3개로 조정 (2025-12-01)
  - [x] scheduler.py 기본값 10개 → 3개로 변경
  - [x] auto_publish.py 기본값 10개 → 3개로 변경
  - [x] env.example 예시 값 10개 → 3개로 변경
- [x] 포스트 생성 시 날짜를 한국시간(KST) 기준으로 수정 (2025-11-28)
  - [x] generate_post.py에서 datetime.now()를 get_kst_now()로 변경
  - [x] 파일명, 타임스탬프, frontmatter 날짜 모두 KST 기준으로 생성
  - [x] auto_publish.py 커밋 메시지도 KST로 수정
- [x] GitHub Actions 워크플로우 푸시 오류 수정 (2025-11-28)
  - [x] git push 전 git pull 추가하여 원격 변경사항 먼저 가져오기
  - [x] 커밋 메시지 날짜를 한국시간(KST)으로 표시하도록 수정
- [x] 새로운 키워드 200개 추가 (2025-11-28)
  - [x] 다양한 카테고리로 흥미로운 키워드 197개 생성 및 추가
  - [x] 키워드 생성 스크립트 작성 (scripts/generate_new_keywords.py)
  - [x] 총 키워드 수: 342개 → 539개
