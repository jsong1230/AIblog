#!/bin/bash

# AI 블로그 초기 설정 스크립트

echo "🚀 AI 블로그 초기 설정 시작"
echo ""

# Python 가상환경 생성 (선택사항)
read -p "Python 가상환경을 생성하시겠습니까? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Python 가상환경 생성 중..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ 가상환경 생성 완료"
fi

# Python 패키지 설치
echo ""
echo "📦 Python 패키지 설치 중..."
pip install -r requirements.txt

# 환경 변수 파일 생성
if [ ! -f .env ]; then
    echo ""
    echo "⚙️  환경 변수 파일 생성 중..."
    cp env.example .env
    echo "✅ .env 파일이 생성되었습니다. API 키를 입력해주세요."
else
    echo "ℹ️  .env 파일이 이미 존재합니다."
fi

# Hugo 설치 확인
echo ""
if ! command -v hugo &> /dev/null; then
    echo "⚠️  Hugo가 설치되어 있지 않습니다."
    echo "   macOS: brew install hugo"
    echo "   또는 https://gohugo.io/installation/ 참고"
else
    echo "✅ Hugo가 설치되어 있습니다: $(hugo version)"
fi

# Hugo 사이트 초기화 확인
if [ ! -f "config.yaml" ] || [ ! -d "content" ]; then
    echo ""
    read -p "Hugo 사이트를 초기화하시겠습니까? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📝 Hugo 사이트 초기화 중..."
        hugo new site . --force
        echo "✅ Hugo 사이트 초기화 완료"
    fi
fi

# 디렉토리 생성
echo ""
echo "📁 필요한 디렉토리 생성 중..."
mkdir -p content/post
mkdir -p static/css
mkdir -p static/js
mkdir -p layouts/_default
mkdir -p layouts/partials
mkdir -p .github/workflows

echo ""
echo "✨ 설정 완료!"
echo ""
echo "다음 단계:"
echo "1. .env 파일을 열어 API 키를 입력하세요"
echo "2. config.yaml에서 블로그 설정을 수정하세요"
echo "3. python3 generate_post.py 로 테스트 포스트를 생성해보세요"
echo "4. hugo server 로 로컬에서 미리보기를 확인하세요"

