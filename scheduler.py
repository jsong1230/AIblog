#!/usr/bin/env python3
"""
블로그 포스트 자동 발행 스케줄러
하루에 지정된 개수만큼 포스트를 자동으로 생성합니다.
"""

import os
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from generate_post import generate_post

load_dotenv()

POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "3"))


def generate_posts_batch():
    """하루치 포스트를 배치로 생성"""
    print(f"\n{'='*50}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 포스트 배치 생성 시작")
    print(f"{'='*50}\n")
    
    success_count = 0
    fail_count = 0
    
    for i in range(POSTS_PER_DAY):
        print(f"\n[{i+1}/{POSTS_PER_DAY}] 포스트 생성 중...")
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
        if i < POSTS_PER_DAY - 1:
            print("⏳ 다음 포스트 생성을 위해 30초 대기...")
            time.sleep(30)
    
    print(f"\n{'='*50}")
    print(f"✅ 배치 생성 완료: 성공 {success_count}개, 실패 {fail_count}개")
    print(f"{'='*50}\n")


def run_scheduler():
    """스케줄러 실행"""
    print("🕐 블로그 포스트 자동 발행 스케줄러 시작")
    print(f"📊 설정: 하루 {POSTS_PER_DAY}개 포스트 자동 생성")
    print("⏰ 매일 자정에 포스트 생성 시작\n")
    
    # 매일 자정에 실행
    schedule.every().day.at("00:00").do(generate_posts_batch)
    
    # 또는 매일 특정 시간에 실행 (예: 오전 9시)
    # schedule.every().day.at("09:00").do(generate_posts_batch)
    
    # 테스트용: 1분마다 실행 (개발 시에만 사용)
    # schedule.every(1).minutes.do(generate_posts_batch)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1분마다 스케줄 확인


if __name__ == "__main__":
    # 즉시 한 번 실행 (테스트용)
    # generate_posts_batch()
    
    # 스케줄러 실행
    run_scheduler()

