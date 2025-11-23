#!/usr/bin/env python3
"""
AI 블로그 포스트 자동 생성 스크립트
ChatGPT API를 사용하여 블로그 포스트를 생성하고 Unsplash에서 이미지를 가져옵니다.
"""

import os
import json
import requests
import frontmatter
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import yaml
from keyword_manager import KeywordManager

# 환경 변수 로드
load_dotenv()

# 설정
CONTENT_DIR = Path("content/post")
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
BLOG_TITLE = os.getenv("BLOG_TITLE", "AI 자동 블로그")
BLOG_DESCRIPTION = os.getenv("BLOG_DESCRIPTION", "AI가 자동으로 생성하는 블로그")
CONTENT_LANGUAGE = os.getenv("CONTENT_LANGUAGE", "ko")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=OPENAI_API_KEY)

# 키워드 매니저 초기화
keyword_manager = KeywordManager()


def generate_keyword():
    """키워드 매니저에서 키워드 가져오기"""
    keyword = keyword_manager.get_random_keyword()
    if not keyword:
        # 폴백: 기본 키워드 리스트
        fallback_keywords = [
            "AI 블로그 자동화",
            "ChatGPT 활용법",
            "웹 개발 팁",
            "프로그래밍 초보자 가이드",
            "최신 기술 트렌드",
        ]
        import random
        return random.choice(fallback_keywords)
    return keyword


def generate_post_content(keyword, lang='ko'):
    """ChatGPT API를 사용하여 블로그 포스트 생성"""
    if lang == 'en':
        system_prompt = f"""You are a professional blog writer. Write high-quality, SEO-optimized blog posts.

Requirements:
1. Title should be SEO-friendly and attractive
2. At least 1500 characters of detailed content
3. Use subheadings (H2, H3) appropriately
4. Provide valuable information to readers
5. Natural keyword placement
6. Write in markdown format
7. Write in English

Keyword: {keyword}
"""
        user_prompt = f"Write an SEO-optimized blog post about '{keyword}'. Include title, body, and conclusion. Write a complete, high-quality article."
    else:
        system_prompt = f"""당신은 전문 블로그 작가입니다. SEO에 최적화된 고품질 블로그 포스트를 작성해주세요.

요구사항:
1. 제목은 SEO 친화적이고 매력적이어야 합니다
2. 최소 1500자 이상의 상세한 내용
3. 소제목(H2, H3)을 적절히 사용
4. 독자에게 가치 있는 정보 제공
5. 자연스러운 키워드 배치
6. 마크다운 형식으로 작성
7. 한국어로 작성

키워드: {keyword}
"""
        user_prompt = f"'{keyword}'에 대한 SEO 최적화된 블로그 포스트를 작성해주세요. 제목, 본문, 결론을 포함하여 완성도 높은 고품질 글을 작성해주세요."
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000,
        )
        
        content = response.choices[0].message.content
        return content
    except Exception as e:
        print(f"OpenAI API 오류: {e}")
        return None


def translate_content(content, target_language="English"):
    """콘텐츠를 영어로 번역"""
    system_prompt = f"You are a professional translator. Translate the following markdown blog post to {target_language}. Maintain the original markdown formatting, links, and structure. Do not translate code blocks."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content}
            ],
            temperature=0.3,
            max_tokens=2000,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Translation Error: {e}")
        return None


def get_unsplash_image(keyword):
    """Unsplash API에서 키워드 관련 이미지 가져오기"""
    if not UNSPLASH_ACCESS_KEY:
        return None
    
    try:
        url = "https://api.unsplash.com/search/photos"
        headers = {
            "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
        }
        params = {
            "query": keyword,
            "per_page": 1,
            "orientation": "landscape"
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if data.get("results"):
            photo = data["results"][0]
            return {
                "url": photo["urls"]["regular"],
                "thumb": photo["urls"]["thumb"],
                "author": photo["user"]["name"],
                "author_url": photo["user"]["links"]["html"],
                "description": photo.get("description", keyword)
            }
    except Exception as e:
        print(f"Unsplash API 오류: {e}")
    
    return None


def extract_title_from_content(content):
    """콘텐츠에서 제목 추출"""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "새로운 블로그 포스트"


def strip_markdown_for_description(text):
    """마크다운 문법을 제거하고 plain text로 변환"""
    import re
    # Remove markdown headers (# ## ###)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove markdown links [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove markdown bold/italic **text** or *text* -> text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Remove code blocks ```
    text = re.sub(r'```[^`]*```', '', text, flags=re.DOTALL)
    # Remove inline code `code`
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Clean up multiple spaces and newlines
    text = ' '.join(text.split())
    return text.strip()


def remove_duplicate_h1_from_content(content, title):
    """콘텐츠에서 중복된 H1 헤더 제거 (제목과 동일한 경우)"""
    lines = content.split('\n')
    result_lines = []
    skip_next_empty = False
    
    for line in lines:
        # If line is H1 header matching the title, skip it
        if line.startswith('# ') and line[2:].strip() == title:
            skip_next_empty = True
            continue
        # Skip one empty line after removed H1
        if skip_next_empty and line.strip() == '':
            skip_next_empty = False
            continue
        skip_next_empty = False
        result_lines.append(line)
    
    return '\n'.join(result_lines)


def create_post_file(keyword, content, image_info=None, lang='ko', original_filename=None):
    """Hugo 포스트 파일 생성"""
    title = extract_title_from_content(content)
    
    if lang == 'ko':
        slug = keyword.lower().replace(' ', '-').replace('_', '-')
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}-{timestamp}.md"
    else:
        # English version uses the same filename base but with .en.md extension
        if original_filename:
            base_name = original_filename.replace('.md', '')
            filename = f"{base_name}.en.md"
        else:
            # Fallback if original filename is not provided (shouldn't happen in this flow)
            slug = keyword.lower().replace(' ', '-').replace('_', '-')
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}-{timestamp}.en.md"

    filepath = CONTENT_DIR / filename
    
    # 이미지 URL 설정
    image_url = image_info["url"] if image_info else ""
    image_thumb = image_info["thumb"] if image_info else ""
    
    # 키워드에서 카테고리 가져오기
    keyword_data = None
    for kw in keyword_manager.keywords:
        if kw.get('키워드') == keyword:
            keyword_data = kw
            break
    
    # 카테고리 한글->영어 매핑
    category_mapping = {
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
    
    if keyword_data:
        category_ko = keyword_data.get('카테고리', '일반')
        if lang == 'en':
            categories = [category_mapping.get(category_ko, category_ko)]
        else:
            categories = [category_ko]
    else:
        if lang == 'en':
            categories = ["AI", "Automation"]
        else:
            categories = ["AI", "자동화"]
    
    # Remove duplicate H1 header from content
    content_cleaned = remove_duplicate_h1_from_content(content, title)
    
    # Create plain text description without markdown
    plain_description = strip_markdown_for_description(content_cleaned)
    
    # Front matter 생성
    post = frontmatter.Post(content_cleaned)
    
    # 태그 설정 (언어에 따라)
    if lang == 'en':
        tags = [keyword, "AI", "Automation"]
    else:
        tags = [keyword, "AI", "자동화"]
    
    post.metadata = {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00"),
        "draft": False,
        "categories": categories,
        "tags": tags,
        "image": image_url,
        "thumbnail": image_thumb,
        "description": plain_description[:200] + "...",
        "author": "AI Blogger",
        "seo": {
            "keywords": keyword,
            "description": plain_description[:160]
        }
    }
    
    # 이미지 정보가 있으면 크레딧 추가
    if image_info:
        credit_text = f"\n\n*이미지 출처: [Unsplash - {image_info['author']}]({image_info['author_url']})*\n\n" if lang == 'ko' else f"\n\n*Image Credit: [Unsplash - {image_info['author']}]({image_info['author_url']})*\n\n"
        post.content = f"![{image_info['description']}]({image_url})" + credit_text + post.content
    
    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"✅ 포스트 생성 완료 ({lang}): {filepath}")
    return filename


def generate_post():
    """포스트 생성 메인 함수 - 한글과 영어 모두 생성"""
    print("🚀 블로그 포스트 생성 시작...")
    
    # 키워드 생성
    keyword = generate_keyword()
    print(f"📝 키워드: {keyword}")
    
    # 이미지 가져오기 (양쪽 언어에서 공통 사용)
    print("🖼️  Unsplash에서 이미지 가져오는 중...")
    image_info = get_unsplash_image(keyword)
    
    # 한국어 콘텐츠 생성
    print("🤖 ChatGPT로 콘텐츠 생성 중 (한국어)...")
    content_ko = generate_post_content(keyword, lang='ko')
    
    if not content_ko:
        print("❌ 한국어 콘텐츠 생성 실패")
        return None
    
    # 한국어 포스트 파일 생성
    print("📄 한국어 포스트 파일 생성 중...")
    filename_ko = create_post_file(keyword, content_ko, image_info, lang='ko')
    
    # 영어 콘텐츠 생성 (번역이 아닌 직접 생성)
    print("🇺🇸 ChatGPT로 콘텐츠 생성 중 (영어)...")
    content_en = generate_post_content(keyword, lang='en')
    
    if content_en:
        print("📄 영어 포스트 파일 생성 중...")
        create_post_file(keyword, content_en, image_info, lang='en', original_filename=filename_ko)
        print("✅ 영어 포스트 생성 완료!")
    else:
        print("⚠️ 영어 콘텐츠 생성 실패, 번역으로 대체 시도...")
        # 번역으로 대체 시도
        content_en = translate_content(content_ko)
        if content_en:
            print("📄 영어 포스트 파일 생성 중 (번역본)...")
            create_post_file(keyword, content_en, image_info, lang='en', original_filename=filename_ko)
            print("✅ 영어 포스트 생성 완료 (번역본)!")
        else:
            print("❌ 영어 포스트 생성 실패")

    # 키워드를 사용됨으로 표시
    keyword_manager.mark_keyword_as_used(keyword)
    
    print(f"✨ 완료! 한글과 영어 포스트가 모두 생성되었습니다.")
    return filename_ko


if __name__ == "__main__":
    generate_post()

