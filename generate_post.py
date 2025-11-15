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


def generate_post_content(keyword):
    """ChatGPT API를 사용하여 블로그 포스트 생성"""
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

    user_prompt = f"'{keyword}'에 대한 SEO 최적화된 블로그 포스트를 작성해주세요. 제목, 본문, 결론을 포함하여 완성도 높은 글을 작성해주세요."

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


def create_post_file(keyword, content, image_info=None):
    """Hugo 포스트 파일 생성"""
    title = extract_title_from_content(content)
    slug = keyword.lower().replace(' ', '-').replace('_', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    
    # 중복 방지를 위해 타임스탬프 추가
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{datetime.now().strftime('%Y-%m-%d')}-{slug}-{timestamp}.md"
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
    
    categories = [keyword_data.get('카테고리', '일반')] if keyword_data else ["AI", "자동화"]
    
    # Front matter 생성
    post = frontmatter.Post(content)
    post.metadata = {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00"),
        "draft": False,
        "categories": categories,
        "tags": [keyword, "AI", "자동화"],
        "image": image_url,
        "thumbnail": image_thumb,
        "description": content[:200].replace('\n', ' ') + "...",
        "author": "AI Blogger",
        "seo": {
            "keywords": keyword,
            "description": content[:160].replace('\n', ' ')
        }
    }
    
    # 이미지 정보가 있으면 크레딧 추가
    if image_info:
        post.content = f"![{image_info['description']}]({image_url})\n\n*이미지 출처: [Unsplash - {image_info['author']}]({image_info['author_url']})*\n\n" + post.content
    
    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"✅ 포스트 생성 완료: {filepath}")
    return filepath


def generate_post():
    """포스트 생성 메인 함수"""
    print("🚀 블로그 포스트 생성 시작...")
    
    # 키워드 생성
    keyword = generate_keyword()
    print(f"📝 키워드: {keyword}")
    
    # 콘텐츠 생성
    print("🤖 ChatGPT로 콘텐츠 생성 중...")
    content = generate_post_content(keyword)
    
    if not content:
        print("❌ 콘텐츠 생성 실패")
        return None
    
    # 이미지 가져오기
    print("🖼️  Unsplash에서 이미지 가져오는 중...")
    image_info = get_unsplash_image(keyword)
    
    # 포스트 파일 생성
    print("📄 포스트 파일 생성 중...")
    filepath = create_post_file(keyword, content, image_info)
    
    # 키워드를 사용됨으로 표시
    keyword_manager.mark_keyword_as_used(keyword)
    
    print(f"✨ 완료! 포스트가 생성되었습니다: {filepath}")
    return filepath


if __name__ == "__main__":
    generate_post()

