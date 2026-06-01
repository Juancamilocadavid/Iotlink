// Smooth scrolling para enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Animación de entrada para elementos cuando se desplazan al viewport
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Aplicar animación a tarjetas
document.querySelectorAll('.solucion-card, .caso-card, .soporte-card, .mv-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// Contador animado para estadísticas hero
const animateHeroStats = () => {
    const stats = document.querySelectorAll('.stat-number, .card-number');
    if (stats.length === 0) return;
    
    const observerStats = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                stats.forEach(stat => {
                    const originalText = stat.textContent;
                    const parsed = originalText.match(/^(\d+)(.*)$/);

                    if (parsed) {
                        const numericValue = parseInt(parsed[1], 10);
                        const suffix = parsed[2]; // conserva "%", "+", etc.
                        let currentValue = 0;
                        const duration = 2000;
                        const startTime = Date.now();

                        const counter = setInterval(() => {
                            const elapsed = Date.now() - startTime;
                            const progress = Math.min(elapsed / duration, 1);
                            currentValue = Math.floor(numericValue * progress);

                            stat.textContent = currentValue + suffix;

                            if (progress === 1) {
                                clearInterval(counter);
                                stat.textContent = originalText;
                            }
                        }, 16);
                    }
                });
                
                observerStats.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        observerStats.observe(heroSection);
    }
};



// Paralax en hero
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroBg = document.querySelector('.hero-bg-full');
    
    if (heroBg && scrolled < 1000) {
        heroBg.style.backgroundPositionY = `${scrolled * 0.5}px`;
    }
});

// Inicialización
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
    animateHeroStats();
});

// Detección de tema
if (navigator.onLine) {
    console.log('IoT Link - Conectado');
} else {
    console.log('Sin conexión a Internet');
}