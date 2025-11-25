#!/usr/bin/env python3
"""
파일명이 변경된 영어 포스트에 대한 리다이렉트 HTML 파일 생성
GitHub Pages에서 기존 한글 파일명 URL로 접근하는 사용자를 새 영어 파일명으로 리다이렉트
"""
from pathlib import Path
import re

# 파일명 매핑 (한글 파일명 -> 영어 파일명)
FILENAME_MAPPING = {
    "2025-11-23-모바일-uiux-디자인-핵심-원칙-20251123152643.en.md": "2025-11-23-key-principles-of-mobile-uiux-design-secrets-to-user-centered-design-20251123152643.en.md",
    "2025-11-23-디지털-제품-판매-20251123152530.en.md": "2025-11-23-selling-digital-products-the-perfect-guide-to-success-20251123152530.en.md",
    "2025-11-23-알고리즘-공부-효율-2배-올리는-법-20251123153135.en.md": "2025-11-23-how-to-double-your-algorithm-study-efficiency-effective-learning-strategies-20251123153135.en.md",
    "2025-11-23-온체인-고점-예측-20251123153346.en.md": "2025-11-23-on-chain-peak-prediction-price-outlook-through-blockchain-analysis-20251123153346.en.md",
    "2025-11-23-자녀-코딩-교육-시작하는-최적-시기-20251123152425.en.md": "2025-11-23-the-best-time-to-start-coding-education-for-your-children-when-is-it-most-suitab-20251123152425.en.md",
    "2025-11-23-개발자-로드맵-20251123153024.en.md": "2025-11-23-your-ultimate-guide-to-the-developer-roadmap-navigating-the-path-to-becoming-a-s-20251123153024.en.md",
    "2025-11-23-소셜-미디어-전략으로-팔로워-10배-늘리기-20251123153239.en.md": "2025-11-23-increasing-your-followers-by-10x-with-social-media-strategy-successful-approache-20251123153239.en.md",
    "2025-11-23-리팩토링-기법-20251123152903.en.md": "2025-11-23-mastering-refactoring-techniques-boosting-your-code-quality-20251123152903.en.md",
    "2025-11-23-ai-뉴스레터로-구독자-1만명-모으기-20251123152748.en.md": "2025-11-23-how-to-build-a-10000-subscriber-list-with-ai-newsletters-20251123152748.en.md",
    "2025-11-23-온라인-비즈니스-시작하는-첫-단계-20251123153453.en.md": "2025-11-23-the-first-steps-to-starting-an-online-business-a-guide-for-a-successful-start-20251123153453.en.md",
}

def get_slug_from_filename(filename):
    """파일명에서 slug 추출 (Hugo 방식: 날짜만 제거, 타임스탬프 포함)"""
    # .en.md 제거
    base = filename.replace('.en.md', '').replace('.md', '')
    # 날짜 부분 제거 (YYYY-MM-DD-)
    parts = base.split('-')
    if len(parts) >= 4:
        # 날짜(3개) + slug + 타임스탬프(1개) 형식
        # Hugo는 날짜만 제거하고 나머지(slug + 타임스탬프)를 slug로 사용
        slug_parts = parts[3:]  # 타임스탬프 포함
        return '-'.join(slug_parts)
    return base

def create_redirect_html(old_slug, new_slug, output_dir):
    """리다이렉트 HTML 파일 생성"""
    old_url = f"/AIblog/en/post/{old_slug}/"
    new_url = f"/AIblog/en/post/{new_slug}/"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={new_url}">
    <link rel="canonical" href="{new_url}">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="{new_url}">new post URL</a>...</p>
    <script>
        window.location.href = "{new_url}";
    </script>
</body>
</html>"""
    
    redirect_dir = output_dir / old_slug
    redirect_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = redirect_dir / "index.html"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 리다이렉트 생성: {old_slug} -> {new_slug}")

def main():
    """메인 함수"""
    # public 디렉토리 (Hugo 빌드 출력 디렉토리)
    public_dir = Path("public")
    en_post_dir = public_dir / "en" / "post"
    
    print("📝 파일명 변경에 따른 리다이렉트 생성 중...\n")
    
    redirect_count = 0
    for old_filename, new_filename in FILENAME_MAPPING.items():
        old_slug = get_slug_from_filename(old_filename)
        new_slug = get_slug_from_filename(new_filename)
        
        create_redirect_html(old_slug, new_slug, en_post_dir)
        redirect_count += 1
    
    print(f"\n✨ 완료! {redirect_count}개 리다이렉트 생성됨")
    print(f"📁 리다이렉트 위치: {en_post_dir}")

if __name__ == "__main__":
    main()

