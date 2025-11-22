#!/usr/bin/env python3
"""
기존 포스트의 frontmatter에서 마크다운 제거 스크립트
"""

import re
from pathlib import Path
import frontmatter

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


def fix_post_frontmatter(filepath):
    """포스트 파일의 frontmatter에서 마크다운 제거"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        modified = False
        
        # Fix description
        if 'description' in post.metadata:
            original_desc = post.metadata['description']
            cleaned_desc = strip_markdown_for_description(original_desc)
            if cleaned_desc != original_desc:
                post.metadata['description'] = cleaned_desc
                modified = True
        
        # Fix seo.description
        if 'seo' in post.metadata and isinstance(post.metadata['seo'], dict):
            if 'description' in post.metadata['seo']:
                original_seo_desc = post.metadata['seo']['description']
                cleaned_seo_desc = strip_markdown_for_description(original_seo_desc)
                if cleaned_seo_desc != original_seo_desc:
                    post.metadata['seo']['description'] = cleaned_seo_desc
                    modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """모든 포스트 파일 처리"""
    content_dir = Path("content/post")
    
    if not content_dir.exists():
        print(f"❌ Directory not found: {content_dir}")
        return
    
    post_files = list(content_dir.glob("*.md"))
    print(f"📝 Found {len(post_files)} post files")
    
    fixed_count = 0
    for filepath in post_files:
        if fix_post_frontmatter(filepath):
            print(f"✅ Fixed: {filepath.name}")
            fixed_count += 1
        else:
            print(f"⏭️  Skipped: {filepath.name}")
    
    print(f"\n✨ Complete! Fixed {fixed_count} out of {len(post_files)} posts")


if __name__ == "__main__":
    main()
