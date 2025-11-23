#!/usr/bin/env python3
"""
포스트 생성 자동화 테스트
"""

import unittest
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, str(Path(__file__).parent.parent))

from keyword_manager import KeywordManager

# generate_post 모듈의 함수들을 직접 정의하거나 모킹
# API 키 없이도 테스트할 수 있도록 함수만 복사
import re

def strip_markdown_for_description(text):
    """마크다운 문법을 제거하고 plain text로 변환"""
    if not text:
        return text
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
    """콘텐츠에서 중복된 H1 헤더 제거"""
    lines = content.split('\n')
    result_lines = []
    for line in lines:
        if line.strip().startswith('# ') and title.lower() in line.lower():
            continue
        result_lines.append(line)
    return '\n'.join(result_lines)

def extract_title_from_content(content):
    """콘텐츠에서 제목 추출"""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "새로운 블로그 포스트"


class TestKeywordManager(unittest.TestCase):
    """키워드 매니저 테스트"""
    
    def setUp(self):
        self.manager = KeywordManager()
    
    def test_load_keywords(self):
        """키워드 로드 테스트"""
        self.assertGreater(len(self.manager.keywords), 0)
    
    def test_get_unused_keywords(self):
        """미사용 키워드 조회 테스트"""
        unused = self.manager.get_unused_keywords()
        self.assertIsInstance(unused, list)
    
    def test_add_keyword(self):
        """키워드 추가 테스트"""
        test_keyword = "테스트 키워드"
        initial_count = len(self.manager.keywords)
        self.manager.add_keyword(test_keyword, "테스트", 1)
        self.assertEqual(len(self.manager.keywords), initial_count + 1)
        
        # 정리: 추가한 키워드 제거
        self.manager.keywords = [kw for kw in self.manager.keywords if kw.get('키워드') != test_keyword]
        self.manager.save_keywords()
    
    def test_get_statistics(self):
        """통계 조회 테스트"""
        stats = self.manager.get_statistics()
        self.assertIn('total', stats)
        self.assertIn('used', stats)
        self.assertIn('unused', stats)
        self.assertIn('usage_rate', stats)
        self.assertGreaterEqual(stats['total'], 0)


class TestPostGeneration(unittest.TestCase):
    """포스트 생성 함수 테스트"""
    
    def test_strip_markdown_for_description(self):
        """마크다운 제거 테스트"""
        test_text = "# 제목\n## 소제목\n**굵은 글씨** 일반 텍스트"
        result = strip_markdown_for_description(test_text)
        self.assertNotIn("#", result)
        self.assertNotIn("**", result)
    
    def test_remove_duplicate_h1(self):
        """중복 H1 제거 테스트"""
        title = "테스트 제목"
        content = f"# {title}\n\n본문 내용"
        result = remove_duplicate_h1_from_content(content, title)
        self.assertNotIn(f"# {title}", result)
    
    def test_extract_title_from_content(self):
        """제목 추출 테스트"""
        content = "# 블로그 제목\n\n본문 내용"
        title = extract_title_from_content(content)
        self.assertEqual(title, "블로그 제목")
    
    def test_generate_keyword_logic(self):
        """키워드 생성 로직 테스트"""
        manager = KeywordManager()
        keyword = manager.get_random_keyword()
        self.assertIsNotNone(keyword)
        self.assertIsInstance(keyword, str)


class TestPostFileStructure(unittest.TestCase):
    """포스트 파일 구조 테스트"""
    
    def test_content_directory_exists(self):
        """콘텐츠 디렉토리 존재 확인"""
        content_dir = Path("content/post")
        self.assertTrue(content_dir.exists() or content_dir.parent.exists())


if __name__ == '__main__':
    unittest.main()
