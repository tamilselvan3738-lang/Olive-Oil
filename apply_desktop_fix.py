import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'about.html':
        continue # Already updated

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Regex to find .mobile-controls { display: none !important; } and change to .mobile-controls, .mobile-menu-close { display: none !important; }
    # We can just look for ".mobile-controls {" or ".mobile-controls{" near "display: none !important"
    
    # Let's replace the specific string in index.html
    old_str_1 = """.mobile-controls {
        display: none !important;
      }"""
    new_str_1 = """.mobile-controls, .mobile-menu-close {
        display: none !important;
      }"""
      
    old_str_2 = """.mobile-controls { display: none !important; }"""
    new_str_2 = """.mobile-controls, .mobile-menu-close { display: none !important; }"""

    if old_str_1 in content:
        content = content.replace(old_str_1, new_str_1)
        changed = True
    elif old_str_2 in content:
        content = content.replace(old_str_2, new_str_2)
        changed = True
    else:
        # try regex for more robust replacement
        # look for @media (min-width: 1025px) block and replace mobile-controls
        pattern = r'(@media\s*\(\s*min-width\s*:\s*102[45]px\s*\)\s*\{[^}]*?\.mobile-controls)\s*\{'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1, .mobile-menu-close {', content)
            changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')
    else:
        print(f'No changes needed or pattern not found in {file}')
