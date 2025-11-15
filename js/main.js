// 기본 JavaScript

// 모바일 메뉴 토글
document.addEventListener('DOMContentLoaded', function() {
    // 향후 모바일 메뉴 기능 추가 가능
    console.log('AI 블로그 로드 완료');
});

// 이미지 lazy loading
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersected) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

