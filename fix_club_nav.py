import os

file_club = 'Oil of the Month Club.html'
file_nav = 'navbar.html'

with open(file_nav, 'r', encoding='utf-8') as f:
    nav_content = f.read()
    
nav_style_start = nav_content.find('<style>') + 7
nav_style_end = nav_content.find('</style>')
nav_css = nav_content[nav_style_start:nav_style_end]

with open(file_club, 'r', encoding='utf-8') as f:
    club_content = f.read()

club_style_start = club_content.find('<style>') + 7
club_style_end = club_content.find('</style>')
club_css = club_content[club_style_start:club_style_end]

# Extract only the VIP specific styles from club_css (skip base variables that overlap)
vip_start = club_css.find('/* ---------- VIP PORTAL LAYOUT ---------- */')
if vip_start != -1:
    vip_css = club_css[vip_start:]
else:
    vip_css = club_css # fallback

# Combine
combined_css = nav_css + "\n" + vip_css

# Write back
final_content = club_content[:club_style_start] + combined_css + club_content[club_style_end:]

with open(file_club, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Restored navbar and footer styles to Oil of the Month Club.html.")
