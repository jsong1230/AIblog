#!/usr/bin/env python3
"""
영어 포스트 파일의 한글 본문을 영어로 번역하는 스크립트
"""

import os
import sys
import frontmatter
from pathlib import Path
import re
from dotenv import load_dotenv
from openai import OpenAI

# 상위 디렉토리를 경로에 추가하여 generate_post 모듈 사용
_script_dir = Path(__file__).parent
_project_root = _script_dir.parent
sys.path.insert(0, str(_project_root))

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 확인
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("⚠️  OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
    print("   이 스크립트는 GitHub Actions에서 자동으로 실행되거나,")
    print("   로컬에서 실행 시 OPENAI_API_KEY 환경 변수를 설정해야 합니다.")
    sys.exit(1)

# generate_post.py의 번역 함수 재사용
from generate_post import translate_content

# 한글 패턴
KOREAN_PATTERN = re.compile(r'[가-힣]+')

def translate_english_post(file_path):
    """영어 포스트 파일의 한글 본문을 영어로 번역"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # 본문에서 한글 확인
        content = post.content
        korean_matches = KOREAN_PATTERN.findall(content)
        
        if len(korean_matches) < 50:  # 한글이 50자 미만이면 번역 불필요
            return False
        
        print(f"  📝 한글 본문 발견 ({len(''.join(korean_matches))}자), 번역 중...")
        
        # 제목도 한글이면 번역
        title = post.metadata.get('title', '')
        if KOREAN_PATTERN.search(title):
            print(f"  📝 제목 번역 중: '{title}'")
            title_translated = translate_content(title)
            if title_translated:
                # 제목에서 마크다운 제거
                title_translated = title_translated.replace('#', '').strip()
                post.metadata['title'] = title_translated
                print(f"  ✅ 제목 번역 완료: '{title_translated}'")
        
        # 본문 번역
        translated_content = translate_content(content)
        
        if translated_content:
            post.content = translated_content
            
            # description도 한글이면 번역
            description = post.metadata.get('description', '')
            if description and KOREAN_PATTERN.search(description):
                print(f"  📝 Description 번역 중...")
                desc_translated = translate_content(description)
                if desc_translated:
                    # 마크다운 제거
                    desc_translated = desc_translated.replace('#', '').strip()
                    post.metadata['description'] = desc_translated[:200] + "..."
            
            # SEO description도 번역
            if 'seo' in post.metadata and 'description' in post.metadata['seo']:
                seo_desc = post.metadata['seo']['description']
                if KOREAN_PATTERN.search(seo_desc):
                    print(f"  📝 SEO description 번역 중...")
                    seo_desc_translated = translate_content(seo_desc)
                    if seo_desc_translated:
                        seo_desc_translated = seo_desc_translated.replace('#', '').strip()
                        post.metadata['seo']['description'] = seo_desc_translated[:160]
            
            # 파일 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            
            return True
        else:
            print(f"  ❌ 번역 실패")
            return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """메인 함수"""
    post_dir = Path("content/post")
    
    # 오늘 생성된 영어 포스트 찾기
    english_posts = []
    for file in sorted(post_dir.glob("2025-11-23-*.en.md"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            content = post.content
            korean_matches = KOREAN_PATTERN.findall(content)
            
            if len(korean_matches) >= 50:  # 한글이 50자 이상이면 번역 필요
                english_posts.append(file)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    if not english_posts:
        print("✅ 번역이 필요한 영어 포스트 없음")
        return
    
    print(f"🔍 한글 본문이 있는 영어 포스트 발견: {len(english_posts)}개\n")
    
    translated_count = 0
    for file_path in english_posts:
        print(f"📄 {file_path.name}")
        if translate_english_post(file_path):
            print(f"  ✅ 번역 완료\n")
            translated_count += 1
        else:
            print(f"  ⏭️  번역 불필요 또는 실패\n")
    
    print(f"✨ 완료! {translated_count}개 파일 번역됨")

if __name__ == "__main__":
    main()
