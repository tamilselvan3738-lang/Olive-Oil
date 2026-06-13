import os

pages = [
    'Balsamic Vinegar Collection.html',
    'Flavor Profiles.html',
    'Gift Box Builder.html',
    'Pairing Recommendations.html'
]

override_style = """
  <!-- THEME OVERRIDE: FORCE OLIVE OIL COLLECTION COLORS -->
  <style id="theme-override">
    :root {
      --bg-main: #fefaf5;
      --text-main: #2c2418;
      --bg-surface: #ffffff;
      --border-light: #e9dfd3;
      --accent: #5f8b6f;
    }
    body.dark {
      --bg-main: #121212;
      --text-main: #ece8e0;
      --bg-surface: #1e1915;
      --border-light: #3a2e26;
    }

    body{ background-color: var(--bg-main) !important; color: var(--text-main) !important; }

    /* BALSAMIC */
    .balsamic-wrapper { background-color: transparent !important; border: none !important; box-shadow: none !important; }
    .hero-mock { background: var(--bg-surface) !important; }
    .lux-card { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }

    /* FLAVOR PROFILES */
    .editorial-container { background-color: transparent !important; }
    .editorial-hero { background: transparent !important; border: 1px solid var(--border-light) !important; box-shadow: none !important; }
    .editorial-hero-content h1, .editorial-hero-content p { color: #ffffff !important; text-shadow: 0 2px 10px rgba(0,0,0,0.8) !important; }
    .editorial-content-card { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .taste-matrix { background: transparent !important; border-color: var(--border-light) !important; }
    .matrix-col { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .editorial-title, .editorial-desc, .taste-matrix h2, .matrix-col h3 { color: var(--text-main) !important; }

    /* GIFT BOX BUILDER */
    .workshop-wrapper { background-color: transparent !important; }
    .ws-custom-box, .ws-corporate, .ws-gourmet, .ws-packaging, .ws-shipping { background-color: transparent !important; }
    .ws-step { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .ws-visualizer { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .ws-holiday { background-color: transparent !important; color: var(--text-main) !important; }
    .ws-holiday h2, .ws-holiday-desc, .ws-holiday-card h3, .ws-holiday-card p { color: var(--text-main) !important; }
    .ws-holiday-card { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .ws-corporate h2, .ws-corporate p, .ws-corporate li, .ws-gourmet h2, .ws-packaging h2, .ws-packaging-desc, .ws-shipping h2 { color: var(--text-main) !important; }
    .ws-pack-item { background: var(--bg-surface) !important; }
    .ws-pack-item-content h3 { color: var(--text-main) !important; }
    .ws-unboxing { background: var(--bg-surface) !important; color: var(--text-main) !important; border-top: 1px solid var(--border-light) !important; }
    .ws-unboxing h2, .ws-unboxing blockquote { color: var(--text-main) !important; }
    .ws-timeline-icon { background: var(--bg-surface) !important; box-shadow: 0 0 0 10px var(--bg-main) !important; }
    .ws-timeline-item h4 { color: var(--text-main) !important; }

    /* PAIRING RECOMMENDATIONS */
    .pr-container { background-color: transparent !important; }
    .bento-hero { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .bento-item { background: var(--bg-surface) !important; border-color: var(--border-light) !important; }
    .pr-title, .bento-title, .bento-desc { color: var(--text-main) !important; }
  </style>
"""

for file in pages:
    if not os.path.exists(file):
        print(f"Skipping {file}, not found.")
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing override if present
    start_idx = content.find('<!-- THEME OVERRIDE:')
    if start_idx != -1:
        end_idx = content.find('</style>', start_idx) + 8
        content = content[:start_idx] + content[end_idx:]

    head_end = content.find('</head>')
    if head_end != -1:
        content = content[:head_end] + override_style + content[head_end:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Applied theme override to {file}")
    else:
        print(f"Could not find </head> in {file}")

print("Done.")
