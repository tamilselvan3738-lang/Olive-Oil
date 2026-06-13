import glob
import re

# 1. Read clean script from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

clean_script_match = re.search(r'<script>(.*?)</script>', about_content, re.DOTALL)
if clean_script_match:
    clean_script = clean_script_match.group(0)
else:
    print("Could not find script in about.html")
    exit(1)

broken_css_pattern = r'      \.mobile-controls, \.mobile-menu-close \{\s*display: none !important;\s*\}\s*\.nav-menu \{\s*justify-content: center;\s*\}\s*\.logo-area \{\s*width: auto;\s*\}\s*\.desktop-controls \{\s*width: auto;\s*\}\s*\}'

for filepath in glob.glob('*.html'):
    if filepath == 'about.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix the broken CSS
    content = re.sub(broken_css_pattern, '', content)
    
    # Replace the navbar script block with the clean script from about.html
    # This removes SyntaxErrors (\\\'click\\\') and demo alerts (e.preventDefault())
    if 'handleMobileAccordion' in content:
        content = re.sub(r'<script>[^<]*handleMobileAccordion[^<]*</script>', clean_script.replace('\\', '\\\\'), content, count=1, flags=re.DOTALL)
    
    # Fix the invisible content bug in pro-animations-script
    if 'selectorsToAnimate.join' in content:
        content = content.replace(
            "const elements = document.querySelectorAll(selectorsToAnimate.join(', '));",
            "const elements = document.querySelectorAll(selectorsToAnimate.join(', ') + ', .reveal-on-scroll');"
        )
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully fixed invisible content and dark mode functionality across all pages.")
