#!/usr/bin/env python3
"""
키워드 추가 도구
새로운 키워드를 CSV 파일에 추가합니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트를 경로에 추가
_project_root = Path(__file__).parent.parent
sys.path.insert(0, str(_project_root))

from keyword_manager import KeywordManager

def main():
    if len(sys.argv) < 2:
        print("사용법: python3 scripts/add_keyword.py <키워드> [카테고리] [우선순위]")
        print("\n예시:")
        print("  python3 scripts/add_keyword.py 'Python 튜토리얼' 기술 1")
        print("  python3 scripts/add_keyword.py '요리 레시피' 요리 2")
        sys.exit(1)
    
    keyword = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else "일반"
    priority = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    
    manager = KeywordManager()
    manager.add_keyword(keyword, category, priority)
    manager.print_statistics()

if __name__ == "__main__":
    main()

