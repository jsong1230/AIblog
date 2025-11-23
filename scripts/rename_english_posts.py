#!/usr/bin/env python3
"""
영어 포스트 파일명의 한글을 영어로 변경하는 스크립트
"""
import frontmatter
from pathlib import Path
import re
import sys
import os
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

from generate_post import translate_content

KOREAN_PATTERN = re.compile(r'[가-힣]+')

def slugify(text):
    """텍스트를 URL-friendly slug로 변환"""
    # 소문자로 변환
    text = text.lower()
    # 특수문자 제거 및 공백을 하이픈으로
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    # 앞뒤 하이픈 제거
    text = text.strip('-')
    return text

def translate_korean_to_english(text):
    """한글 텍스트를 영어로 번역"""
    if not KOREAN_PATTERN.search(text):
        return text
    
    translated = translate_content(text)
    if translated:
        # 마크다운 제거 및 정리
        translated = translated.replace('#', '').strip()
        # 첫 줄만 사용 (제목이 여러 줄일 수 있음)
        translated = translated.split('\n')[0].strip()
        return translated
    return text

def rename_english_post(file_path):
    """영어 포스트 파일명을 영어로 변경"""
    if not file_path.exists():
        print(f"❌ 파일 없음: {file_path}")
        return False
    
    filename = file_path.name
    
    # 한글이 없으면 스킵
    if not KOREAN_PATTERN.search(filename):
        return False
    
    print(f"\n📄 {filename}")
    
    # 파일 내용 읽기
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
    except Exception as e:
        print(f"  ❌ 파일 읽기 실패: {e}")
        return False
    
    # 제목 가져오기
    title = post.metadata.get('title', '')
    if not title:
        print(f"  ⚠️  제목 없음, 파일명 기반으로 번역 시도")
        # 파일명에서 한글 부분 추출
        korean_part = '-'.join([part for part in filename.split('-') if KOREAN_PATTERN.search(part)])
        if korean_part:
            title = korean_part.replace('.en.md', '')
        else:
            print(f"  ❌ 파일명에서 한글 추출 실패")
            return False
    
    # 제목을 영어로 번역
    print(f"  📝 제목: '{title}'")
    english_title = translate_korean_to_english(title)
    print(f"  ✅ 영어 제목: '{english_title}'")
    
    # 파일명 형식: YYYY-MM-DD-slug-timestamp.en.md
    # 기존 파일명에서 날짜와 타임스탬프 추출
    parts = filename.replace('.en.md', '').split('-')
    date_part = '-'.join(parts[:3])  # YYYY-MM-DD
    timestamp = parts[-1]  # 마지막 부분이 타임스탬프
    
    # 영어 제목을 slug로 변환
    slug = slugify(english_title)
    # slug가 너무 길면 제한 (파일명 길이 제한 고려)
    if len(slug) > 80:
        slug = slug[:80]
    
    # 새 파일명 생성
    new_filename = f"{date_part}-{slug}-{timestamp}.en.md"
    new_file_path = file_path.parent / new_filename
    
    # 같은 파일명이 이미 있으면 스킵
    if new_file_path.exists() and new_file_path != file_path:
        print(f"  ⚠️  이미 존재하는 파일명: {new_filename}")
        return False
    
    print(f"  📝 새 파일명: {new_filename}")
    
    # 파일명 변경 (git mv 사용)
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'mv', str(file_path), str(new_file_path)],
            capture_output=True,
            text=True,
            cwd=file_path.parent.parent.parent
        )
        if result.returncode == 0:
            print(f"  ✅ 파일명 변경 완료")
            return True
        else:
            print(f"  ❌ git mv 실패: {result.stderr}")
            # 일반 파일 시스템 이동 시도
            file_path.rename(new_file_path)
            print(f"  ✅ 파일명 변경 완료 (일반 이동)")
            return True
    except Exception as e:
        print(f"  ❌ 파일명 변경 실패: {e}")
        return False

def main():
    """메인 함수"""
    post_dir = Path("content/post")
    
    if not post_dir.exists():
        print(f"❌ 디렉토리 없음: {post_dir}")
        sys.exit(1)
    
    # 모든 .en.md 파일 찾기
    en_files = list(post_dir.glob("*.en.md"))
    korean_filename_files = [f for f in en_files if KOREAN_PATTERN.search(f.name)]
    
    print(f"📚 총 {len(en_files)}개의 영어 포스트 파일")
    print(f"📝 한글 파일명을 가진 파일: {len(korean_filename_files)}개\n")
    
    if not korean_filename_files:
        print("✅ 변경할 파일이 없습니다.")
        return
    
    renamed_count = 0
    for file_path in korean_filename_files:
        if rename_english_post(file_path):
            renamed_count += 1
    
    print(f"\n✨ 완료! {renamed_count}개 파일명 변경됨")

if __name__ == "__main__":
    main()
