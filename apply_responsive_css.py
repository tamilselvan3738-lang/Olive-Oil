import glob

responsive_css = """
  <!-- GLOBAL RESPONSIVE SCALING (Aligned with about.html behavior) -->
  <style id="global-responsive-scaling">
    img { max-width: 100%; height: auto; }
    
    @media (max-width: 1024px) {
      h1 { font-size: clamp(2.5rem, 5vw, 4rem) !important; }
      .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1 { font-size: 3rem !important; }
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container { padding-left: 1.5rem !important; padding-right: 1.5rem !important; }
    }
    
    @media (max-width: 768px) {
      h1, .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1 { font-size: 2.2rem !important; margin-bottom: 1rem !important; }
      p, .ws-hero p, .editorial-hero-content p, .alchemy-header p, .hero-content p { font-size: 1rem !important; }
      h2, .editorial-title, .pairing-title, .bento-title, .ws-step h2, .taste-matrix h2 { font-size: 1.8rem !important; margin-bottom: 1rem !important; }
      
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container { padding-top: 3rem !important; padding-bottom: 3rem !important; padding-left: 1rem !important; padding-right: 1rem !important; }
      
      /* Stack multi-column layouts */
      .pairing-section, .editorial-section, .ws-step, .bento-grid, .taste-matrix { flex-direction: column !important; }
      .pairing-section.reverse { flex-direction: column !important; }
      .bento-grid { grid-template-columns: 1fr !important; }
      .matrix-col { width: 100% !important; margin-bottom: 1.5rem; }
      
      .pairing-visual img, .editorial-img-wrap img { height: auto !important; max-height: 350px; object-fit: cover; }
      
      .footer-container { grid-template-columns: 1fr !important; gap: 2rem !important; }
    }
    
    @media (max-width: 480px) {
      h1, .ws-hero h1, .editorial-hero-content h1, .alchemy-header h1, .about-hero h1, .hero-content h1 { font-size: 1.8rem !important; }
      h2, .editorial-title, .pairing-title, .bento-title, .ws-step h2 { font-size: 1.5rem !important; }
      main, section, .editorial-container, .alchemy-container, .workshop-wrapper, .pr-container { padding-top: 2.5rem !important; padding-bottom: 2.5rem !important; }
      .footer { padding: 2rem 1rem 1.5rem !important; }
    }
  </style>
"""

for filepath in glob.glob('*.html'):
    if filepath == 'about.html':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<style id="global-responsive-scaling">' in content:
        continue
        
    # Insert just before </head>
    content = content.replace('</head>', responsive_css + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected global responsive CSS into all pages.")
