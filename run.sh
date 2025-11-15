#!/bin/bash

# AI 블로그 자동 생성 및 배포 스크립트

echo "🚀 AI 블로그 자동 생성 시스템 시작"
echo ""

# 가상환경 활성화 (선택사항)
# source venv/bin/activate

# 포스트 생성
echo "📝 포스트 생성 중..."
python3 generate_post.py

# Git에 커밋 및 푸시
echo ""
echo "📦 Git에 커밋 및 푸시 중..."
python3 deploy.py

echo ""
echo "✅ 완료!"

