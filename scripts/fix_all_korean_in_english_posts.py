#!/usr/bin/env python3
"""
영어 포스트 파일의 모든 한글을 영어로 번역하는 스크립트
제목, 본문, description, SEO description, 태그, SEO keywords 모두 처리
"""
import os
import sys
import frontmatter
from pathlib import Path
import re
from dotenv import load_dotenv

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
    sys.exit(1)

# generate_post.py의 번역 함수 재사용
from generate_post import translate_content

# 한글 패턴
KOREAN_PATTERN = re.compile(r'[가-힣]+')

def translate_text(text):
    """텍스트를 영어로 번역"""
    if not text or not KOREAN_PATTERN.search(text):
        return text
    
    translated = translate_content(text)
    if translated:
        # 마크다운 제거 및 정리
        translated = translated.replace('#', '').strip()
        # 첫 줄만 사용 (제목이 여러 줄일 수 있음)
        translated = translated.split('\n')[0].strip()
        return translated
    return text

def translate_english_post(file_path):
    """영어 포스트 파일의 모든 한글을 영어로 번역"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        modified = False
        
        # 1. 제목 번역
        title = post.metadata.get('title', '')
        if KOREAN_PATTERN.search(title):
            print(f"  📝 제목 번역 중: '{title}'")
            title_translated = translate_text(title)
            if title_translated:
                post.metadata['title'] = title_translated
                print(f"  ✅ 제목 번역 완료: '{title_translated}'")
                modified = True
        
        # 2. 본문 번역
        content = post.content
        korean_matches = KOREAN_PATTERN.findall(content)
        if len(korean_matches) > 10:  # 한글이 10자 이상이면 번역
            print(f"  📝 본문 번역 중 ({len(''.join(korean_matches))}자 한글)...")
            content_translated = translate_content(content)
            if content_translated:
                post.content = content_translated
                print(f"  ✅ 본문 번역 완료")
                modified = True
        
        # 3. Description 번역
        description = post.metadata.get('description', '')
        if description and KOREAN_PATTERN.search(description):
            print(f"  📝 Description 번역 중...")
            desc_translated = translate_text(description)
            if desc_translated:
                post.metadata['description'] = desc_translated[:200] + "..."
                print(f"  ✅ Description 번역 완료")
                modified = True
        
        # 4. SEO description 번역
        if 'seo' in post.metadata and 'description' in post.metadata['seo']:
            seo_desc = post.metadata['seo']['description']
            if KOREAN_PATTERN.search(seo_desc):
                print(f"  📝 SEO description 번역 중...")
                seo_desc_translated = translate_text(seo_desc)
                if seo_desc_translated:
                    post.metadata['seo']['description'] = seo_desc_translated[:160]
                    print(f"  ✅ SEO description 번역 완료")
                    modified = True
        
        # 5. 태그 번역
        tags = post.metadata.get('tags', [])
        if tags:
            fixed_tags = []
            tags_modified = False
            for tag in tags:
                tag_str = str(tag)
                if KOREAN_PATTERN.search(tag_str):
                    print(f"  📝 태그 번역 중: '{tag_str}'")
                    tag_translated = translate_text(tag_str)
                    if tag_translated:
                        fixed_tags.append(tag_translated)
                        print(f"  ✅ 태그 번역 완료: '{tag_translated}'")
                        tags_modified = True
                    else:
                        fixed_tags.append(tag_str)
                else:
                    fixed_tags.append(tag)
            
            if tags_modified:
                post.metadata['tags'] = fixed_tags
                modified = True
        
        # 6. SEO keywords 번역
        if 'seo' in post.metadata and 'keywords' in post.metadata['seo']:
            keywords = post.metadata['seo']['keywords']
            if KOREAN_PATTERN.search(keywords):
                print(f"  📝 SEO keywords 번역 중: '{keywords}'")
                keywords_translated = translate_text(keywords)
                if keywords_translated:
                    post.metadata['seo']['keywords'] = keywords_translated
                    print(f"  ✅ SEO keywords 번역 완료: '{keywords_translated}'")
                    modified = True
        
        # 파일 저장
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            return True
        else:
            return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """메인 함수"""
    post_dir = Path("content/post")
    
    # 모든 영어 포스트 찾기
    en_files = list(post_dir.glob("*.en.md"))
    
    print(f"📚 총 {len(en_files)}개의 영어 포스트 파일 발견\n")
    
    translated_count = 0
    for file_path in sorted(en_files):
        print(f"📄 {file_path.name}")
        if translate_english_post(file_path):
            print(f"  ✅ 번역 완료\n")
            translated_count += 1
        else:
            print(f"  ⏭️  번역 불필요 (한글 없음)\n")
    
    print(f"✨ 완료! {translated_count}개 파일 번역됨")

if __name__ == "__main__":
    main()
