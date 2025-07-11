// Generar estrellas dinámicamente
function createStars() {
    const starsContainer = document.querySelector('.stars');
    const numberOfStars = 200;
    
    for (let i = 0; i < numberOfStars; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 3 + 's';
        starsContainer.appendChild(star);
    }
}

// Generar partículas flotantes
function createFloatingParticles() {
    const particlesContainer = document.querySelector('.floating-particles');
    const numberOfParticles = 50;
    
    for (let i = 0; i < numberOfParticles; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 8 + 's';
        particle.style.animationDuration = (Math.random() * 4 + 6) + 's';
        particlesContainer.appendChild(particle);
    }
}

// Efecto de parallax suave
function handleParallax() {
    const scrolled = window.pageYOffset;
    const nebula = document.querySelector('.nebula-bg');
    const stars = document.querySelector('.stars');
    
    if (nebula) {
        nebula.style.transform = `translateY(${scrolled * 0.2}px)`;
    }
    
    if (stars) {
        stars.style.transform = `translateY(${scrolled * 0.1}px)`;
    }
}

// Configurar observador de intersección para animaciones de entrada
function setupIntersectionObserver() {
    const cards = document.querySelectorAll('.product-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Efectos adicionales de hover para las tarjetas
function setupCardHoverEffects() {
    const cards = document.querySelectorAll('.product-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.background = 'rgba(255, 255, 255, 0.08)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.background = 'rgba(255, 255, 255, 0.05)';
        });
    });
}

// Efecto de escritura para el nombre de la empresa
function typewriterEffect() {
    const companyName = document.querySelector('.company-name');
    const text = companyName.textContent;
    
    // Solo ejecutar si el texto es el placeholder
    if (text === '[NOMBRE EMPRESA]') {
        companyName.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                companyName.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        setTimeout(typeWriter, 1000);
    }
}

// Función para suavizar el scroll
function smoothScroll() {
    const buttons = document.querySelectorAll('.cta-button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Efecto visual de click
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1.05)';
            }, 100);
            
            // Aquí puedes agregar la lógica de navegación o contacto
            console.log('Botón clickeado:', this.textContent);
        });
    });
}

// Función para optimizar rendimiento con throttling
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Función principal de inicialización
function initializeApp() {
    // Crear elementos visuales
    createStars();
    createFloatingParticles();
    
    // Configurar efectos de scroll optimizados
    window.addEventListener('scroll', throttle(handleParallax, 16));
    
    // Configurar animaciones de entrada
    setupIntersectionObserver();
    
    // Configurar efectos de hover
    setupCardHoverEffects();
    
    // Configurar interacciones de botones
    smoothScroll();
    
    // Efecto de escritura (opcional)
    typewriterEffect();
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', initializeApp);

// Reinicializar ciertos efectos cuando se redimensiona la ventana
window.addEventListener('resize', throttle(() => {
    // Reconfigurar efectos si es necesario
    handleParallax();
}, 250));

// Preloader simple (opcional)
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});