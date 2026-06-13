import os
import re

file_path = 'Balsamic Vinegar Collection.html'

if not os.path.exists(file_path):
    print("File not found!")
    exit()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up inline styles that have hardcoded backgrounds causing issues
# Match any style attribute containing background or background-color with gradients or hexes
content = re.sub(r'style="[^"]*background:\s*linear-gradient[^"]*"', 'style="border-radius: 2.5rem; padding: 8rem 2rem; text-align: center; margin: 6rem 0; position: relative; overflow: hidden;"', content)
content = re.sub(r'style="[^"]*background:\s*#ffffff[^"]*"', 'style="margin-bottom: 5rem; padding: 6rem 2rem; border-radius: 2rem; border: 1px solid #cfbcab; box-shadow: 0 30px 60px rgba(0,0,0,0.05); position: relative; overflow: hidden; text-align: center;"', content)
content = re.sub(r'<div style="position: absolute; top: 0; left: 0; right: 0; height: 100%; background: linear-gradient[^>]+></div>', '', content)
content = re.sub(r'<div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient[^>]+></div>', '', content)

# 2. Hardcode the exact Olive Oil Collection colors
# Light Mode Base: #fefaf5
# Text: #2c2418
# Secondary Text: #6b5a48
# Accent: #5f8b6f
# Gold: #cfbcab
# Dark Mode Base: #121212
# Dark Surface: #1f1b16
# Dark Text: #ece8e0

color_replacements = {
    '#ffffff': 'var(--bg-surface, #ffffff)',  
    '#2c241c': '#2c2418',
    '#7a6e61': '#6b5a48',
    '#cfbcab': '#cfbcab',
    '#f0e9df': '#cfbcab', # Use gold for borders instead of off-white
    '#362a21': '#3a2e26',
    '#1f1b16': '#1f1b16',
    'rgba(212,184,139,0.05)': 'rgba(0,0,0,0.05)',
    'rgba(212, 184, 139, 0.1)': 'rgba(0,0,0,0.05)',
    'rgba(212, 184, 139, 0.08)': 'rgba(0,0,0,0.05)',
}

for old, new in color_replacements.items():
    content = content.replace(old, new)

# 3. Add CSS Variables globally at the start of the <style> block
vars_css = """
    :root {
      --bg-main: #fefaf5;
      --text-main: #2c2418;
      --bg-surface: #ffffff;
      --border-light: #cfbcab;
      --accent: #5f8b6f;
    }
    body.dark {
      --bg-main: #121212;
      --text-main: #ece8e0;
      --bg-surface: #1f1b16;
      --border-light: #3a2e26;
    }
"""

style_idx = content.find('<style>')
if style_idx != -1:
    content = content[:style_idx + 7] + vars_css + content[style_idx + 7:]

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Balsamic Vinegar Collection.html cleaned and theme aligned.")
