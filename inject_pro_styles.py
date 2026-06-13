import os

files_to_update = [
    'Flavor Profiles.html',
    'flavor.html',
    'Pairing Recommendations.html',
    'Balsamic Vinegar Collection.html'
]

pro_css = """
  <!-- PRO STYLES INJECTED -->
  <style id="pro-styles">
    /* ---------- PRO STYLES & MICRO-INTERACTIONS ---------- */
    ::selection { background: rgba(95, 139, 111, 0.3); color: inherit; }
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #cfbcab; border-radius: 10px; border: 2px solid transparent; background-clip: padding-box; }
    ::-webkit-scrollbar-thumb:hover { background-color: #5f8b6f; }
    body.dark ::-webkit-scrollbar-thumb { background-color: #3a2e26; }
    body.dark ::-webkit-scrollbar-thumb:hover { background-color: #8fbc9f; }

    html{ scroll-behavior: smooth; }

    /* Reveal Animations */
    .reveal-on-scroll { opacity: 0; transform: translateY(40px); transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1); will-change: opacity, transform; }
    .reveal-on-scroll.is-visible { opacity: 1; transform: translateY(0); }

    /* Subtle Image Enhancements */
    img { transition: filter 0.6s ease, transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1); }
    
    /* Button Polish */
    button, .btn, a { transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1); }
    button:active, .btn:active { transform: scale(0.97); }
    
    /* Soft Glows */
    .glow-on-hover:hover { box-shadow: 0 0 25px rgba(95, 139, 111, 0.4); }
  </style>
"""

pro_js = """
<!-- PRO ANIMATIONS SCRIPT INJECTED -->
<script id="pro-animations-script">
  document.addEventListener('DOMContentLoaded', () => {
    // 1. Intersection Observer for fade-up animations
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Auto-attach to major layout elements
    const selectorsToAnimate = [
      '.editorial-section', '.matrix-col', '.taste-matrix', '.editorial-hero', 
      '.bento-item', '.bento-hero', '.pr-filter-btn',
      '.lux-card', '.lux-section', '.hero-mock'
    ];
    
    const elements = document.querySelectorAll(selectorsToAnimate.join(', '));
    elements.forEach((el, index) => {
      // Add slight staggered delay based on index for siblings
      el.classList.add('reveal-on-scroll');
      el.style.transitionDelay = `${(index % 3) * 0.1}s`;
      observer.observe(el);
    });

    // 2. Parallax effect on hero images
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const heroImgs = document.querySelectorAll('.editorial-hero-img, .editorial-banner-img, .bento-hero-img');
      heroImgs.forEach(img => {
        img.style.transform = `translateY(${scrolled * 0.15}px) scale(1.05)`;
      });
    });
  });
</script>
"""

for file in files_to_update:
    if not os.path.exists(file):
        print(f"Skipping {file}, not found.")
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Inject CSS
    if 'id="pro-styles"' not in content:
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + pro_css + content[head_end:]
            modified = True

    # Inject JS
    if 'id="pro-animations-script"' not in content:
        body_end = content.find('</body>')
        if body_end != -1:
            content = content[:body_end] + pro_js + content[body_end:]
            modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected pro styles into {file}")
    else:
        print(f"{file} already has pro styles.")
