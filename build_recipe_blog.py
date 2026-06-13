import os

# Read the original file
with open('Recipe Blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new HTML content for the Recipe Blog
new_html = """
<!-- 1. Hero Section -->
<section class="recipe-hero" style="background: url('images/recipe_hero.png') center/cover no-repeat; position: relative; padding: 10rem 2rem; text-align: center; color: white;">
  <div style="position: absolute; top:0; left:0; right:0; bottom:0; background: rgba(44, 36, 24, 0.6); z-index: 1;"></div>
  <div style="position: relative; z-index: 2; max-width: 800px; margin: 0 auto;">
    <h1 style="font-size: 3.5rem; font-family: 'Playfair Display', serif; font-weight: 700; margin-bottom: 1rem;">The Artisan's Kitchen</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Discover culinary inspiration. Elevate your everyday cooking with our premium olive oils and aged balsamic vinegars.</p>
  </div>
</section>

<!-- 2. Featured Recipe -->
<section class="container" style="margin-top: 5rem; margin-bottom: 5rem;">
  <div class="featured-recipe-card">
    <div class="featured-recipe-image-wrap">
      <img src="images/recipe_featured.png" alt="Blood Orange Olive Oil Cake">
    </div>
    <div class="featured-recipe-text-wrap">
      <span class="badge" style="margin-bottom: 1rem;">Recipe of the Month</span>
      <h2 style="font-size: 2.5rem; color: #2c2418; margin-bottom: 1rem; line-height: 1.2;">Blood Orange Olive Oil Cake</h2>
      <p style="color: #6b5a48; margin-bottom: 1.5rem; font-size: 1.05rem;">An incredibly moist, tender cake that celebrates citrus season. Our mild extra virgin olive oil replaces butter to create a delicate crumb, while a fresh blood orange glaze adds the perfect bright finish.</p>
      <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
        <span style="font-size: 0.9rem; color: #5f8b6f;"><i class="far fa-clock"></i> 55 Mins</span>
        <span style="font-size: 0.9rem; color: #5f8b6f;"><i class="fas fa-signal"></i> Intermediate</span>
      </div>
      <a href="#" class="btn-primary">View Full Recipe</a>
    </div>
  </div>
</section>

<!-- 3. Appetizers -->
<section class="container" style="margin-bottom: 5rem;">
  <div style="text-align: center; margin-bottom: 3rem;">
    <h2 class="section-title">Appetizers & Starters</h2>
    <p style="color: #6b5a48; max-width: 600px; margin: 0 auto;">Set the stage for a memorable meal with these elegant, flavor-forward small bites.</p>
  </div>
  <div class="three-cards-grid">
    <div class="feature-card" style="padding: 0; text-align: left;">
      <img src="images/recipe_app_crostini.png" alt="Burrata Crostini" style="width: 100%; height: 250px; object-fit: cover;">
      <div style="padding: 1.5rem;">
        <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Burrata & Fig Balsamic Crostini</h3>
        <p style="color: #6b5a48; font-size: 0.9rem; margin-bottom: 1rem;">Crispy baguette slices topped with creamy burrata, fresh figs, and our dark aged balsamic.</p>
        <a href="#" style="color: #5f8b6f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
    <div class="feature-card" style="padding: 0; text-align: left;">
      <img src="images/recipe_app_tart.png" alt="Onion Tart" style="width: 100%; height: 250px; object-fit: cover;">
      <div style="padding: 1.5rem;">
        <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Caramelized Onion & Thyme Tart</h3>
        <p style="color: #6b5a48; font-size: 0.9rem; margin-bottom: 1rem;">A savory, flaky tart using our robust olive oil to deeply caramelize sweet onions.</p>
        <a href="#" style="color: #5f8b6f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
    <div class="feature-card" style="padding: 0; text-align: left;">
      <img src="images/pairing_hearth.png" alt="Olive Tapenade" style="width: 100%; height: 250px; object-fit: cover;">
      <div style="padding: 1.5rem;">
        <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Rustic Olive Tapenade</h3>
        <p style="color: #6b5a48; font-size: 0.9rem; margin-bottom: 1rem;">A classic Mediterranean spread elevated with our garlic-infused extra virgin olive oil.</p>
        <a href="#" style="color: #5f8b6f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- 4. Main Courses -->
<section style="background-color: #f7efe7; padding: 5rem 0; margin-bottom: 5rem;">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <h2 class="section-title" style="margin-top: 0;">Hearty Main Courses</h2>
      <p style="color: #6b5a48; max-width: 600px; margin: 0 auto;">Transform simple proteins and pastas into restaurant-quality dishes.</p>
    </div>
    <div class="two-columns">
      <div class="info-image">
        <img src="images/pairing_mediterranean.png" alt="Herb-Crusted Salmon" style="box-shadow: 0 15px 30px rgba(0,0,0,0.1);">
      </div>
      <div class="info-text">
        <span class="badge" style="background: white; margin-bottom: 1rem;">Seafood</span>
        <h3 style="font-size: 2rem; margin-bottom: 1rem; color: #2c2418;">Herb-Crusted Salmon with Lemon Olive Oil</h3>
        <p style="color: #6b5a48; margin-bottom: 1.5rem; line-height: 1.7;">A bright and fresh weeknight dinner. We use our lemon-infused olive oil to create a vibrant marinade that seals in the salmon's moisture, pairing perfectly with a crispy herb topping.</p>
        <a href="#" class="btn-primary">View Full Recipe</a>
      </div>
    </div>
  </div>
</section>

<!-- 5. Healthy Recipes -->
<section class="container" style="margin-bottom: 5rem;">
  <div style="text-align: center; margin-bottom: 3rem;">
    <h2 class="section-title">Healthy Recipes & Greens</h2>
    <p style="color: #6b5a48; max-width: 600px; margin: 0 auto;">Nourish your body with fresh salads and grain bowls.</p>
  </div>
  <div class="two-cards-grid">
    <div style="position: relative; border-radius: 1.5rem; overflow: hidden; height: 350px;">
      <img src="images/pairing_orchard.png" alt="Healthy Salad" style="width: 100%; height: 100%; object-fit: cover;">
      <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white;">
        <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Summer Peach & Prosciutto Salad</h3>
        <p style="opacity: 0.9; font-size: 0.9rem;">Drizzled with Aged Dark Balsamic</p>
      </div>
    </div>
    <div style="position: relative; border-radius: 1.5rem; overflow: hidden; height: 350px;">
      <img src="images/bal_white1.png" alt="Quinoa Bowl" style="width: 100%; height: 100%; object-fit: cover;">
      <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white;">
        <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Mediterranean Quinoa Bowl</h3>
        <p style="opacity: 0.9; font-size: 0.9rem;">With White Balsamic Vinaigrette</p>
      </div>
    </div>
  </div>
</section>

<!-- 6. Desserts -->
<section style="background-color: #2c2418; color: #fefaf5; padding: 5rem 0; margin-bottom: 5rem;">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3rem;">
      <h2 class="section-title" style="margin-top: 0; color: #fefaf5;">Decadent Desserts</h2>
      <p style="color: #c7b59b; max-width: 600px; margin: 0 auto;">Yes, olive oil belongs in desserts! Discover incredibly moist cakes and rich brownies.</p>
    </div>
    <div class="three-cards-grid">
      <div class="feature-card" style="background: #1f1b16; border-color: #3a2e26; padding: 0; text-align: left;">
        <img src="images/bal_fruit_main.png" alt="Fruit Dessert" style="width: 100%; height: 250px; object-fit: cover;">
        <div style="padding: 1.5rem;">
          <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem; color: #fefaf5;">Balsamic Macerated Berries</h3>
          <p style="color: #c7b59b; font-size: 0.9rem; margin-bottom: 1rem;">Fresh strawberries and raspberries naturally sweetened with our thick, syrupy dark balsamic over vanilla bean ice cream.</p>
          <a href="#" style="color: #8fbc9f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="feature-card" style="background: #1f1b16; border-color: #3a2e26; padding: 0; text-align: left;">
        <img src="images/infused_olive_oils.png" alt="Olive Oil Brownies" style="width: 100%; height: 250px; object-fit: cover;">
        <div style="padding: 1.5rem;">
          <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem; color: #fefaf5;">Dark Chocolate Sea Salt Brownies</h3>
          <p style="color: #c7b59b; font-size: 0.9rem; margin-bottom: 1rem;">Replacing butter with our robust olive oil creates the fudgiest texture and enhances the rich cocoa flavor.</p>
          <a href="#" style="color: #8fbc9f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="feature-card" style="background: #1f1b16; border-color: #3a2e26; padding: 0; text-align: left;">
        <img src="images/tasting_experience.png" alt="Olive Oil Cookies" style="width: 100%; height: 250px; object-fit: cover;">
        <div style="padding: 1.5rem;">
          <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem; color: #fefaf5;">Lemon Olive Oil Biscotti</h3>
          <p style="color: #c7b59b; font-size: 0.9rem; margin-bottom: 1rem;">Crispy, twice-baked Italian cookies made completely dairy-free with our citrus-infused oil.</p>
          <a href="#" style="color: #8fbc9f; text-decoration: none; font-weight: 600; font-size: 0.9rem;">Get Recipe <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 7. Chef's Tips -->
<section class="container" style="margin-bottom: 5rem;">
  <div class="two-columns">
    <div class="info-text">
      <h2 class="section-title" style="text-align: left; margin-top: 0;">Chef's Tips & Techniques</h2>
      <p style="color: #6b5a48; margin-bottom: 1.5rem; line-height: 1.7;">Mastering the basics is the first step to culinary excellence. Our executive chef shares insider knowledge on how to get the most out of your premium oils and vinegars.</p>
      <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem;">
        <li style="display: flex; gap: 1rem; align-items: flex-start;">
          <i class="fas fa-fire" style="color: #5f8b6f; margin-top: 5px;"></i>
          <div>
            <strong>Understanding Smoke Points:</strong> Extra virgin olive oil is perfectly safe for sautéing and roasting up to 400°F (204°C).
          </div>
        </li>
        <li style="display: flex; gap: 1rem; align-items: flex-start;">
          <i class="fas fa-blender" style="color: #5f8b6f; margin-top: 5px;"></i>
          <div>
            <strong>The Perfect Emulsion:</strong> The golden ratio for vinaigrettes is 3 parts oil to 1 part vinegar. Add a dab of mustard to keep it stable!
          </div>
        </li>
        <li style="display: flex; gap: 1rem; align-items: flex-start;">
          <i class="fas fa-spoon" style="color: #5f8b6f; margin-top: 5px;"></i>
          <div>
            <strong>Finishing Oils:</strong> Reserve your most robust, high-polyphenol oils solely for finishing dishes off the heat to preserve their flavor.
          </div>
        </li>
      </ul>
    </div>
    <div class="info-image">
      <img src="images/chefs_corner.png" alt="Chef Tips" style="border-radius: 1.5rem; box-shadow: 0 15px 30px rgba(0,0,0,0.1);">
    </div>
  </div>
</section>

<!-- 8. Newsletter CTA -->
<section style="background: linear-gradient(135deg, #e9dfd3, #f7efe7); padding: 5rem 1.25rem; text-align: center; border-radius: 2rem; max-width: 1200px; margin: 0 auto 5rem; border: 1px solid #e2d6ca;">
  <i class="fas fa-envelope-open-text" style="font-size: 2.5rem; color: #5f8b6f; margin-bottom: 1.5rem;"></i>
  <h2 style="font-size: 2.2rem; color: #2c2418; margin-bottom: 1rem;">Join the Recipe Club</h2>
  <p style="color: #6b5a48; max-width: 500px; margin: 0 auto 2rem;">Get weekly culinary inspiration, seasonal recipes, and exclusive access to new harvest releases sent directly to your inbox.</p>
  <form class="newsletter-form">
    <input type="email" placeholder="Enter your email address" required>
    <button type="submit" class="btn-primary">Subscribe</button>
  </form>
</section>
"""

# Replace content
start_marker = '<div class="menu-overlay" id="menuOverlay"></div>'
end_marker = '<!-- FOOTER WITH SAME NAVBAR DESIGN, COLORS, FONTS, STYLES -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_file_content = content[:start_idx + len(start_marker)] + "\n\n<main>\n" + new_html + "\n</main>\n\n" + content[end_idx:]
    with open('Recipe Blog.html', 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    print("Recipe Blog.html updated successfully!")
else:
    print("Error: Could not find markers in the file.")
