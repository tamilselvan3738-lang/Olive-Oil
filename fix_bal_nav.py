import os

file_bal = 'Balsamic Vinegar Collection.html'
file_nav = 'navbar.html'

with open(file_nav, 'r', encoding='utf-8') as f:
    nav_content = f.read()
    
nav_style_start = nav_content.find('<style>') + 7
nav_style_end = nav_content.find('</style>')
nav_css = nav_content[nav_style_start:nav_style_end]

with open(file_bal, 'r', encoding='utf-8') as f:
    bal_content = f.read()

bal_style_start = bal_content.find('<style>') + 7
bal_style_end = bal_content.find('</style>')
bal_css = bal_content[bal_style_start:bal_style_end]

# Extract only the Gallery specific styles from bal_css
gallery_start = bal_css.find('/* ---------- GALLERY WALL LAYOUT ---------- */')
if gallery_start != -1:
    gallery_css = bal_css[gallery_start:]
else:
    gallery_css = bal_css # fallback

# Combine
combined_css = nav_css + "\n" + gallery_css

# Write back
final_content = bal_content[:bal_style_start] + combined_css + bal_content[bal_style_end:]

with open(file_bal, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Restored navbar and footer styles to Balsamic Vinegar Collection.html.")
