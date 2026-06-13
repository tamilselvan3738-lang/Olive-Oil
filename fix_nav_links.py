import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want to replace `e.preventDefault(); alert("... Demo: ...");` with nothing, 
# or just remove `e.preventDefault();` when it's attached to an alert.

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content

    # 1. simpleNavHandler
    content = re.sub(
        r'function simpleNavHandler\(e\)\s*\{\s*if\(window\.innerWidth <= 1024\)\{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*closeMobileMenu\(\);\s*\}\s*\}',
        r'function simpleNavHandler(e) { if(window.innerWidth <= 1024){ closeMobileMenu(); } }',
        content
    )
    
    # 2. dropdown-item, mega-dropdown-item
    content = re.sub(
        r'item\.addEventListener\(\'click\', \(e\) => \{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*(if\(window\.innerWidth <= 1024\) closeMobileMenu\(\);)?\s*\}\);',
        r'item.addEventListener(\'click\', (e) => { \1 });',
        content
    )
    
    # 3. nav-item:not... nav-link
    content = re.sub(
        r'link\.addEventListener\(\'click\', \(e\) => \{\s*if\(window\.innerWidth > 1024\)\s*\{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*\}\s*\}\);',
        r'link.addEventListener(\'click\', (e) => { /* no-op */ });',
        content
    )
    
    # 4. logoLink
    content = re.sub(
        r'logoLink\.addEventListener\(\'click\', \(e\) => \{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*(if\(window\.innerWidth <= 1024\) closeMobileMenu\(\);)?\s*\}\);',
        r'logoLink.addEventListener(\'click\', (e) => { \1 });',
        content
    )
    
    # 5. homeMainLink
    content = re.sub(
        r'homeMainLink\.addEventListener\(\'click\', \(e\) => \{\s*if\(window\.innerWidth > 1024\)\s*\{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*\}\s*\}\);',
        r'homeMainLink.addEventListener(\'click\', (e) => { /* no-op */ });',
        content
    )
    
    # 6. clubDesktopLink
    content = re.sub(
        r'clubDesktopLink\.addEventListener\(\'click\', \(e\) => \{\s*e\.preventDefault\(\);\s*alert\([^)]+\);\s*\}\);',
        r'clubDesktopLink.addEventListener(\'click\', (e) => { /* no-op */ });',
        content
    )

    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file}")
