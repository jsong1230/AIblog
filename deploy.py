#!/usr/bin/env python3
"""
GitHub에 자동 커밋 및 푸시하는 스크립트
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GITHUB_REPO = os.getenv("GITHUB_REPO", "")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")


def git_add_commit_push():
    """변경사항을 Git에 추가하고 커밋한 후 푸시"""
    try:
        # Git 상태 확인
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        
        if not result.stdout.strip():
            print("📝 변경사항이 없습니다.")
            return
        
        print("📦 변경사항을 Git에 추가 중...")
        subprocess.run(["git", "add", "."], check=True)
        
        commit_message = f"Auto: 새 포스트 생성 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        print(f"💾 커밋 중: {commit_message}")
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True
        )
        
        print("🚀 GitHub에 푸시 중...")
        subprocess.run(["git", "push"], check=True)
        
        print("✅ 배포 완료!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 오류: {e}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")


if __name__ == "__main__":
    git_add_commit_push()

