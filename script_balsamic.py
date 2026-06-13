import os

with open('Balsamic Vinegar Collection.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = content.find('    /* ---------- DARK CELLAR THEME ---------- */')
css_end = content.find('  </style>', css_start)

new_css = """    /* ---------- BIANCO & ORO (WHITE & GOLD CASCADE) THEME ---------- */
    .balsamic-wrapper {
      background-color: #fdfcfb;
      color: #3e3227;
      padding: 3rem 1.5rem;
      border-radius: 3rem;
      border: 1px solid #f0e9df;
      box-shadow: 0 40px 100px rgba(0,0,0,0.03);
      position: relative;
    }
    body.dark .balsamic-wrapper { background-color: #1a1614; color: #f0e9df; border-color: #3a2e26; box-shadow: 0 40px 100px rgba(0,0,0,0.3); }

    @media (min-width: 768px) {
      .balsamic-wrapper { padding: 4rem; }
    }
    .balsamic-wrapper::before {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at top right, rgba(212, 184, 139, 0.1), transparent 50%); pointer-events: none; border-radius: 3rem;
    }

    .lux-grid { display: grid; grid-template-columns: 1fr; gap: 3rem; margin: 3rem 0; position: relative; z-index: 2; }
    @media (min-width: 768px) { .lux-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (min-width: 1024px) { .lux-grid { grid-template-columns: repeat(3, 1fr); gap: 4rem; } }
    
    .lux-card {
      background: #ffffff;
      border-radius: 1rem; overflow: hidden;
      box-shadow: 0 10px 40px rgba(212, 184, 139, 0.08);
      border: 1px solid #f2eee8;
      transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
      display: flex; flex-direction: column;
      position: relative;
    }
    body.dark .lux-card { background: #221c19; border-color: #362a21; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }

    .lux-card:hover {
      transform: translateY(-15px);
      box-shadow: 0 30px 60px rgba(212, 184, 139, 0.2);
      border-color: #d4b88b;
    }
    body.dark .lux-card:hover { box-shadow: 0 30px 60px rgba(212, 184, 139, 0.1); border-color: #d4b88b; }

    .lux-card-img-wrap { padding: 0.5rem; position: relative; }
    .lux-card img { width: 100%; height: 320px; object-fit: cover; border-radius: 0.8rem; transition: transform 0.8s ease; }
    .lux-card:hover img { transform: scale(1.04); }
    
    .lux-card-body{ padding: 2rem 2.5rem 3rem; text-align: center; flex-grow: 1; display: flex; flex-direction: column; position: relative; }
    .lux-card-body::before { content: ''; width: 40px; height: 2px; background: #d4b88b; position: absolute; top: 0; left: 50%; transform: translateX(-50%); }

    .lux-card-title { font-size: 1.7rem; font-weight: 300; color: #2c241c; margin-top: 1rem; margin-bottom: 0.8rem; font-family: 'Times New Roman', serif; letter-spacing: 1px; }
    body.dark .lux-card-title { color: #f0e9df; }
    .lux-card-text { font-size: 0.95rem; color: #7a6e61; line-height: 1.7; margin-bottom: 2rem; flex-grow: 1; font-weight: 300; }
    body.dark .lux-card-text { color: #b8a695; }
    
    .lux-btn {
      align-self: center; background: #ffffff; color: #d4b88b; border: 1px solid #d4b88b;
      padding: 0.8rem 2.5rem; border-radius: 50px; font-weight: 600; text-decoration: none;
      transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 2px; font-size: 0.75rem;
    }
    body.dark .lux-btn { background: #221c19; }
    .lux-btn:hover { background: #d4b88b; color: #ffffff; box-shadow: 0 10px 20px rgba(212, 184, 139, 0.3); }

    .lux-section { display: flex; flex-direction: column; gap: 4rem; margin: 8rem 0; align-items: center; position: relative; z-index: 2; }
    @media (min-width: 900px) {
      .lux-section { flex-direction: row; gap: 6rem; }
      .lux-section:nth-of-type(even) { flex-direction: row-reverse; }
    }
    .lux-section-content { flex: 1; padding: 2rem; }
    .lux-section-img { flex: 1; position: relative; }
    .lux-section-img::before {
      content: ''; position: absolute; top: 20px; left: -20px; right: 20px; bottom: -20px;
      background: #fdfcfb; border: 1px solid #d4b88b; border-radius: 2rem; z-index: -1; transition: transform 0.5s ease;
    }
    body.dark .lux-section-img::before { background: #1a1614; }
    .lux-section:hover .lux-section-img::before { transform: translate(15px, -15px); }
    .lux-section-img img { width: 100%; height: 450px; object-fit: cover; border-radius: 2rem; box-shadow: 0 20px 50px rgba(0,0,0,0.08); }
    
    .lux-tag { display: inline-block; color: #d4b88b; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 1.5rem; border-bottom: 1px solid #d4b88b; padding-bottom: 6px; }
    .lux-heading { font-size: 3rem; font-weight: 300; color: #2c241c; margin-bottom: 1.5rem; line-height: 1.2; font-family: 'Times New Roman', serif; }
    body.dark .lux-heading { color: #f0e9df; }
    .lux-paragraph { font-size: 1.1rem; color: #7a6e61; line-height: 1.9; margin-bottom: 1.8rem; font-weight: 300; }
    body.dark .lux-paragraph { color: #b8a695; }
    .lux-divider { text-align: center; margin: 6rem 0; opacity: 0.6; }
    .lux-divider i { color: #d4b88b; font-size: 2rem; }
"""
content = content[:css_start] + new_css + content[css_end:]

# Replace HTML Hero
hero_start = content.find('<div class="hero-mock"')
hero_end = content.find('</div>', content.find('</div>', hero_start) + 1) + 6

new_hero = """<div class="hero-mock" style="margin-bottom: 5rem; padding: 6rem 2rem; border-radius: 2rem; background: #ffffff; border: 1px solid #f0e9df; box-shadow: 0 30px 60px rgba(212,184,139,0.05); position: relative; overflow: hidden; text-align: center;">
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 100%; background: linear-gradient(135deg, rgba(253,252,251,1), rgba(242,238,232,0.6)); pointer-events: none; z-index: 0;"></div>
    <div style="position: relative; z-index: 1;">
      <h2 style="font-size: 4rem; font-weight: 300; color: #d4b88b; font-family: 'Times New Roman', serif; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 1.5rem;">Aged to Perfection</h2>
      <p style="font-size: 1.25rem; max-width: 650px; margin: 0 auto; color: #7a6e61; line-height: 1.8; font-weight: 300;">Discover our artisanal collection of Balsamic Vinegars from Modena. Complex, rich, and naturally aged in traditional wooden barrels for an exquisite culinary experience.</p>
    </div>
  </div>"""

content = content[:hero_start] + new_hero + content[hero_end:]

# Also update the Mixology banner at the bottom to match the new style
mixology_start = content.find('<div style="background: linear-gradient(135deg, rgba(31,27,22,0.95)')
if mixology_start != -1:
    mixology_end = content.find('</div>', content.find('</div>', content.find('</div>', mixology_start) + 1) + 1) + 6
    new_mixology = """<div style="background: linear-gradient(135deg, rgba(253,252,251,0.95), rgba(242,238,232,0.95)), url('images/balsamic_mixology.png'); background-size: cover; background-position: center; border-radius: 2.5rem; padding: 8rem 2rem; text-align: center; margin: 6rem 0; color: #2c241c; box-shadow: 0 30px 80px rgba(212,184,139,0.1); border: 1px solid #f0e9df; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at center, transparent, rgba(255,255,255,0.7)); z-index: 0;"></div>
    <div style="position: relative; z-index: 1;">
      <span class="lux-tag" style="background: transparent; color: #d4b88b; border-bottom: 1px solid #d4b88b;">Mixology</span>
      <h2 style="font-size: 3.5rem; margin: 1.5rem 0; color: #2c241c; font-weight: 300; font-family: 'Times New Roman', serif; letter-spacing: 2px;">Balsamic Mixology</h2>
      <p style="font-size: 1.2rem; opacity: 0.9; max-width: 650px; margin: 0 auto 3rem; line-height: 1.8; font-weight: 300; color: #7a6e61;">Redefine happy hour. A splash of fruit-infused white balsamic adds a brilliant tartness and complexity to sparkling water, gin botanicals, or bourbon smash cocktails.</p>
      <a href="#" class="lux-btn" style="background-color: #d4b88b; color: #ffffff; border-color: #d4b88b;">View Cocktail Recipes</a>
    </div>
  </div>"""
    content = content[:mixology_start] + new_mixology + content[mixology_end:]


with open('Balsamic Vinegar Collection.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully applied Bianco & Oro design.')
