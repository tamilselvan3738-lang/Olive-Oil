import glob
import re

new_css = """  <!-- GLOBAL RESPONSIVE SCALING (Aligned with about.html behavior) -->
  <style id="global-responsive-scaling">
    html, body{
      overflow-x: clip !important;
      width: 100% !important;
      max-width: 100vw !important;
    }
    *, *::before, *::after {
      box-sizing: border-box !important;
    }
    img, video, iframe {
      max-width: 100% !important;
    }
    
    /* Ensure text doesn't overflow */
    p, h1, h2, h3, h4, h5, h6, a, span, div {
      word-wrap: break-word;
      overflow-wrap: break-word;
    }

    @media (max-width: 1024px) {
      h1, .hero-title { font-size: clamp(2.5rem, 5vw, 4rem) !important; }
      .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1, .contact-hero h1 { font-size: 3rem !important; }
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container, .contact-section { padding-left: 2rem !important; padding-right: 2rem !important; }
    }
    
    @media (max-width: 768px) {
      /* Typography */
      h1, .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1, .contact-hero h1 { font-size: 2.2rem !important; margin-bottom: 1rem !important; }
      p, .ws-hero p, .editorial-hero-content p, .alchemy-header p, .hero-content p, .contact-hero p { font-size: 1rem !important; }
      h2, .editorial-title, .pairing-title, .bento-title, .ws-step h2, .taste-matrix h2, .section-header h2 { font-size: 1.8rem !important; margin-bottom: 1rem !important; }
      h3, .info-card h3, .visit-info h3, .cta-banner h3 { font-size: 1.4rem !important; }
      
      /* Padding and Layouts */
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container, .contact-section { padding-top: 3rem !important; padding-bottom: 3rem !important; padding-left: 1.25rem !important; padding-right: 1.25rem !important; }
      
      /* Stack multi-column layouts universally */
      .pairing-section, .editorial-section, .ws-step, .bento-grid, .taste-matrix, .contact-grid, .contact-cards, .visit-card, .footer-container, .bento-item, .features-grid, .society-perks { 
          display: flex !important; 
          flex-direction: column !important; 
          gap: 2rem !important;
      }
      .pairing-section.reverse { flex-direction: column !important; }
      .matrix-col { width: 100% !important; margin-bottom: 1.5rem; }
      
      /* Fix form, map, cards */
      .visit-info, .contact-form-wrapper, .info-card { width: 100% !important; min-height: auto !important; padding: 1.5rem !important; }
      .form-image, .map-box { width: 100% !important; min-height: auto !important; padding: 0 !important; overflow: hidden; border-radius: 20px; }
      .form-image img, .map-box iframe, .map-box img { position: relative !important; height: 300px !important; width: 100% !important; display: block !important; object-fit: cover !important; }
      
      /* Fix Decorative Images in Contact */
      div[style*="display: flex; gap: 1rem; justify-content: center"] {
          flex-wrap: wrap !important;
      }
      div[style*="display: flex; gap: 1rem; justify-content: center"] img {
          width: calc(50% - 0.5rem) !important;
          height: 180px !important;
          margin-bottom: 1rem;
      }
      
      /* Image constraints */
      .pairing-visual img, .editorial-img-wrap img { height: auto !important; max-height: 350px; object-fit: cover; }
      
      /* Buttons */
      .btn-submit, .btn-secondary, button { width: 100% !important; text-align: center !important; }
      
      /* Adjust custom inline styles */
      div[style*="max-width: 1200px;"] { max-width: 100% !important; padding-left: 1rem !important; padding-right: 1rem !important; }
    }
    
    @media (max-width: 480px) {
      /* Smaller typography */
      h1, .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1, .contact-hero h1 { font-size: 1.8rem !important; }
      h2, .editorial-title, .pairing-title, .bento-title, .ws-step h2, .section-header h2 { font-size: 1.5rem !important; }
      h3 { font-size: 1.25rem !important; }
      p, .info-card p, .visit-info p, .form-label { font-size: 0.95rem !important; }
      
      /* Spacing */
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container, .contact-section { padding-top: 2rem !important; padding-bottom: 2rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
      .footer { padding: 2rem 1rem 1.5rem !important; }
      
      /* Contact specific fixes */
      .contact-hero { padding: 4rem 1rem !important; }
      .info-icon { width: 50px !important; height: 50px !important; font-size: 1.4rem !important; }
      
      /* Decor images strip - full width */
      div[style*="display: flex; gap: 1rem; justify-content: center"] img {
          width: 100% !important;
          height: 200px !important;
          margin-left: 0 !important;
          margin-right: 0 !important;
      }
    }

    @media (max-width: 320px) {
      /* Extra small devices */
      h1, .contact-hero h1 { font-size: 1.5rem !important; }
      h2, .section-header h2 { font-size: 1.3rem !important; }
      main, section, .contact-section { padding-left: 0.75rem !important; padding-right: 0.75rem !important; }
      .btn-submit, .btn-secondary { font-size: 0.9rem !important; padding: 0.8rem !important; }
    }
  </style>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it already has the old block, replace it
    pattern = r'<!-- GLOBAL RESPONSIVE SCALING.*?</style>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_css, content, flags=re.DOTALL)
    else:
        # Otherwise, insert right before </head>
        content = content.replace('</head>', '\n' + new_css + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied massive global responsive update to all pages.")
