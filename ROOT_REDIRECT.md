# 최상위 도메인 리다이렉트 설정 가이드

## 문제
- AdSense에 `jsong1230.github.io` (최상위 도메인) 등록
- 실제 블로그는 `jsong1230.github.io/AIblog`에 있음
- 최상위 도메인에 사이트가 없어서 AdSense 확인 실패

## 해결 방법

### 옵션 1: 최상위 도메인 저장소 생성 (권장)

1. GitHub에서 새 저장소 생성: `jsong1230.github.io`
2. 다음 내용의 `index.html` 파일 생성:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=https://jsong1230.github.io/AIblog/">
    <link rel="canonical" href="https://jsong1230.github.io/AIblog/">
    <!-- Google AdSense Account -->
    <meta name="google-adsense-account" content="ca-pub-5954947755126324">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5954947755126324"
     crossorigin="anonymous"></script>
</head>
<body>
    <p>Redirecting to <a href="https://jsong1230.github.io/AIblog/">AI Blog</a>...</p>
    <script>
        window.location.href = "https://jsong1230.github.io/AIblog/";
    </script>
</body>
</html>
```

3. GitHub Pages 활성화
4. AdSense 메타 태그 포함하여 크롤러가 확인 가능하도록 설정

### 옵션 2: AdSense에 전체 경로로 재등록

AdSense에서 사이트를 삭제하고 `https://jsong1230.github.io/AIblog`로 다시 등록

