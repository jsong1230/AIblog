// 기본 JavaScript

// 모바일 메뉴 토글
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenuToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // 메뉴 링크 클릭 시 모바일 메뉴 닫기
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
        
        // 외부 클릭 시 모바일 메뉴 닫기
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target);
            const isClickOnToggle = mobileMenuToggle.contains(event.target);
            
            if (!isClickInsideNav && !isClickOnToggle && navMenu.classList.contains('active')) {
                mobileMenuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
    
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

