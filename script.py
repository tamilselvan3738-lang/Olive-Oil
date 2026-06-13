import os

with open('Flavor Profiles.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = content.find('    /* ---------- FLAVOR PROFILES DESIGN ---------- */')
css_end = content.find('  </style>', css_start)

new_css = """    /* ---------- OVERLAPPING EDITORIAL DESIGN ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&display=swap');

    .editorial-container { max-width: 1400px; margin: 0 auto; padding: 0 1.25rem; width: 100%; overflow: hidden; }
    @media (min-width: 768px) { .editorial-container { padding: 0 2rem; } }

    .editorial-hero {
      position: relative; padding: 8rem 2rem; text-align: center; border-radius: 2rem; margin: 2rem 0 6rem;
      background: #e9dfd3; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center;
      box-shadow: inset 0 0 50px rgba(0,0,0,0.05);
    }
    .editorial-hero-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; filter: saturate(1.2) brightness(0.9); }
    .editorial-hero-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(44,36,24,0.3), rgba(31,27,22,0.8)); z-index: 2; }
    .editorial-hero-content { position: relative; z-index: 3; max-width: 800px; color: #ffffff; }
    .editorial-hero h1 { font-size: 4rem; font-family: 'Playfair Display', serif; font-weight: 700; margin-bottom: 1.5rem; letter-spacing: -1px; }
    .editorial-hero p { font-size: 1.25rem; font-weight: 300; opacity: 0.95; line-height: 1.7; }
    @media (max-width: 768px) { .editorial-hero h1 { font-size: 2.8rem; } }

    .editorial-section { display: flex; flex-direction: column; align-items: center; margin: 8rem 0; position: relative; }
    @media (min-width: 992px) {
      .editorial-section { flex-direction: row; justify-content: center; align-items: stretch; }
      .editorial-section.reverse { flex-direction: row-reverse; }
    }
    
    .editorial-img-box { width: 100%; max-width: 650px; position: relative; z-index: 1; }
    .editorial-img-box img { width: 100%; height: 650px; object-fit: cover; border-radius: 1.5rem; box-shadow: 0 30px 60px rgba(0,0,0,0.15); transition: transform 0.6s ease; }
    .editorial-img-box:hover img { transform: scale(1.02); }
    .editorial-img-box::after {
      content: ''; position: absolute; top: 2.5rem; bottom: -2.5rem; left: 2.5rem; right: -2.5rem;
      border: 1px solid #5f8b6f; border-radius: 1.5rem; z-index: -1; transition: all 0.5s ease;
    }
    .editorial-section.reverse .editorial-img-box::after { left: -2.5rem; right: 2.5rem; }
    body.dark .editorial-img-box::after { border-color: #8fbc9f; }
    .editorial-img-box:hover::after { top: 1.5rem; bottom: -1.5rem; left: 1.5rem; right: -1.5rem; }
    .editorial-section.reverse .editorial-img-box:hover::after { top: 1.5rem; bottom: -1.5rem; left: -1.5rem; right: 1.5rem; }
    
    .editorial-content-card {
      background: #ffffff; padding: 4rem 3rem; border-radius: 1.5rem; box-shadow: 0 25px 50px rgba(0,0,0,0.06);
      max-width: 550px; margin-top: -4rem; position: relative; z-index: 2; border: 1px solid #f0e8df;
    }
    body.dark .editorial-content-card { background: #1e1915; box-shadow: 0 25px 50px rgba(0,0,0,0.4); border-color: #3a2e26; }
    @media (min-width: 992px) {
      .editorial-content-card { margin-top: 4rem; margin-left: -8rem; align-self: center; }
      .editorial-section.reverse .editorial-content-card { margin-left: 0; margin-right: -8rem; }
    }
    
    .editorial-tag { font-family: 'Playfair Display', serif; font-style: italic; color: #5f8b6f; font-size: 1.3rem; margin-bottom: 0.8rem; display: block; }
    body.dark .editorial-tag { color: #8fbc9f; }
    .editorial-title { font-size: 2.8rem; font-weight: 800; color: #2c2418; margin-bottom: 1.5rem; letter-spacing: -1px; line-height: 1.1; }
    body.dark .editorial-title { color: #f0e9df; }
    .editorial-desc { font-size: 1.1rem; color: #6b5a48; line-height: 1.8; margin-bottom: 2.5rem; }
    body.dark .editorial-desc { color: #c7b59b; }
    
    .editorial-notes { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; border-top: 1px solid #e9dfd3; padding-top: 2rem; margin-bottom: 2.5rem; }
    body.dark .editorial-notes { border-top-color: #3a2e26; }
    .editorial-note { display: flex; align-items: center; gap: 12px; font-weight: 600; font-size: 0.95rem; color: #3e2c1c; }
    body.dark .editorial-note { color: #f0e9df; }
    .editorial-note i { color: #5f8b6f; font-size: 1.4rem; }
    body.dark .editorial-note i { color: #8fbc9f; }

    .editorial-btn {
      display: inline-flex; align-items: center; gap: 8px; font-weight: 600; font-size: 0.9rem;
      color: #ffffff; background-color: #2c2418; padding: 1rem 2rem; border-radius: 50px; text-decoration: none;
      transition: all 0.3s ease; border: 1px solid #2c2418;
    }
    .editorial-btn:hover { background-color: #5f8b6f; border-color: #5f8b6f; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(95, 139, 111, 0.2); }
    body.dark .editorial-btn { background-color: #d4c3aa; color: #121212; border-color: #d4c3aa; }
    body.dark .editorial-btn:hover { background-color: #8fbc9f; border-color: #8fbc9f; box-shadow: 0 10px 20px rgba(143, 188, 159, 0.2); }

    .taste-matrix { background: #fdfaf6; border-radius: 2rem; padding: 5rem 2rem; box-shadow: inset 0 0 30px rgba(0,0,0,0.02); margin: 8rem 0; border: 1px solid #ede5db; text-align: center; }
    body.dark .taste-matrix { background: #1a1613; border-color: #3a2e26; box-shadow: inset 0 0 30px rgba(0,0,0,0.2); }
    .taste-matrix h2 { font-size: 3rem; font-family: 'Playfair Display', serif; color: #2c2418; margin-bottom: 4rem; font-weight: 800; }
    body.dark .taste-matrix h2 { color: #f0e9df; }
    .matrix-grid { display: grid; grid-template-columns: 1fr; gap: 2rem; }
    @media (min-width: 768px) { .matrix-grid { grid-template-columns: repeat(3, 1fr); } }
    .matrix-col { padding: 3rem 2rem; border-radius: 1.5rem; background: #ffffff; border: 1px solid #f0e8df; transition: transform 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.03); }
    body.dark .matrix-col { background: #1e1915; border-color: #3a2e26; }
    .matrix-col:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(95, 139, 111, 0.08); border-color: #5f8b6f; }
    .matrix-col h3 { font-size: 1.6rem; color: #2c2418; margin-bottom: 1rem; font-family: 'Playfair Display', serif; }
    body.dark .matrix-col h3 { color: #f0e9df; }
    .matrix-icon { font-size: 2.8rem; color: #5f8b6f; margin-bottom: 1.5rem; }
    .matrix-list { list-style: none; padding: 0; text-align: left; margin-top: 2rem; border-top: 1px solid #f0e8df; padding-top: 1.5rem; }
    body.dark .matrix-list { border-top-color: #3a2e26; }
    .matrix-list li { margin-bottom: 1rem; font-size: 1rem; color: #5a4a38; display: flex; align-items: flex-start; gap: 10px; }
    body.dark .matrix-list li { color: #c7b59b; }
    .matrix-list li i { color: #5f8b6f; margin-top: 5px; font-size: 0.9rem; }

    .editorial-banner { position: relative; border-radius: 2rem; overflow: hidden; margin: 8rem 0; padding: 8rem 2rem; text-align: center; }
    .editorial-banner-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; filter: brightness(0.9); }
    .editorial-banner-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(44,36,24,0.9), rgba(95,139,111,0.8)); z-index: 2; }
    .editorial-banner-content { position: relative; z-index: 3; color: white; max-width: 800px; margin: 0 auto; }
    .editorial-banner-content h2 { font-size: 3.5rem; font-family: 'Playfair Display', serif; font-weight: 800; margin-bottom: 1.5rem; line-height: 1.1; }
    .editorial-banner-content p { font-size: 1.25rem; opacity: 0.95; line-height: 1.7; margin-bottom: 2.5rem; font-weight: 300; }
"""
content = content[:css_start] + new_css + content[css_end:]

# Replace HTML
html_start = content.find('<main class="fp-container"')
html_end = content.find('</main>') + 7

new_html = """<main class="editorial-container" style="margin-top: 4rem;">
  
  <!-- 1. Hero Section -->
  <div class="editorial-hero">
    <img src="images/flavor_hero.png" alt="Flavor Profiles Spread" class="editorial-hero-img">
    <div class="editorial-hero-overlay"></div>
    <div class="editorial-hero-content">
      <h1>The Language of Taste</h1>
      <p>From the delicate buttery notes of a mild olive oil to the intense, peppery finish of a robust harvest. Discover the nuanced flavor profiles that define our premium collection.</p>
    </div>
  </div>

  <!-- 2. Mild & Delicate Section -->
  <div class="editorial-section">
    <div class="editorial-img-box">
      <img src="images/mild_delicate.png" alt="Mild and Delicate Olive Oil">
    </div>
    <div class="editorial-content-card">
      <span class="editorial-tag">The Gentle Touch</span>
      <h2 class="editorial-title">Mild & Delicate</h2>
      <p class="editorial-desc">Smooth, buttery, and incredibly light on the palate. Our mild profiles are crafted from late-harvest olives that yield a tender, unobtrusive flavor, making it the perfect foundation for subtle dishes.</p>
      <div class="editorial-notes">
        <div class="editorial-note"><i class="fas fa-leaf"></i> Sweet Almond</div>
        <div class="editorial-note"><i class="fas fa-apple-alt"></i> Ripe Banana</div>
        <div class="editorial-note"><i class="fas fa-seedling"></i> Chamomile</div>
        <div class="editorial-note"><i class="fas fa-wind"></i> Soft Finish</div>
      </div>
      <a href="#" class="editorial-btn">Shop Delicate Oils <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

  <!-- 3. Fruity & Sweet Section -->
  <div class="editorial-section reverse">
    <div class="editorial-img-box">
      <img src="images/fruity_sweet.png" alt="Fruity and Sweet Profile">
    </div>
    <div class="editorial-content-card">
      <span class="editorial-tag">Nature's Candy</span>
      <h2 class="editorial-title">Fruity & Sweet</h2>
      <p class="editorial-desc">Vibrant, lively, and brimming with fresh orchard aromas. These oils and young vinegars offer a pleasant sweetness balanced by a mild tang, bringing an immediate brightness to your culinary creations.</p>
      <div class="editorial-notes">
        <div class="editorial-note"><i class="fas fa-apple-whole"></i> Green Apple</div>
        <div class="editorial-note"><i class="fas fa-lemon"></i> Citrus Zest</div>
        <div class="editorial-note"><i class="fas fa-pepper-hot"></i> Mild Tomato</div>
        <div class="editorial-note"><i class="fas fa-sun"></i> Bright Acid</div>
      </div>
      <a href="#" class="editorial-btn">Shop Fruity Notes <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

  <!-- 4. Robust & Peppery Section -->
  <div class="editorial-section">
    <div class="editorial-img-box">
      <img src="images/robust_peppery.png" alt="Robust and Peppery Olive Oil">
    </div>
    <div class="editorial-content-card">
      <span class="editorial-tag">The Bold Statement</span>
      <h2 class="editorial-title">Robust & Peppery</h2>
      <p class="editorial-desc">Pressed from early-harvest green olives, these oils pack a powerful punch. High in antioxidants, they deliver a sharp, lingering peppery finish at the back of the throat—a true sign of premium quality.</p>
      <div class="editorial-notes">
        <div class="editorial-note"><i class="fas fa-leaf"></i> Fresh Cut Grass</div>
        <div class="editorial-note"><i class="fas fa-fire"></i> Black Pepper</div>
        <div class="editorial-note"><i class="fas fa-spa"></i> Artichoke Leaf</div>
        <div class="editorial-note"><i class="fas fa-bolt"></i> High Polyphenols</div>
      </div>
      <a href="#" class="editorial-btn">Shop Robust Oils <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

  <!-- 5. Rich & Aged Section -->
  <div class="editorial-section reverse">
    <div class="editorial-img-box">
      <img src="images/rich_aged.png" alt="Rich and Aged Balsamic">
    </div>
    <div class="editorial-content-card">
      <span class="editorial-tag">Time-Honored</span>
      <h2 class="editorial-title">Rich & Aged</h2>
      <p class="editorial-desc">Thick, syrupy, and exceptionally complex. Aged for decades in wooden barrels, these vinegars possess a deep caramelized sweetness with underlying woody notes that elevate both savory meats and sweet desserts.</p>
      <div class="editorial-notes">
        <div class="editorial-note"><i class="fas fa-tree"></i> Oak & Cherry Wood</div>
        <div class="editorial-note"><i class="fas fa-cookie"></i> Dark Caramel</div>
        <div class="editorial-note"><i class="fas fa-wine-glass"></i> Ripe Fig</div>
        <div class="editorial-note"><i class="fas fa-droplet"></i> Syrupy Texture</div>
      </div>
      <a href="#" class="editorial-btn">Shop Aged Reserves <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

  <!-- 6. Flavor Comparison Guide Section -->
  <div class="taste-matrix">
    <h2>Flavor Comparison Guide</h2>
    <div class="matrix-grid">
      <div class="matrix-col">
        <div class="matrix-icon"><i class="fas fa-droplet"></i></div>
        <h3>Light & Delicate</h3>
        <p style="font-size: 1.05rem; opacity: 0.8; margin-bottom: 1rem;">Best for baking, subtle sauces, and mild fish.</p>
        <ul class="matrix-list">
          <li><i class="fas fa-check"></i> Minimal bitterness</li>
          <li><i class="fas fa-check"></i> Buttery mouthfeel</li>
          <li><i class="fas fa-check"></i> Pale golden color</li>
          <li><i class="fas fa-check"></i> Ripe harvest olives</li>
        </ul>
      </div>
      <div class="matrix-col" style="border-color: #5f8b6f; box-shadow: 0 20px 50px rgba(95, 139, 111, 0.1);">
        <div class="matrix-icon"><i class="fas fa-leaf"></i></div>
        <h3>Medium & Fruity</h3>
        <p style="font-size: 1.05rem; opacity: 0.8; margin-bottom: 1rem;">Best for everyday use, salads, and chicken.</p>
        <ul class="matrix-list">
          <li><i class="fas fa-check"></i> Balanced pungency</li>
          <li><i class="fas fa-check"></i> Fresh herbaceous aroma</li>
          <li><i class="fas fa-check"></i> Yellow-green hue</li>
          <li><i class="fas fa-check"></i> Mixed harvest olives</li>
        </ul>
      </div>
      <div class="matrix-col">
        <div class="matrix-icon"><i class="fas fa-fire-burner"></i></div>
        <h3>Intense & Robust</h3>
        <p style="font-size: 1.05rem; opacity: 0.8; margin-bottom: 1rem;">Best for steaks, stews, and finishing heavy dishes.</p>
        <ul class="matrix-list">
          <li><i class="fas fa-check"></i> Strong peppery finish</li>
          <li><i class="fas fa-check"></i> High polyphenol count</li>
          <li><i class="fas fa-check"></i> Deep emerald green</li>
          <li><i class="fas fa-check"></i> Early harvest olives</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 7. Tasting Techniques Section -->
  <div class="editorial-banner">
    <img src="images/tasting_technique.png" alt="Tasting Techniques" class="editorial-banner-img">
    <div class="editorial-banner-overlay"></div>
    <div class="editorial-banner-content">
      <h2>The Sommelier's Approach</h2>
      <p>True tasting requires engaging all the senses. Warm the tasting glass in the palm of your hand to release the volatile aromas. Inhale deeply, taking note of grass, fruit, or pepper. Finally, take a small sip and draw air sharply through your teeth—a technique called "strippaggio"—to spread the oil across your palate and experience the full spectrum of its flavor profile.</p>
      <a href="#" class="editorial-btn" style="background: transparent; border-color: white; color: white;">Watch Tasting Guide <i class="fas fa-play-circle"></i></a>
    </div>
  </div>

  <!-- 8. Culinary Applications Section -->
  <div class="editorial-section">
    <div class="editorial-img-box">
      <img src="images/culinary_applications.png" alt="Culinary Applications">
    </div>
    <div class="editorial-content-card">
      <span class="editorial-tag">In The Kitchen</span>
      <h2 class="editorial-title">Mastering Pairings</h2>
      <p class="editorial-desc">Knowing your flavor profiles transforms cooking from a routine into an art form. Match intensities: pair robust oils with hearty winter greens and grilled red meats, while reserving delicate oils for tender white fish, fresh mozzarella, or even a citrus olive oil cake.</p>
      <div class="editorial-notes" style="grid-template-columns: 1fr; border: none; padding-top: 0; margin-bottom: 1.5rem;">
        <div class="editorial-note" style="background: rgba(95, 139, 111, 0.1); padding: 1rem; border-radius: 8px;"><i class="fas fa-utensils"></i> Elevate Everyday Meals</div>
        <div class="editorial-note" style="background: rgba(95, 139, 111, 0.1); padding: 1rem; border-radius: 8px;"><i class="fas fa-wine-bottle"></i> Substitute Butter Seamlessly</div>
      </div>
      <a href="#" class="editorial-btn">Explore Recipe Blog <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

</main>"""

content = content[:html_start] + new_html + content[html_end:]

with open('Flavor Profiles.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('flavor.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully applied Overlapping Editorial design.')
