#!/usr/bin/env python3
"""
자동 발행 스크립트
키워드 → 글 생성 → 빌드 → 배포의 전체 자동화 루프
"""

import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv
from generate_post import generate_post
from keyword_manager import KeywordManager

load_dotenv()

POSTS_PER_RUN = int(os.getenv("POSTS_PER_DAY", "10"))
AUTO_BUILD = os.getenv("AUTO_BUILD", "true").lower() == "true"
AUTO_DEPLOY = os.getenv("AUTO_DEPLOY", "true").lower() == "true"


def build_hugo_site():
    """Hugo 사이트 빌드"""
    print("\n🔨 Hugo 사이트 빌드 중...")
    try:
        result = subprocess.run(
            ["hugo", "--minify"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ 빌드 완료!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 빌드 실패: {e}")
        print(f"에러 출력: {e.stderr}")
        return False
    except FileNotFoundError:
        print("⚠️  Hugo가 설치되어 있지 않습니다. 빌드를 건너뜁니다.")
        return False


def deploy_to_git():
    """Git에 커밋 및 푸시"""
    print("\n📦 Git에 커밋 및 푸시 중...")
    try:
        # 변경사항 확인
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        
        if not result.stdout.strip():
            print("📝 변경사항이 없습니다.")
            return True
        
        # 추가
        subprocess.run(["git", "add", "."], check=True)
        
        # 커밋
        from datetime import datetime
        commit_message = f"Auto: 새 포스트 생성 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True
        )
        
        # 푸시
        subprocess.run(["git", "push"], check=True)
        
        print("✅ 배포 완료!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 오류: {e}")
        return False
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False


def main():
    """메인 자동화 루프"""
    print("=" * 60)
    print("🚀 AI 블로그 자동 발행 시스템 시작")
    print("=" * 60)
    
    keyword_manager = KeywordManager()
    keyword_manager.print_statistics()
    
    success_count = 0
    fail_count = 0
    
    # 포스트 생성
    print(f"\n📝 {POSTS_PER_RUN}개의 포스트 생성 시작...\n")
    
    for i in range(POSTS_PER_RUN):
        print(f"\n[{i+1}/{POSTS_PER_RUN}] 포스트 생성 중...")
        print("-" * 60)
        
        try:
            result = generate_post()
            if result:
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            fail_count += 1
        
        # API 레이트 리밋을 고려한 대기
        if i < POSTS_PER_RUN - 1:
            print("\n⏳ 다음 포스트 생성을 위해 30초 대기...")
            import time
            time.sleep(30)
    
    # 결과 요약
    print("\n" + "=" * 60)
    print(f"📊 생성 결과: 성공 {success_count}개, 실패 {fail_count}개")
    print("=" * 60)
    
    keyword_manager.print_statistics()
    
    # 빌드
    if AUTO_BUILD and success_count > 0:
        build_hugo_site()
    
    # 배포
    if AUTO_DEPLOY and success_count > 0:
        deploy_to_git()
    
    print("\n✨ 자동 발행 프로세스 완료!")
    return success_count > 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

