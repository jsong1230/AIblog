#!/usr/bin/env python3
"""
영어 포스트 파일의 한글 카테고리/태그를 영어로 수정하는 스크립트
"""

import frontmatter
from pathlib import Path
import re

# 카테고리 한글->영어 매핑
CATEGORY_MAPPING = {
    '수익': 'Revenue',
    '기술': 'Technology',
    '금융': 'Finance',
    '커리어': 'Career',
    '교육': 'Education',
    '생산성': 'Productivity',
    '건강': 'Health',
    '여행': 'Travel',
    '비즈니스': 'Business',
    '마케팅': 'Marketing',
    '블록체인': 'Blockchain',
    '디자인': 'Design',
    'AI': 'AI',
    '일반': 'General',
    '라이프': 'Lifestyle',
    '심리': 'Psychology',
    '경제': 'Economy',
    '생활': 'Lifestyle',
    '요리': 'Cooking',
}

# 한글 패턴
KOREAN_PATTERN = re.compile(r'[가-힣]+')

def fix_english_post(file_path):
    """영어 포스트 파일의 한글 카테고리/태그를 영어로 수정"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        modified = False
        
        # 카테고리 수정
        if 'categories' in post.metadata:
            fixed_categories = []
            for cat in post.metadata['categories']:
                cat_str = str(cat)
                if KOREAN_PATTERN.search(cat_str):
                    # 한글 카테고리를 영어로 변환
                    english_cat = CATEGORY_MAPPING.get(cat_str, cat_str)
                    fixed_categories.append(english_cat)
                    modified = True
                    print(f"  Category '{cat}' -> '{english_cat}'")
                else:
                    fixed_categories.append(cat)
            post.metadata['categories'] = fixed_categories
        
        # 태그 수정
        if 'tags' in post.metadata:
            fixed_tags = []
            for tag in post.metadata['tags']:
                tag_str = str(tag)
                if KOREAN_PATTERN.search(tag_str):
                    # 한글 태그를 영어로 변환
                    if tag_str == '자동화':
                        fixed_tags.append('Automation')
                    else:
                        # 다른 한글 태그는 그대로 유지하거나 매핑 필요
                        fixed_tags.append(tag_str)
                    modified = True
                    print(f"  Tag '{tag}' -> '{fixed_tags[-1]}'")
                else:
                    fixed_tags.append(tag)
            post.metadata['tags'] = fixed_tags
        
        if modified:
            # 파일 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            return True
        
        return False
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """메인 함수"""
    post_dir = Path("content/post")
    english_posts = list(post_dir.glob("*.en.md"))
    
    print(f"🔍 영어 포스트 파일 검사 중... ({len(english_posts)}개)")
    print()
    
    fixed_count = 0
    for file_path in english_posts:
        print(f"📄 {file_path.name}")
        if fix_english_post(file_path):
            print(f"  ✅ 수정 완료")
            fixed_count += 1
        else:
            print(f"  ⏭️  수정 불필요")
        print()
    
    print(f"✨ 완료! {fixed_count}개 파일 수정됨")

if __name__ == "__main__":
    main()
