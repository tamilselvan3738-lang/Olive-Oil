import os

file_path = 'Balsamic Vinegar Collection.html'

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

# 1. New CSS for the Gallery Wall Design
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

    /* ---------- GALLERY WALL LAYOUT ---------- */
    .gallery-wrapper { max-width: 1400px; margin: 0 auto; padding: 4rem 2rem; display: flex; flex-direction: column; gap: 8rem; }
    
    .gallery-title { font-size: 3.5rem; font-family: 'Playfair Display', serif; text-align: center; margin-bottom: 2rem; color: var(--text-main); letter-spacing: -1px; }
    .gallery-subtitle { font-size: 1.2rem; text-align: center; color: var(--text-muted); max-width: 600px; margin: 0 auto 5rem; }
    
    .gallery-btn { display: inline-block; background: transparent; color: var(--text-main); border: 1px solid var(--gold); padding: 0.8rem 2rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 2px; text-decoration: none; transition: all 0.3s ease; }
    .gallery-btn:hover { background: var(--gold); color: #ffffff; }

    /* The Z-Pattern Exhibit Row */
    .exhibit-row { display: flex; flex-direction: column; align-items: center; gap: 4rem; position: relative; }
    @media(min-width: 992px) { .exhibit-row { flex-direction: row; justify-content: space-between; } }
    .exhibit-row.reverse { flex-direction: column; }
    @media(min-width: 992px) { .exhibit-row.reverse { flex-direction: row-reverse; } }
    
    .exhibit-img { flex: 1.2; width: 100%; position: relative; }
    .exhibit-img img { width: 100%; height: 500px; object-fit: cover; box-shadow: 20px 20px 0px var(--bg-surface), 21px 21px 0px var(--border-light); transition: transform 0.5s ease; }
    .exhibit-row:hover .exhibit-img img { transform: translate(-5px, -5px); }
    
    .exhibit-text { flex: 1; padding: 2rem 0; }
    @media(min-width: 992px) { .exhibit-text { padding: 2rem 4rem; } }
    .exhibit-text h2 { font-size: 2.5rem; font-family: 'Playfair Display', serif; margin-bottom: 1.5rem; color: var(--text-main); position: relative; display: inline-block; }
    .exhibit-text h2::after { content: ''; position: absolute; bottom: -5px; left: 0; width: 40px; height: 2px; background: var(--accent); }
    .exhibit-text p { font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 2rem; }
    
    /* 3-Column Display (For Culinary & Gifts) */
    .triptych-grid { display: grid; grid-template-columns: 1fr; gap: 2rem; }
    @media(min-width: 768px) { .triptych-grid { grid-template-columns: repeat(3, 1fr); } }
    .triptych-card { background: var(--bg-surface); padding: 2rem; text-align: center; border: 1px solid var(--border-light); transition: transform 0.3s; }
    .triptych-card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0,0,0,0.05); }
    .triptych-card img { width: 100%; height: 200px; object-fit: cover; margin-bottom: 1.5rem; }
    .triptych-card h3 { font-size: 1.5rem; font-family: 'Playfair Display', serif; margin-bottom: 0.5rem; }
    .triptych-card p { font-size: 0.95rem; color: var(--text-muted); }
    
    /* 4-Grid Masonry (For Fruit Infused) */
    .masonry-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
    .masonry-item img { width: 100%; height: 100%; object-fit: cover; aspect-ratio: 1; transition: filter 0.3s; }
    .masonry-item:hover img { filter: brightness(1.1); }
    .masonry-item:nth-child(1) { grid-column: span 2; aspect-ratio: 2/1; }

    /* Vault Layout (For Reserves) */
    .vault-section { background: var(--bg-surface); border: 1px solid var(--border-light); padding: 6rem 2rem; text-align: center; position: relative; overflow: hidden; }
    .vault-section::before { content: ''; position: absolute; top: 10px; left: 10px; right: 10px; bottom: 10px; border: 1px solid var(--border-light); pointer-events: none; }
    .vault-content { max-width: 700px; margin: 0 auto; position: relative; z-index: 2; }
    .vault-icon { font-size: 2.5rem; color: var(--gold); margin-bottom: 1.5rem; }
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
<div class="gallery-wrapper">

  <div style="text-align: center; margin-bottom: -4rem;" class="reveal-on-scroll">
    <span style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 4px; color: var(--gold); display: block; margin-bottom: 1rem;">The Dark Gold of Modena</span>
    <h1 class="gallery-title">The Balsamic Gallery</h1>
    <p class="gallery-subtitle">A curated exhibition of our finest aged vinegars, from traditional centuries-old methods to vibrant modern infusions.</p>
  </div>

  <!-- 1. Traditional Balsamic -->
  <section class="exhibit-row reveal-on-scroll">
    <div class="exhibit-img">
      <img src="images/bal_traditional.png" alt="Traditional Balsamic Vinegar">
    </div>
    <div class="exhibit-text">
      <h2>Traditional Balsamic</h2>
      <p>The foundation of Italian culinary heritage. Made purely from Trebbiano and Lambrusco grape must, reduced slowly over an open flame, and transferred through a battery of wooden barrels. Rich, thick, and perfectly balanced between sweet and tart.</p>
      <ul style="list-style: none; margin-bottom: 2rem; color: var(--text-muted);">
        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check" style="color: var(--accent); margin-right: 10px;"></i> PGI Certified from Modena</li>
        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check" style="color: var(--accent); margin-right: 10px;"></i> No added sugars or caramels</li>
      </ul>
      <a href="#" class="gallery-btn">Explore Collection</a>
    </div>
  </section>

  <!-- 2. Aged Balsamic -->
  <section class="exhibit-row reverse reveal-on-scroll">
    <div class="exhibit-img">
      <img src="images/bal_aged.png" alt="Aged Balsamic Vinegar Barrels">
    </div>
    <div class="exhibit-text">
      <h2>Aged Balsamic</h2>
      <p>Time is the most vital ingredient. Our aged balsamic vinegars spend a minimum of 12 years resting in oak, cherry, chestnut, and juniper barrels, absorbing the complex tannins and aromas of the wood. The result is a profound depth of flavor reserved for finishing fine meats and artisan cheeses.</p>
      <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
        <span style="border: 1px solid var(--border-light); padding: 0.5rem 1rem; font-size: 0.85rem;">12-Year</span>
        <span style="border: 1px solid var(--border-light); padding: 0.5rem 1rem; font-size: 0.85rem;">18-Year</span>
        <span style="border: 1px solid var(--gold); background: var(--bg-surface); padding: 0.5rem 1rem; font-size: 0.85rem; font-weight: bold;">25-Year</span>
      </div>
      <a href="#" class="gallery-btn">View Aged Vintages</a>
    </div>
  </section>

  <!-- 3. White Balsamic -->
  <section class="exhibit-row reveal-on-scroll">
    <div class="exhibit-img" style="display: flex; gap: 1rem; align-items: stretch;">
      <div style="flex: 1;"><img src="images/bal_white1.png" alt="White Balsamic Pour" style="height: 100%;"></div>
      <div style="flex: 1;"><img src="images/bal_white2.png" alt="White Balsamic Salad" style="height: 100%; margin-top: 2rem;"></div>
    </div>
    <div class="exhibit-text">
      <h2>White Balsamic</h2>
      <p>Bright, crisp, and clear. White balsamic is cooked at lower temperatures to prevent caramelization, preserving its delicate golden hue and sharp, fruit-forward acidity. It provides all the complex flavor of traditional balsamic without discoloring your vibrant salads and seafood dishes.</p>
      <a href="#" class="gallery-btn">Shop White Balsamics</a>
    </div>
  </section>

  <!-- 4. Fruit Infused Balsamic -->
  <section class="exhibit-row reverse reveal-on-scroll">
    <div class="exhibit-img masonry-grid">
      <div class="masonry-item"><img src="images/bal_fruit_main.png" alt="Fruit Infused Balsamic"></div>
      <div class="masonry-item"><img src="images/bal_fruit_fig.png" alt="Fig Balsamic"></div>
      <div class="masonry-item"><img src="images/bal_fruit_berry.png" alt="Raspberry Balsamic"></div>
    </div>
    <div class="exhibit-text">
      <h2>Fruit Infused Balsamic</h2>
      <p>A celebration of the orchard. We blend our premium white and dark balsamics with real, whole-fruit purées to create vibrant, versatile condiments. From the deep jammy notes of Black Mission Fig to the bright tartness of Sicilian Lemon, these vinegars bring salads, marinades, and even cocktails to life.</p>
      <a href="#" class="gallery-btn">Explore Flavors</a>
    </div>
  </section>

  <!-- 5. Specialty Blends -->
  <section class="exhibit-row reveal-on-scroll">
    <div class="exhibit-img">
      <img src="images/bal_specialty.png" alt="Specialty Balsamic Blends">
    </div>
    <div class="exhibit-text">
      <h2>Specialty Blends</h2>
      <p>For the adventurous chef. Our master blenders have crafted unique profiles by marrying balsamic with unexpected savory elements. Experience the earthy luxury of our White Truffle Balsamic, or the rich, roasted depth of our Espresso Dark Balsamic—perfect for glazing steaks or drizzling over gelato.</p>
      <a href="#" class="gallery-btn">Discover Blends</a>
    </div>
  </section>

  <!-- 6. Premium Reserves -->
  <section class="vault-section reveal-on-scroll">
    <div class="vault-content">
      <div class="vault-icon"><i class="fas fa-key"></i></div>
      <h2 style="font-size: 3rem; font-family: 'Playfair Display', serif; margin-bottom: 1rem;">Premium Reserves</h2>
      <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 2rem;">Highly allocated, intensely aged, and extraordinarily rare. Our Premium Reserve balsamics represent the absolute pinnacle of Modena's craft. Limited to only 100 bottles per year, these are liquid treasures.</p>
      <img src="images/bal_reserve_bottle.png" alt="Reserve Bottle" style="width: 150px; margin: 0 auto 2rem; display: block;">
      <a href="#" class="gallery-btn">Request Allocation</a>
    </div>
  </section>

  <!-- 7. Culinary Favorites -->
  <section class="reveal-on-scroll">
    <h2 class="gallery-title" style="font-size: 2.5rem; text-align: left;">7. Culinary Favorites</h2>
    <div class="triptych-grid">
      <div class="triptych-card">
        <img src="images/bal_fav_fig.png" alt="Fig Dark Balsamic">
        <h3>Fig Dark Balsamic</h3>
        <p>Our #1 best-seller. Incredibly versatile for salads and cheese boards.</p>
      </div>
      <div class="triptych-card">
        <img src="images/bal_fav_peach.png" alt="Peach White Balsamic">
        <h3>Peach White Balsamic</h3>
        <p>A summer staple. Bright, sweet, and perfect for fruit salads or cocktails.</p>
      </div>
      <div class="triptych-card">
        <img src="images/bal_fav_garlic.png" alt="Garlic Cilantro Balsamic">
        <h3>Garlic Cilantro</h3>
        <p>Savory and punchy. The ultimate marinade for grilled chicken and vegetables.</p>
      </div>
    </div>
  </section>

  <!-- 8. Gift Sets -->
  <section class="reveal-on-scroll">
    <h2 class="gallery-title" style="font-size: 2.5rem; text-align: left;">8. Balsamic Gift Sets</h2>
    <div class="exhibit-row reverse" style="gap: 2rem; align-items: stretch;">
      <div class="exhibit-img" style="flex: 2;">
        <img src="images/bal_giftset.png" alt="Balsamic Gift Box" style="height: 100%; min-height: 400px;">
      </div>
      <div class="exhibit-text" style="flex: 1; display: flex; flex-direction: column; justify-content: center; background: var(--bg-surface); padding: 3rem; border: 1px solid var(--border-light);">
        <h3>The Connoisseur's Flight</h3>
        <p style="margin-top: 1rem;">Give the gift of extraordinary flavor. Our elegantly packaged tasting flights include six 60ml bottles of our most popular traditional, white, and infused balsamics.</p>
        <a href="#" class="gallery-btn" style="margin-top: 1.5rem; align-self: flex-start;">Shop Gifts</a>
      </div>
    </div>
  </section>

</div>

<script>
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

print("Successfully redesigned Balsamic Vinegar Collection.html with the Gallery Wall layout.")
