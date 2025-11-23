#!/bin/bash
# 대소문자 구분 없는 URL 리다이렉트 생성 스크립트

PUBLIC_DIR="public"
REDIRECT_DIR="${PUBLIC_DIR}/aiblog"

# public 디렉토리가 존재하는지 확인
if [ ! -d "$PUBLIC_DIR" ]; then
    echo "Error: $PUBLIC_DIR directory not found. Run 'hugo' first."
    exit 1
fi

# 리다이렉트 디렉토리 생성
mkdir -p "$REDIRECT_DIR"

# 리다이렉트 HTML 파일 생성
cat > "${REDIRECT_DIR}/index.html" << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=https://jsong1230.github.io/AIblog/">
    <link rel="canonical" href="https://jsong1230.github.io/AIblog/">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="https://jsong1230.github.io/AIblog/">AI Blog</a>...</p>
    <script>
        window.location.href = "https://jsong1230.github.io/AIblog/";
    </script>
</body>
</html>
EOF

echo "✅ Case-insensitive redirect created at ${REDIRECT_DIR}/index.html"
