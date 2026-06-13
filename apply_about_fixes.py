import glob
import re

# 1. Read clean script from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

clean_script = re.search(r'<script>(.*?)</script>', about_content, re.DOTALL).group(0)

broken_css_pattern = r'      \.mobile-controls, \.mobile-menu-close \{\s*display: none !important;\s*\}\s*\.nav-menu \{\s*justify-content: center;\s*\}\s*\.logo-area \{\s*width: auto;\s*\}\s*\.desktop-controls \{\s*width: auto;\s*\}\s*\}'

for filepath in glob.glob('*.html'):
    if filepath == 'about.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 2. Fix the broken CSS
    content = re.sub(broken_css_pattern, '', content)
    
    # 3. Replace the last script block with the clean script from about.html
    # Some files might have other scripts, so we replace the last one (which is the navbar script)
    # Actually, we can just replace the navbar script. The navbar script usually contains 'handleMobileAccordion'
    
    if 'handleMobileAccordion' in content:
        # Find the script block containing handleMobileAccordion
        content = re.sub(r'<script>[^<]*handleMobileAccordion[^<]*</script>', clean_script.replace('\\', '\\\\'), content, flags=re.DOTALL)
    else:
        # If no handleMobileAccordion, just replace the last script block
        # Find all script blocks
        scripts = list(re.finditer(r'<script>.*?</script>', content, re.DOTALL))
        if scripts:
            last_script = scripts[-1]
            content = content[:last_script.start()] + clean_script + content[last_script.end():]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully applied about.html fixes to all pages.")
