import os

file_path = 'Oil of the Month Club.html'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found.")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate boundaries
header_end = content.find('</header>') + 9
footer_start = content.find('<footer class="footer">')
style_start = content.find('<style>') + 7
style_end = content.find('</style>')

if header_end == 8 or footer_start == -1 or style_start == 6 or style_end == -1:
    print("Error: Could not find necessary boundaries in HTML.")
    exit(1)

# 1. New CSS for the VIP Portal Design
new_css = """
    /* ---------- GLOBAL THEME VARIABLES ---------- */
    :root {
      --bg-main: #fefaf5;
      --bg-surface: #ffffff;
      --text-main: #2c2418;
      --text-muted: #6b5a48;
      --accent: #5f8b6f;
      --accent-hover: #4a6f58;
      --border-light: #e9dfd3;
      --gold: #cfbcab;
    }
    body.dark {
      --bg-main: #121212;
      --bg-surface: #1e1915;
      --text-main: #ece8e0;
      --text-muted: #8a7a68;
      --border-light: #3a2e26;
      --gold: #d4b88b;
    }

    /* ---------- RESET & BASE ---------- */
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body{ font-family: 'Inter', sans-serif; background-color: var(--bg-main); color: var(--text-main); transition: background-color 0.3s ease, color 0.2s ease; line-height: 1.6; overflow-x: clip; width: 100%; }
    
    /* Reveal Animation */
    .reveal-on-scroll { opacity: 0; transform: translateY(40px); transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1); will-change: opacity, transform; }
    .reveal-on-scroll.is-visible { opacity: 1; transform: translateY(0); }

    /* ---------- VIP PORTAL LAYOUT ---------- */
    .vip-wrapper { position: relative; width: 100%; }
    .vip-btn { background: var(--accent); color: #ffffff; border: none; padding: 1rem 2.5rem; border-radius: 50px; font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
    .vip-btn:hover { background: var(--accent-hover); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .vip-section-title { font-size: 3.5rem; font-family: 'Playfair Display', serif; text-align: center; margin-bottom: 4rem; color: var(--text-main); }
    @media(max-width: 768px) { .vip-section-title { font-size: 2.5rem; } }

    /* 1. Split-Screen Hero */
    .vip-hero { display: flex; min-height: 90vh; flex-direction: column; }
    @media(min-width: 1024px) { .vip-hero { flex-direction: row; } }
    .vip-hero-img { flex: 1; min-height: 400px; background: url('images/club_hero.png') center/cover; position: relative; }
    .vip-hero-img::after { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(to right, transparent, var(--bg-main)); }
    @media(max-width: 1024px) { .vip-hero-img::after { background: linear-gradient(to bottom, transparent, var(--bg-main)); } }
    .vip-hero-content { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 4rem; z-index: 2; }
    .vip-hero-content h1 { font-size: 4rem; font-family: 'Playfair Display', serif; margin-bottom: 1.5rem; line-height: 1.1; }
    .vip-hero-content p { font-size: 1.25rem; color: var(--text-muted); margin-bottom: 2.5rem; max-width: 500px; }

    /* 2. The Journey (Flowchart) */
    .vip-journey { padding: 8rem 2rem; border-top: 1px solid var(--border-light); }
    .journey-grid { display: grid; grid-template-columns: 1fr; gap: 3rem; max-width: 1200px; margin: 0 auto; position: relative; }
    @media(min-width: 768px) { .journey-grid { grid-template-columns: repeat(3, 1fr); } }
    .journey-grid::before { content: ''; position: absolute; top: 40px; left: 10%; width: 80%; height: 2px; background: dashed 2px var(--gold); z-index: 0; display: none; }
    @media(min-width: 768px) { .journey-grid::before { display: block; } }
    .journey-step { position: relative; z-index: 1; text-align: center; }
    .journey-icon { width: 80px; height: 80px; border-radius: 50%; background: var(--bg-surface); border: 2px solid var(--gold); margin: 0 auto 1.5rem; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: var(--accent); box-shadow: 0 0 0 10px var(--bg-main); }
    .journey-step h3 { font-size: 1.5rem; margin-bottom: 1rem; }
    .journey-step p { color: var(--text-muted); }

    /* 3. Monthly Selections (Calendar Grid) */
    .vip-selections { padding: 8rem 2rem; background: var(--bg-surface); }
    .selections-wrapper { max-width: 1400px; margin: 0 auto; display: flex; gap: 2rem; overflow-x: auto; padding-bottom: 2rem; scroll-snap-type: x mandatory; }
    .selections-wrapper::-webkit-scrollbar { height: 6px; }
    .selections-wrapper::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 10px; }
    .selection-card { min-width: 400px; flex-shrink: 0; scroll-snap-align: center; border: 1px solid var(--border-light); border-radius: 1.5rem; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.3s; }
    .selection-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.05); }
    .selection-img { height: 250px; background-size: cover; background-position: center; position: relative; }
    .selection-month { position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.9); color: #2c2418; padding: 0.5rem 1.5rem; border-radius: 50px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem; }
    body.dark .selection-month { background: rgba(30,25,21,0.9); color: var(--text-main); }
    .selection-info { padding: 2.5rem; flex: 1; display: flex; flex-direction: column; }
    .selection-info h3 { font-size: 1.8rem; font-family: 'Playfair Display', serif; margin-bottom: 1rem; }
    .selection-info p { color: var(--text-muted); margin-bottom: 1.5rem; flex: 1; }

    /* 4. Member Benefits (Circular Grid) */
    .vip-benefits { padding: 8rem 2rem; border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); }
    .benefits-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 4rem; max-width: 1200px; margin: 0 auto; }
    .benefit-item { text-align: center; display: flex; flex-direction: column; align-items: center; }
    .benefit-circle { width: 150px; height: 150px; border-radius: 50%; background: var(--bg-surface); border: 1px solid var(--border-light); display: flex; align-items: center; justify-content: center; font-size: 3.5rem; color: var(--gold); margin-bottom: 2rem; transition: transform 0.5s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.02); }
    .benefit-item:hover .benefit-circle { transform: rotateY(180deg); background: var(--bg-main); }
    .benefit-item h4 { font-size: 1.4rem; margin-bottom: 0.5rem; }
    .benefit-item p { color: var(--text-muted); font-size: 0.95rem; }

    /* 5. Membership Plans (Pricing Tables) */
    .vip-pricing { padding: 8rem 2rem; background: var(--bg-surface); }
    .pricing-grid { display: grid; grid-template-columns: 1fr; gap: 2rem; max-width: 1200px; margin: 0 auto; align-items: center; }
    @media(min-width: 1024px) { .pricing-grid { grid-template-columns: repeat(3, 1fr); } }
    .price-card { border: 1px solid var(--border-light); border-radius: 2rem; padding: 3rem; position: relative; transition: all 0.4s ease; background: var(--bg-main); }
    .price-card:hover { transform: translateY(-15px); box-shadow: 0 30px 60px rgba(0,0,0,0.08); border-color: var(--gold); }
    .price-card.popular { border: 2px solid var(--accent); transform: scale(1.05); z-index: 2; box-shadow: 0 20px 40px rgba(0,0,0,0.05); }
    @media(max-width: 1023px) { .price-card.popular { transform: scale(1); } }
    .price-badge { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--accent); color: white; padding: 0.5rem 1.5rem; border-radius: 50px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
    .price-card h3 { font-size: 2rem; font-family: 'Playfair Display', serif; text-align: center; margin-bottom: 0.5rem; }
    .price-amount { text-align: center; font-size: 3.5rem; font-weight: bold; margin-bottom: 2rem; color: var(--accent); }
    .price-amount span { font-size: 1rem; color: var(--text-muted); font-weight: normal; }
    .price-list { list-style: none; margin-bottom: 3rem; }
    .price-list li { margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-light); display: flex; align-items: flex-start; gap: 10px; color: var(--text-muted); }
    .price-list li:last-child { border-bottom: none; }
    .price-list li i { color: var(--gold); margin-top: 5px; }

    /* 6. The Reserve Collection (Showcase) */
    .vip-reserve { position: relative; padding: 10rem 2rem; text-align: center; background: url('images/club_reserve.png') center/cover; background-attachment: fixed; color: #ffffff; }
    .vip-reserve::before { content: ''; position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(26,22,18,0.8); }
    .reserve-content { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; }
    .reserve-content h2 { font-size: 4rem; font-family: 'Playfair Display', serif; margin-bottom: 1.5rem; color: #ffffff; }
    .reserve-content p { font-size: 1.2rem; line-height: 1.8; opacity: 0.9; margin-bottom: 3rem; }

    /* 7. Subscription Management (Accordions) */
    .vip-manage { padding: 8rem 2rem; }
    .manage-container { max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem; }
    .accordion { border: 1px solid var(--border-light); border-radius: 1rem; background: var(--bg-surface); overflow: hidden; }
    .accordion-header { padding: 1.5rem 2rem; display: flex; justify-content: space-between; align-items: center; cursor: pointer; background: transparent; transition: background 0.3s; }
    .accordion-header:hover { background: rgba(0,0,0,0.02); }
    body.dark .accordion-header:hover { background: rgba(255,255,255,0.02); }
    .accordion-header h4 { font-size: 1.2rem; margin: 0; }
    .accordion-icon { transition: transform 0.3s ease; color: var(--gold); }
    .accordion.active .accordion-icon { transform: rotate(180deg); }
    .accordion-content { padding: 0 2rem; max-height: 0; overflow: hidden; transition: max-height 0.4s ease, padding 0.4s ease; color: var(--text-muted); }
    .accordion.active .accordion-content { padding: 0 2rem 1.5rem; max-height: 300px; }

    /* 8. Testimonials */
    .vip-testimonials { padding: 8rem 2rem; background: var(--bg-surface); text-align: center; }
    .testi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem; max-width: 1200px; margin: 0 auto; }
    .testi-card { padding: 3rem; border: 1px solid var(--border-light); border-radius: 1rem; position: relative; background: var(--bg-main); }
    .testi-quote-icon { position: absolute; top: -20px; left: 50%; transform: translateX(-50%); width: 40px; height: 40px; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 1rem; }
    .testi-card p { font-size: 1.1rem; font-style: italic; color: var(--text-muted); margin-bottom: 2rem; line-height: 1.8; }
    .testi-author { font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem; color: var(--text-main); }
/* ==========================================================================
       GLOBAL RESPONSIVE OVERRIDES (Mobile Breakpoints: 320px, 480px, 768px, 1024px)
       ========================================================================== */
    html, body{
      max-width: 100% !important;
      overflow-x: clip !important;
      box-sizing: border-box !important;
    }
    *, *::before, *::after {
      box-sizing: inherit !important;
    }
    img, video, picture, iframe {
      max-width: 100% !important;
      height: auto !important;
    }
    p, h1, h2, h3, h4, h5, h6, span, a, li {
      word-wrap: break-word !important;
      overflow-wrap: break-word !important;
    }

    /* Prevent flex containers or elements with fixed widths from overflowing */
    .container, .gallery-wrapper, .vip-wrapper, .workshop-wrapper, .pr-container, .editorial-container, .contact-section {
      width: 100% !important;
      max-width: 100% !important;
      overflow-x: clip !important;
    }

    @media (max-width: 1024px) {
      /* Smooth out desktop-to-tablet transitions */
      .cards-grid, .pricing-grid, .profiles-grid, .science-bento-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }

    @media (max-width: 768px) {
      /* Mobile layout stack overrides */
      section, 
      .about-section, 
      .ws-custom-box, 
      .ws-holiday, 
      .ws-corporate, 
      .ws-gourmet, 
      .ws-packaging, 
      .ws-unboxing, 
      .ws-shipping, 
      .vip-journey, 
      .vip-selections, 
      .vip-benefits, 
      .vip-pricing, 
      .vip-testimonials, 
      .collection-section, 
      .features-section, 
      .heritage-section, 
      .pairing-section, 
      .club-section, 
      .testimonial-section,
      .terroir-section,
      .sustainability-section,
      .join-society-section,
      .creative-hero,
      .pairing-container,
      .exhibit-row,
      .exhibit-row.reverse,
      .asymmetric-section,
      .alchemy-section,
      .cultivars-section {
        padding: 2.5rem 1.25rem !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
      }
      .editorial-container {
        padding: 0 1.25rem !important;
        margin-top: 1.5rem !important;
        margin-bottom: 3rem !important;
      }
      .about-hero, .ws-hero, .contact-hero, .editorial-hero, .vip-hero-content {
        padding: 3.5rem 1.25rem !important;
        min-height: auto !important;
      }
      
      /* Typography responsive scaling */
      h1, .ws-hero h1, .ws-corp-text h2, .vip-section-title, .ws-holiday h2, .ws-gourmet h2, .ws-packaging h2, .ws-unboxing h2, .ws-shipping h2, .gallery-title {
        font-size: clamp(1.8rem, 7vw, 2.5rem) !important;
        line-height: 1.2 !important;
      }
      h2, .about-text h2, .section-title, .exhibit-text h2, .reserve-content h2 {
        font-size: clamp(1.5rem, 5.5vw, 1.8rem) !important;
        line-height: 1.2 !important;
      }
      h3 {
        font-size: clamp(1.2rem, 4.5vw, 1.4rem) !important;
      }

      /* Stack grids and columns vertically */
      .cards-grid, 
      .features-grid, 
      .testimonial-grid, 
      .collection-grid, 
      .about-grid, 
      .values-grid, 
      .ws-bento-grid, 
      .ws-pack-grid, 
      .ws-timeline, 
      .journey-grid, 
      .pricing-grid, 
      .benefits-grid, 
      .blog-layout, 
      .two-columns, 
      .contact-grid, 
      .matrix-grid, 
      .triptych-grid, 
      .masonry-grid,
      .terroir-grid,
      .creative-hero,
      .ws-custom-container,
      .ws-corp-container,
      .zig-zag-row,
      .profiles-grid,
      .sommelier-layout,
      .science-bento-grid,
      .sommelier-steps,
      .ws-steps-list,
      .feature-grid,
      .pairing-ingredients,
      .seasons-grid,
      .cultivar-grid,
      .alchemy-stages,
      .article-list,
      .article-item,
      .sidebar,
      .tags-cloud,
      .social-login,
      .checkbox-group,
      .exhibit-row,
      .exhibit-row.reverse,
      .pricing-grid,
      .testi-grid,
      .seasons-grid,
      .cultivar-grid {
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
      }
      
      /* Make items span full width when stacked */
      .matrix-col, .masonry-item, .triptych-card, .ws-pack-item, .ws-holiday-card, .selection-card, .price-card, .testi-card, .benefit-item, .journey-step, .profile-card, .science-card {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 100% !important;
      }
      
      /* Custom timeline stacking */
      .timeline::before, .ws-timeline::before, .alchemy-stages::before {
        display: none !important;
      }
      .timeline-item, .ws-timeline-item, .alchemy-stage {
        width: 100% !important;
        left: 0 !important;
        text-align: left !important;
        padding: 0 0 1.5rem 1.5rem !important;
        border-left: 2px solid #5f8b6f !important;
        border-bottom: none !important;
        display: flex !important;
        flex-direction: column !important;
      }
      .timeline-dot, .ws-timeline-icon, .alchemy-number {
        left: -6px !important;
        right: auto !important;
        position: absolute !important;
      }
      
      /* RTL Support for stacked timeline */
      body.rtl .timeline-item, body.rtl .ws-timeline-item, body.rtl .alchemy-stage {
        text-align: right !important;
        padding-left: 0 !important;
        padding-right: 1.5rem !important;
        border-left: none !important;
        border-right: 2px solid #5f8b6f !important;
      }
      body.rtl .timeline-dot, body.rtl .ws-timeline-icon, body.rtl .alchemy-number {
        left: auto !important;
        right: -6px !important;
      }

      /* Horizontal scroll elements stack vertically on mobile */
      .ws-scroll-row, .selections-wrapper {
        flex-direction: column !important;
        overflow-x: visible !important;
        padding: 1rem 0 !important;
        margin: 0 !important;
      }
      .ws-holiday-card, .selection-card {
        min-width: 100% !important;
        width: 100% !important;
        max-width: 100% !important;
      }

      /* Flex and spacing adjustments */
      .info-text, .info-image, .ws-visualizer, .ws-corp-img, .ws-corp-text, .exhibit-img, .exhibit-text {
        width: 100% !important;
        flex: none !important;
      }
      .ws-visualizer {
        position: static !important;
      }

      /* Image height adjustments for mobile */
      .exhibit-img img, .form-image img, .map-box img {
        height: auto !important;
        max-height: 300px !important;
        width: 100% !important;
        box-shadow: none !important;
      }
      
      /* Buttons fit mobile screens */
      .btn, .btn-primary, .btn-submit, .btn-secondary, .vip-btn, .login-btn, .mobile-login-btn, .gallery-btn {
        width: 100% !important;
        text-align: center !important;
        display: block !important;
        padding: 0.8rem 1.25rem !important;
      }
    }

    @media (max-width: 480px) {
      h1, .ws-hero h1 { font-size: 1.6rem !important; }
      h2, .about-text h2, .section-title { font-size: 1.35rem !important; }
      h3 { font-size: 1.15rem !important; }

      .login-container, .register-container, .ws-step, .sidebar-widget, .price-card, .value-card, .benefit-circle, .testi-card {
        padding: 1rem 0.75rem !important;
      }
      .ws-pack-item {
        width: 100% !important;
        height: auto !important;
        aspect-ratio: 1 !important;
      }
      .selection-card, .ws-holiday-card {
        height: auto !important;
      }
      
      /* Section padding reduction for small screens */
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container, .contact-section {
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
      }
    }

    @media (max-width: 320px) {
      h1, .ws-hero h1 { font-size: 1.45rem !important; }
      h2, .about-text h2 { font-size: 1.2rem !important; }
      
      /* Extra padding reduction */
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container, .contact-section {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        padding-top: 1.25rem !important;
        padding-bottom: 1.25rem !important;
      }
    }

    /* RTL Support for Font Awesome directional icons */
    body.rtl .fa-arrow-right, 
    body.rtl .fa-long-arrow-alt-right, 
    body.rtl .fa-chevron-right {
      display: inline-block !important;
      transform: scaleX(-1) !important;
    }

    /* --- INJECTED NAVBAR & FOOTER STYLES --- */
    body.dark .navbar {
      border-bottom: 1px solid rgba(58, 46, 38, 0.8);
      background: transparent;
    }

    body.dark .navbar::before {
      background: linear-gradient(135deg, rgba(31,27,22,0.95), rgba(42,36,30,0.95), rgba(26,35,30,0.95), rgba(31,27,22,0.95));
      background-size: 300% 300%;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }

    body.dark .footer {
      background-color: #1f1b16;
      border-bottom: 1px solid #3a2e26;
      border-top: 1px solid #3a2e26;
    }

    body.dark .nav-link,
    body.dark .nav-item a,
    body.dark .icon-btn,
    body.dark .login-btn,
    body.dark .mobile-controls .icon-btn,
    body.dark .mobile-login-btn,
    body.dark .footer a,
    body.dark .footer .footer-link,
    body.dark .footer-heading,
    body.dark .footer-bottom-text {
      color: #f0e9df;
    }
    
    body.dark .logo-text {
      background: linear-gradient(90deg, #f0e9df, #8fbc9f, #d4c3aa, #f0e9df);
      background-size: 300% auto;
      color: transparent !important;
      -webkit-background-clip: text;
      background-clip: text;
    }

    body.dark .dropdown-menu,
    body.dark .mega-dropdown-menu {
      background-color: #1f1b16;
      border-color: #4a3e34;
    }

    body.dark .dropdown-item,
    body.dark .mega-dropdown-item {
      color: #f0e9df;
    }

    body.dark .dropdown-item:hover,
    body.dark .mega-dropdown-item:hover {
      background-color: #3f3329;
    }

    body.dark .hamburger span {
      background-color: #f0e9df;
    }

    body.dark .login-btn {
      border-color: #c7b59b;
    }

    body.dark .mobile-controls {
      border-top-color: #3a2e26;
    }

    body.dark .feature-card,
    body.dark .blog-card {
      background-color: #1f1b16;
      border-color: #3a2e26;
    }

    body.dark .badge {
      background: #2f281f;
    }
    
    body.dark .footer {
      border-top-color: #3a2e26;
      background-color: #1f1b16;
    }
    
    body.dark .footer-social-icon {
      background-color: #1f1b16;
      color: #f0e9df;
    }
    
    body.dark .footer-social-icon:hover {
      background-color: #5f8b6f;
      color: white;
    }
    
    body.dark .footer-newsletter input {
      background-color: #1f1b16;
      border-color: #4a3e34;
      color: #f0e9df;
    }

    /* ---------- COMPACT NAVBAR (Reduced size) ---------- */
    @keyframes premiumShimmer {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    @keyframes glowingBorder {
      0% { background-position: 0% center; }
      100% { background-position: 200% center; }
    }

        .navbar {
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;
      padding: 0.4rem 1rem;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
      border-bottom: none;
      background: transparent;
    }

    .navbar::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(246,240,230,0.92), rgba(235,242,238,0.92), rgba(255,255,255,0.92));
      background-size: 300% 300%;
      animation: premiumShimmer 10s ease infinite;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      z-index: -1;
      pointer-events: none;
      transition: background 0.3s ease, backdrop-filter 0.3s ease;
    }

    .navbar::after {
      content: '';
      position: absolute;
      bottom: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, rgba(95,139,111,0.2), #5f8b6f, #cfbcab, rgba(95,139,111,0.2));
      background-size: 200% auto;
      animation: glowingBorder 4s linear infinite;
    }

    @media (min-width: 768px) {
      .navbar {
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;

        padding: 0.4rem 2rem;
      }
    }

    .nav-container {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      position: relative;
    }

    /* Logo - left side */
    .logo-area {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      flex-shrink: 0;
      min-width: 120px;
    }

    .logo-icon {
      font-size: 1.1rem;
      color: #5f8b6f;
    }

    @keyframes textGradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    .logo-text {
      font-weight: 800;
      font-size: 1.1rem;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #3f2e21, #5f8b6f, #b89f7a, #3f2e21);
      background-size: 300% auto;
      color: transparent;
      -webkit-background-clip: text;
      background-clip: text;
      animation: textGradient 6s linear infinite;
      text-decoration: none;
      white-space: nowrap;
      transition: transform 0.3s ease;
    }
    
    .logo-text:hover {
      transform: scale(1.02);
    }

    @media (min-width: 480px) {
      .logo-icon { font-size: 1.2rem; }
      .logo-text { font-size: 1.05rem; }
    }

    /* Desktop navigation menu - centered */
    .nav-menu {
      display: flex;
      list-style: none;
      align-items: center;
      justify-content: center;
      flex: 1;
      margin: 0 1rem;
      gap: 0.05rem;
    }

    .nav-item {
      position: relative;
    }

    .nav-link {
      display: flex;
      align-items: center;
      gap: 5px;
      padding: 0.3rem 0.7rem;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.8rem;
      color: #2c2418;
      border-radius: 30px;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      white-space: nowrap;
      position: relative;
    }

    .nav-link::after {
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: 2px;
      left: 50%;
      background: linear-gradient(90deg, #5f8b6f, #cfbcab);
      transition: width 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), left 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      border-radius: 2px;
      opacity: 0;
    }

    .nav-link:hover::after {
      width: 80%;
      left: 10%;
      opacity: 1;
    }

    .nav-link:hover {
      color: #5f8b6f;
      transform: translateY(-1px);
    }

    /* Dropdown menus - desktop */
    .mega-dropdown-menu, .dropdown-menu {
      position: absolute;
      top: 100%;
      left: 0;
      background: rgba(255, 253, 249, 0.95);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-radius: 18px;
      min-width: 200px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
      border: 1px solid rgba(233, 223, 211, 0.6);
      opacity: 0;
      visibility: hidden;
      transform: translateY(15px) scale(0.98);
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      z-index: 100;
      list-style: none;
      padding: 0.6rem 0;
    }

    .nav-item.mega-dropdown:hover .mega-dropdown-menu,
    .nav-item.dropdown:hover .dropdown-menu {
      opacity: 1;
      visibility: visible;
      transform: translateY(8px) scale(1);
    }

    .mega-dropdown-item, .dropdown-item {
      display: block;
      padding: 0.4rem 1.2rem;
      text-decoration: none;
      color: #2c2418;
      font-size: 0.75rem;
      font-weight: 450;
      transition: background 0.15s;
    }

    .mega-dropdown-item:hover, .dropdown-item:hover {
      background-color: #f7efe7;
    }

    /* Desktop controls (hidden on mobile/tablet) */
    .desktop-controls {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      margin-left: auto;
    }

    .icon-btn {
      background: none;
      border: none;
      font-size: 1rem;
      cursor: pointer;
      color: #2c2418;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .icon-btn:hover {
      background-color: #e7dfd6;
    }

    .login-btn {
      background: transparent;
      border: 1.5px solid #cfbcab;
      padding: 0.35rem 1rem;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.75rem;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      color: #2c2418;
      display: flex;
      align-items: center;
      gap: 6px;
      position: relative;
      overflow: hidden;
      z-index: 1;
    }

    .login-btn::before {
      content: '';
      position: absolute;
      top: 0; left: -100%; width: 100%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
      transition: left 0.5s ease;
      z-index: -1;
    }

    .login-btn:hover::before {
      left: 100%;
    }

    .login-btn:hover {
      background: linear-gradient(135deg, #5f8b6f, #4a6f58);
      border-color: transparent;
      color: #ffffff;
      box-shadow: 0 6px 16px rgba(95, 139, 111, 0.3);
      transform: translateY(-2px);
    }

    .hamburger { display: none; flex-direction: column; cursor: pointer; gap: 4px; margin-left: 6px; }
    .hamburger span { width: 22px; height: 2px; background-color: #2c2418; transition: 0.3s ease; border-radius: 2px; transform-origin: center; }
    .hamburger.active span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
    .hamburger.active span:nth-child(2) { opacity: 0; }
    .hamburger.active span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }

    @media (max-width: 1024px) {
      .desktop-controls { display: none !important; } .hamburger { display: flex; }
      .nav-menu { position: fixed; right: -100%; top: 0; flex-direction: column; background-color: #ffffff; width: 280px; height: 100vh; transition: right 0.3s cubic-bezier(0.2, 0.9, 0.4, 1.1); box-shadow: -4px 0 20px rgba(0, 0, 0, 0.15); padding: 70px 0 2rem 0; overflow-y: auto; z-index: 999; border-left: 1px solid #e2d6ca; align-items: stretch; gap: 0; margin: 0; flex: none; justify-content: flex-start; }
      body.dark .nav-menu { background-color: #1f1b16; border-left-color: #3a2e26; }
      .nav-menu.active { right: 0; }
      .nav-item { width: 100%; }
      .nav-link { white-space: normal; justify-content: space-between; padding: 0.75rem 1.5rem; border-radius: 0; font-size: 0.9rem; }
      .dropdown-menu, .mega-dropdown-menu { position: static; opacity: 1; visibility: visible; transform: none; display: none; width: 100%; background-color: rgba(0, 0, 0, 0.02); border: none; padding-left: 1.5rem; box-shadow: none; }
      .nav-item.dropdown.open .dropdown-menu, .nav-item.mega-dropdown.open .mega-dropdown-menu { display: block; }
      .mobile-controls { display: flex; flex-direction: column; gap: 12px; padding: 1.5rem; margin-top: 1rem; border-top: 1px solid #e9dfd3; }
      .mobile-controls .control-row { display: flex; align-items: center; width: 100%; }
      .mobile-controls .icon-btn { justify-content: flex-start; gap: 12px; width: auto; padding: 0.6rem 1rem; font-size: 0.9rem; border-radius: 12px; background-color: transparent; transition: all 0.2s; }
      .mobile-controls .icon-btn:hover { background-color: #e7dfd6; color: #2c2418; }
      body.dark .mobile-controls .icon-btn:hover { background-color: #3a2e26; color: #f0e9df; }
      .mobile-login-btn { border: 1.5px solid #cfbcab; padding: 0.7rem; border-radius: 40px; font-weight: 600; text-align: center; width: 100%; background: transparent; cursor: pointer; font-size: 0.9rem; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s; }
      .mobile-login-btn:hover { background-color: #e7dfd6; border-color: #5f8b6f; }
      .menu-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.4); z-index: 998; opacity: 0; visibility: hidden; transition: all 0.25s ease; }
      .menu-overlay.active { opacity: 1; visibility: visible; }
      .mobile-menu-close { position: absolute; top: 20px; right: 20px; background: none; border: none; font-size: 1.5rem; color: #2c2418; cursor: pointer; padding: 5px; transition: color 0.2s; display: block; z-index: 1000; }
      .mobile-menu-close:hover { color: #5f8b6f; }
      body.dark .mobile-menu-close { color: #f0e9df; }
    }
    @media (min-width: 1025px) {
      .mobile-controls, .mobile-menu-close {
        display: none !important;
      }
      .nav-menu {
        justify-content: center;
      }
      .logo-area, .desktop-controls {
        width: auto;
      }
    }

    /* ---------- RTL SUPPORT ---------- */
    body.rtl {
      direction: rtl;
    }
    body.rtl .nav-menu {
      padding-right: 0;
    }
    body.rtl .dropdown-menu,
    body.rtl .mega-dropdown-menu {
      left: auto;
      right: 0;
    }
    @media (max-width: 1024px) {
      body.rtl .nav-menu {
        right: auto;
        left: -100%;
        border-left: none;
        border-right: 1px solid #e2d6ca;
      }
      body.rtl .nav-menu.active {
        right: auto;
        left: 0;
      }
    }

    /* ---------- FOOTER SECTION - MATCHING NAVBAR STYLES ---------- */
    .footer {
      background-color: #ffffff;
      border-top: 1px solid #ede5db;
      margin-top: 3rem;
      padding: 2rem 1rem 1.5rem;
      transition: background 0.2s;
    }
    
    .footer-container {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
    }
    
    @media (min-width: 768px) {
      .footer-container {
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        padding: 0 1rem;
      }
    }
    
    /* Footer Logo Area - identical to navbar logo */
    .footer-logo-area {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      margin-bottom: 1rem;
    }
    
    .footer-logo-icon {
      font-size: 1.2rem;
      color: #5f8b6f;
    }
    
    .footer-logo-text {
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #3f2e21, #5f8b6f, #b89f7a, #3f2e21);
      background-size: 300% auto;
      color: transparent !important;
      -webkit-background-clip: text;
      background-clip: text;
      animation: textGradient 6s linear infinite;
      text-decoration: none;
      white-space: nowrap;
      transition: transform 0.3s ease;
      font-family: 'Inter', sans-serif;
    }
    .footer-logo-text:hover {
      transform: scale(1.02);
    }
    body.dark .footer-logo-text {
      background: linear-gradient(90deg, #f0e9df, #8fbc9f, #d4c3aa, #f0e9df);
      background-size: 300% auto;
      color: transparent !important;
      -webkit-background-clip: text;
      background-clip: text;
    }
    
    .footer-description {
      font-size: 0.8rem;
      line-height: 1.5;
      color: #5a4a38;
      margin-top: 0.5rem;
    }
    
    body.dark .footer-description {
      color: #c7b59b;
    }
    
    .footer-heading {
      font-weight: 600;
      font-size: 0.85rem;
      letter-spacing: 0.5px;
      color: #3f2e21;
      margin-bottom: 1rem;
      text-transform: uppercase;
    }
    
    .footer-links {
      list-style: none;
      padding: 0;
    }
    
    .footer-links li {
      margin-bottom: 0.6rem;
    }
    
    .footer-link {
      text-decoration: none;
      font-size: 0.78rem;
      font-weight: 500;
      color: #2c2418;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    
    .footer-link:hover {
      color: #5f8b6f;
      transform: translateX(3px);
    }
    
    body.rtl .footer-link:hover {
      transform: translateX(-3px);
    }
    
    /* Social Icons */
    .footer-social {
      display: flex;
      gap: 0.8rem;
      margin-top: 1rem;
      flex-wrap: wrap;
    }
    
    .footer-social-icon {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background-color: #f0e8df;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      color: #2c2418;
      font-size: 0.9rem;
      transition: all 0.2s;
    }
    
    .footer-social-icon:hover {
      background-color: #5f8b6f;
      color: white;
      transform: translateY(-2px);
    }
    
    /* Newsletter Form */
    .footer-newsletter {
      margin-top: 0.5rem;
    }
    
    .footer-newsletter input {
      width: 100%;
      padding: 0.6rem 0.8rem;
      border: 1px solid #e9dfd3;
      border-radius: 40px;
      font-family: 'Inter', sans-serif;
      font-size: 0.75rem;
      background-color: transparent;
      color: #2c2418;
      outline: none;
      transition: all 0.2s;
    }
    
    .footer-newsletter input:focus {
      border-color: #5f8b6f;
    }
    
    .footer-newsletter button {
      margin-top: 0.6rem;
      background-color: #5f8b6f;
      color: white;
      border: none;
      padding: 0.5rem 1.2rem;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.7rem;
      cursor: pointer;
      transition: background 0.2s;
      font-family: 'Inter', sans-serif;
    }
    
    .footer-newsletter button:hover {
      background-color: #4a6f58;
    }
    
    .footer-bottom {
      text-align: center;
      padding-top: 2rem;
      margin-top: 1.5rem;
      border-top: 1px solid #ede5db;
      font-size: 0.7rem;
    }
    
    .footer-bottom-text {
      color: #5a4a38;
    }
    
    @media (min-width: 768px) {
      .footer {
        padding: 2.5rem 2rem 1.5rem;
      }
    }
"""

# 2. New HTML
new_html = """
<div class="vip-wrapper">
  
  <!-- 1. Hero Intro (Split-Screen) -->
  <section class="vip-hero">
    <div class="vip-hero-img reveal-on-scroll"></div>
    <div class="vip-hero-content reveal-on-scroll">
      <h1>The Ultimate Tasting Experience</h1>
      <p>Join an exclusive community of culinary enthusiasts. Receive rare, limited-batch olive oils and aged vinegars delivered directly to your door every month.</p>
      <div><button class="vip-btn">Become a Member</button></div>
    </div>
  </section>

  <!-- 2. The Journey (How it Works) -->
  <section class="vip-journey">
    <h2 class="vip-section-title reveal-on-scroll">How The Club Works</h2>
    <div class="journey-grid">
      <div class="journey-step reveal-on-scroll">
        <div class="journey-icon"><i class="fas fa-leaf"></i></div>
        <h3>1. We Curate</h3>
        <p>Our sommeliers select the finest seasonal harvests from artisan groves globally.</p>
      </div>
      <div class="journey-step reveal-on-scroll" style="transition-delay: 0.1s;">
        <div class="journey-icon"><i class="fas fa-box-open"></i></div>
        <h3>2. We Deliver</h3>
        <p>Your beautifully packaged selection arrives with tasting notes and recipes.</p>
      </div>
      <div class="journey-step reveal-on-scroll" style="transition-delay: 0.2s;">
        <div class="journey-icon"><i class="fas fa-wine-glass-alt"></i></div>
        <h3>3. You Savor</h3>
        <p>Elevate your cooking and discover extraordinary new flavor profiles.</p>
      </div>
    </div>
  </section>

  <!-- 3. Monthly Selections (Calendar Grid) -->
  <section class="vip-selections">
    <h2 class="vip-section-title reveal-on-scroll">Upcoming Deliveries</h2>
    <div class="selections-wrapper reveal-on-scroll">
      <div class="selection-card">
        <div class="selection-img" style="background-image: url('images/club_month1.png');">
          <div class="selection-month">October</div>
        </div>
        <div class="selection-info">
          <h3>The Tuscan Harvest</h3>
          <p>A robust, peppery Coratina Extra Virgin Olive Oil paired with an 18-year aged traditional Balsamic. Perfect for hearty autumn roasting.</p>
          <a href="#" style="color: var(--accent); font-weight: bold; text-decoration: none; text-transform: uppercase; font-size: 0.85rem;">View Tasting Notes <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="selection-card">
        <div class="selection-img" style="background-image: url('images/club_month2.png');">
          <div class="selection-month">November</div>
        </div>
        <div class="selection-info">
          <h3>Truffle & Gold</h3>
          <p>Our exclusive White Truffle infused olive oil from Alba, Italy, paired with a delicate champagne vinegar. The ultimate holiday prep kit.</p>
          <a href="#" style="color: var(--accent); font-weight: bold; text-decoration: none; text-transform: uppercase; font-size: 0.85rem;">View Tasting Notes <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="selection-card">
        <div class="selection-img" style="background-image: url('images/club_month3.png');">
          <div class="selection-month">December</div>
        </div>
        <div class="selection-info">
          <h3>The Grand Reserve</h3>
          <p>A special year-end allocation of our 25-year aged Balsamico Tradizionale, strictly reserved for active club members.</p>
          <a href="#" style="color: var(--accent); font-weight: bold; text-decoration: none; text-transform: uppercase; font-size: 0.85rem;">View Tasting Notes <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. Member Benefits -->
  <section class="vip-benefits">
    <h2 class="vip-section-title reveal-on-scroll">Exclusive Member Benefits</h2>
    <div class="benefits-grid">
      <div class="benefit-item reveal-on-scroll">
        <div class="benefit-circle"><i class="fas fa-truck"></i></div>
        <h4>Free Shipping</h4>
        <p>On all club boxes and additional store orders over $50.</p>
      </div>
      <div class="benefit-item reveal-on-scroll">
        <div class="benefit-circle"><i class="fas fa-tags"></i></div>
        <h4>15% Store Discount</h4>
        <p>Enjoy a permanent discount on our entire catalog of oils and vinegars.</p>
      </div>
      <div class="benefit-item reveal-on-scroll">
        <div class="benefit-circle"><i class="fas fa-star"></i></div>
        <h4>Early Access</h4>
        <p>Shop limited-edition harvests 48 hours before the general public.</p>
      </div>
      <div class="benefit-item reveal-on-scroll">
        <div class="benefit-circle"><i class="fas fa-book-open"></i></div>
        <h4>Digital Magazine</h4>
        <p>Monthly recipes, chef interviews, and deep dives into olive varieties.</p>
      </div>
    </div>
  </section>

  <!-- 5. Membership Plans -->
  <section class="vip-pricing">
    <h2 class="vip-section-title reveal-on-scroll">Choose Your Tier</h2>
    <div class="pricing-grid">
      <div class="price-card reveal-on-scroll">
        <h3>The Enthusiast</h3>
        <div class="price-amount">$45<span>/mo</span></div>
        <ul class="price-list">
          <li><i class="fas fa-check"></i> 1 Premium EVOO (500ml)</li>
          <li><i class="fas fa-check"></i> Tasting Notes & Recipe Card</li>
          <li><i class="fas fa-check"></i> 10% Store Discount</li>
          <li><i class="fas fa-check"></i> Cancel Anytime</li>
        </ul>
        <button class="vip-btn" style="width: 100%; background: transparent; color: var(--accent); border: 2px solid var(--accent);">Select Plan</button>
      </div>
      <div class="price-card popular reveal-on-scroll">
        <div class="price-badge">Most Popular</div>
        <h3>The Connoisseur</h3>
        <div class="price-amount">$75<span>/mo</span></div>
        <ul class="price-list">
          <li><i class="fas fa-check"></i> 1 Premium EVOO (500ml)</li>
          <li><i class="fas fa-check"></i> 1 Aged Balsamic (250ml)</li>
          <li><i class="fas fa-check"></i> Tasting Notes & Recipe Book</li>
          <li><i class="fas fa-check"></i> 15% Store Discount & Free Shipping</li>
        </ul>
        <button class="vip-btn" style="width: 100%;">Select Plan</button>
      </div>
      <div class="price-card reveal-on-scroll">
        <h3>The Sommelier</h3>
        <div class="price-amount">$120<span>/mo</span></div>
        <ul class="price-list">
          <li><i class="fas fa-check"></i> 2 Ultra-Premium Oils (500ml)</li>
          <li><i class="fas fa-check"></i> 1 Reserve Balsamic (250ml)</li>
          <li><i class="fas fa-check"></i> Quarterly Artisan Pairing Gifts</li>
          <li><i class="fas fa-check"></i> 20% Store Discount & VIP Support</li>
        </ul>
        <button class="vip-btn" style="width: 100%; background: transparent; color: var(--accent); border: 2px solid var(--accent);">Select Plan</button>
      </div>
    </div>
  </section>

  <!-- 6. The Reserve Collection -->
  <section class="vip-reserve reveal-on-scroll">
    <div class="reserve-content">
      <h2>The Reserve Collection</h2>
      <p>Certain harvests are so scarce they never make it to our public shelves. As a club member, you guarantee your allocation of single-estate, early-harvest, and uniquely infused masterpieces.</p>
      <button class="vip-btn" style="background: transparent; border: 1px solid #ffffff;">View Past Reserves</button>
    </div>
  </section>

  <!-- 7. Subscription Management -->
  <section class="vip-manage">
    <h2 class="vip-section-title reveal-on-scroll">Complete Flexibility</h2>
    <div class="manage-container reveal-on-scroll">
      <div class="accordion active">
        <div class="accordion-header">
          <h4><i class="fas fa-pause-circle" style="margin-right: 10px; color: var(--accent);"></i> Skip a Month Anytime</h4>
          <i class="fas fa-chevron-down accordion-icon"></i>
        </div>
        <div class="accordion-content">
          <p>Going on vacation or simply have too much oil? You can pause your subscription or skip an upcoming delivery with a single click in your member dashboard. No questions asked, no hidden fees.</p>
        </div>
      </div>
      <div class="accordion">
        <div class="accordion-header">
          <h4><i class="fas fa-gift" style="margin-right: 10px; color: var(--accent);"></i> Gift Your Allocation</h4>
          <div class="accordion-icon"><i class="fas fa-chevron-down"></i></div>
        </div>
        <div class="accordion-content">
          <p>Want to share the love? You can easily redirect any month's box to a friend or family member's address, complete with a personalized gift note.</p>
        </div>
      </div>
      <div class="accordion">
        <div class="accordion-header">
          <h4><i class="fas fa-exchange-alt" style="margin-right: 10px; color: var(--accent);"></i> Customize Your Profile</h4>
          <div class="accordion-icon"><i class="fas fa-chevron-down"></i></div>
        </div>
        <div class="accordion-content">
          <p>Let us know your palate preferences. Prefer robust and peppery over mild and buttery? We tailor the Connoisseur and Sommelier boxes to your specific taste profile.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. Testimonials -->
  <section class="vip-testimonials">
    <h2 class="vip-section-title reveal-on-scroll">From Our Members</h2>
    <div class="testi-grid">
      <div class="testi-card reveal-on-scroll">
        <div class="testi-quote-icon"><i class="fas fa-quote-left"></i></div>
        <p>"I consider myself a foodie, but the quality of the oils in the Connoisseur box blew me away. The tasting notes really help you appreciate the nuances of each harvest."</p>
        <div class="testi-author">Michael T., Member since 2024</div>
      </div>
      <div class="testi-card reveal-on-scroll">
        <div class="testi-quote-icon"><i class="fas fa-quote-left"></i></div>
        <p>"It's like getting a present from Italy every month. The flexibility to skip a month when I travel is fantastic, but honestly, I rarely want to miss a box."</p>
        <div class="testi-author">Elena R., Member since 2023</div>
      </div>
      <div class="testi-card reveal-on-scroll">
        <div class="testi-quote-icon"><i class="fas fa-quote-left"></i></div>
        <p>"The 15% store discount pays for the membership itself. We use the member-exclusive white truffle oil for literally every dinner party we host."</p>
        <div class="testi-author">James & Clara., Members since 2025</div>
      </div>
    </div>
  </section>

</div>

<script>
  // Simple Accordion Logic
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const accordion = header.parentElement;
      const isActive = accordion.classList.contains('active');
      
      // Close all
      document.querySelectorAll('.accordion').forEach(acc => acc.classList.remove('active'));
      
      // Toggle current
      if (!isActive) {
        accordion.classList.add('active');
      }
    });
  });

  // Simple Scroll Reveal
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-on-scroll').forEach(el => observer.observe(el));
  });
</script>
"""

# Assemble new content
final_content = content[:style_start] + new_css + content[style_end:header_end] + new_html + content[footer_start:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Successfully redesigned Oil of the Month Club.html.")
