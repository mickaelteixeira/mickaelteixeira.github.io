/**
 * Modern Portfolio Scripts
 * Handles scroll animations, form submission, and interactions.
 */

/**
 * Initialize Deep Space Background
 * Progressive starfield that gets denser towards the bottom
 */
function initSpaceBackground() {
    const canvas = document.getElementById('space-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width, height;
    let stars = [];
    const baseStarCount = 400; // Base number of stars

    // Resize handling
    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
        initStars();
    }

    // Star object
    class Star {
        constructor() {
            this.reset();
            // Initial random y pos to fill screen
            this.y = Math.random() * height;
        }

        reset() {
            this.x = Math.random() * width;
            this.y = -10; // Start just above screen
            this.z = Math.random() * 2 + 0.5; // Depth/Speed
            this.size = Math.random() * 1.5;
            this.opacity = Math.random() * 0.5 + 0.1;
            this.twinkleSpeed = Math.random() * 0.05;
            this.twinkleDir = 1;
        }

        update() {
            this.y += this.z * 0.2; // Slow drift downwards

            // Twinkle effect
            this.opacity += this.twinkleSpeed * this.twinkleDir;
            if (this.opacity > 0.8 || this.opacity < 0.1) {
                this.twinkleDir *= -1;
            }

            // Reset if out of bounds
            if (this.y > height) {
                this.reset();
            }
        }

        draw() {
            // Calculate density based on scroll position + screen position
            // We want more stars visible when user scrolls down
            const scrollPct = window.scrollY / (document.body.scrollHeight - window.innerHeight);

            // Global opacity based on scroll: 0 at top, 1 at bottom
            // But we want some stars always visible, just MORE at bottom
            const visibilityThreshold = 1 - (scrollPct * 0.8 + 0.2);

            // Simple draw
            ctx.beginPath();
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function initStars() {
        stars = [];
        for (let i = 0; i < baseStarCount; i++) {
            stars.push(new Star());
        }
        canvas.style.opacity = 1;
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        // Draw stars
        // We want the "density" effect to be visual. 
        // Instead of hiding stars, let's make them brighter/more numerous visually by 
        // controlling their alpha based on scroll position.

        const scrollY = window.scrollY;
        const maxScroll = document.body.scrollHeight - window.innerHeight;
        const scrollProgress = Math.min(scrollY / maxScroll, 1); // 0 to 1

        stars.forEach((star, index) => {
            star.update();

            // Dynamic Density Logic:
            // We only render a subset of stars at the top, and all stars at the bottom.
            // 'index' is 0 to 400. 
            // At scroll 0, we want maybe 10% visible (indices 0-40).
            // At scroll 1, we want 100% visible.

            // Calculate visibility threshold based on scroll
            // Power of 2 makes the reveal accelerate towards the end
            const visibleThreshold = baseStarCount * (0.1 + Math.pow(scrollProgress, 2) * 0.9);

            if (index < visibleThreshold) {
                // Star is visible
                // We also increase brightness as we go deeper
                const brightness = star.opacity * (0.5 + scrollProgress * 0.5);

                ctx.beginPath();
                ctx.fillStyle = `rgba(255, 255, 255, ${brightness})`;
                ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
                ctx.fill();
            }
        });

        requestAnimationFrame(animate);
    }

    window.addEventListener('resize', resize);
    resize();
    animate();
}

document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initFormHandling();
    initSmoothScroll();
    initLightbox();
    initKonamiCode();
    initSpaceBackground(); // Add this
});

/**
 * Initialize Lightbox for Project Images
 */
function initLightbox() {
    // Create Lightbox DOM
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.innerHTML = `
        <div class="lightbox-close">&times;</div>
        <img src="" alt="Project Fullscreen">
    `;
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector('img');
    const closeBtn = lightbox.querySelector('.lightbox-close');

    // Open Lightbox
    document.querySelectorAll('.screenshot-placeholder').forEach(placeholder => {
        placeholder.addEventListener('click', () => {
            const img = placeholder.querySelector('img');
            if (img) {
                lightboxImg.src = img.src;
                lightbox.classList.add('active');
            }
        });
    });

    // Close Lightbox
    const closeLightbox = () => {
        lightbox.classList.remove('active');
        setTimeout(() => {
            lightboxImg.src = '';
        }, 300); // Clear src after transition
    };

    closeBtn.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
}

/**
 * Initialize Intersection Observer for scroll animations
 */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Add fade-in class to elements we want to animate
    const animatedElements = document.querySelectorAll('.hero-content, .card, .project-row, .timeline-end-card, .contact-text, .contact-form-wrapper');

    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        // Use modulo to reset delay every 5 elements, preventing huge delays at bottom of page
        // Max delay is now 0.2s (4 * 0.05)
        const delay = (index % 5) * 0.05;
        el.style.transition = `opacity 0.3s ease-out ${delay}s, transform 0.3s ease-out ${delay}s`;
        observer.observe(el);
    });

    // Custom class for "in-view" state
    const style = document.createElement('style');
    style.innerHTML = `
        .in-view {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
}



/**
 * Initialize Konami Code Easter Egg
 * Sequence: ↑ ↑ ↓ ↓ ← → ← → B A
 */
function initKonamiCode() {
    const code = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
    let index = 0;

    // Console Invitation
    console.log('%c🐰 Psst... Try the Konami Code.', 'font-size: 12px; color: #a855f7; font-weight: bold; background: #f3f4f6; padding: 4px 8px; border-radius: 4px;');

    document.addEventListener('keydown', (e) => {
        // Check if key matches the current step in sequence
        if (e.key === code[index]) {
            index++;
            console.log(`%c🔑 Key accepted: ${e.key} (${index}/${code.length})`, 'color: #10b981;');

            // If sequence is complete
            if (index === code.length) {
                console.log('%c🔓 ACCESS GRANTED. Welcome to the Matrix.', 'font-size: 16px; color: #10b981; font-weight: bold;');
                toggleMatrixMode();
                index = 0; // Reset
            }
        } else {
            if (index > 0) {
                console.log('%c❌ Access Denied. Sequence reset.', 'color: #ef4444;');
            }
            index = 0; // Reset if wrong key
        }
    });
}

/**
 * Toggle Matrix Mode (Easter Egg)
 */
/**
 * Toggle Matrix Mode (Easter Egg)
 */
let matrixInterval;

function toggleMatrixMode() {
    document.body.classList.toggle('matrix-mode');
    const isMatrix = document.body.classList.contains('matrix-mode');

    if (isMatrix) {
        alert('🐇 Follow the white rabbit...');
        startMatrixRain();
    } else {
        stopMatrixRain();
    }
}

function startMatrixRain() {
    // Create Canvas
    const canvas = document.createElement('canvas');
    canvas.id = 'matrix-rain';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '9998'; // Behind content but in front of background
    canvas.style.pointerEvents = 'none';
    canvas.style.opacity = '0.15'; // Subtle overlay
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン0123456789Z';
    const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const nums = '0123456789';
    const alphabet = katakana + latin + nums;

    const fontSize = 16;
    const columns = canvas.width / fontSize;

    const rainDrops = [];
    for (let x = 0; x < columns; x++) {
        rainDrops[x] = 1;
    }

    const draw = () => {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0F0';
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < rainDrops.length; i++) {
            const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);

            if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    };

    matrixInterval = setInterval(draw, 30);

    // Handle Resize
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

function stopMatrixRain() {
    clearInterval(matrixInterval);
    const canvas = document.getElementById('matrix-rain');
    if (canvas) canvas.remove();
}

/**
 * Initialize Smooth Scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 100, // Offset for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Initialize Form Handling and Toast
 */
function initFormHandling() {
    // Check URL for success param
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('success') === 'true') {
        setTimeout(() => {
            showToast();
        }, 1000); // Delay for visibility
        cleanUrl();
    }
}

function showToast() {
    const toast = document.getElementById('toast');
    if (toast) {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 5000);
    }
}

function cleanUrl() {
    const url = new URL(window.location);
    url.searchParams.delete('success');
    window.history.replaceState({}, document.title, url.pathname + url.hash);
}
