import glob
import os
import re

js_snippet = """    // --- Dynamic Active Link Highlighting ---
    const currentPath = decodeURIComponent(window.location.pathname).split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link, .mega-dropdown-item').forEach(link => {
      const href = link.getAttribute('href');
      if (href && !href.startsWith('#') && !href.startsWith('http')) {
        const linkPath = decodeURIComponent(href.replace('./', '')).split('/').pop();
        if (linkPath === currentPath || (currentPath === '' && linkPath === 'index.html')) {
          link.classList.add('active-page');
          const parentDropdown = link.closest('.nav-item.dropdown, .nav-item.mega-dropdown');
          if (parentDropdown) {
             const parentLink = parentDropdown.querySelector('.nav-link');
             if (parentLink) parentLink.classList.add('active-page');
          }
        } else {
          // Remove hardcoded inline color if it doesn't match the current page
          link.style.color = '';
        }
      }
    });"""

css_snippet = """    /* --- Active Page Nav Styling --- */
    .nav-link.active-page, .mega-dropdown-item.active-page {
      color: #c98a3c !important;
    }
    body.dark .nav-link.active-page, body.dark .mega-dropdown-item.active-page {
      color: #e6b975 !important;
    }
    .nav-link.active-page::after {
      width: 80% !important;
      left: 10% !important;
      opacity: 1 !important;
    }"""

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the dynamic JS snippet if it exists
    if '// --- Dynamic Active Link Highlighting ---' in content:
        # Regex to remove the snippet
        content = re.sub(r' +// --- Dynamic Active Link Highlighting ---.*?(?=\s*\n  \}\)\(\);\n</script>)', '', content, flags=re.DOTALL)
        content = re.sub(r'\n+', '\n', content)
        
    # Remove old inline styling
    content = content.replace('style="color: #5f8b6f;"', '')
    
    # Remove any existing active-page classes
    content = content.replace(' active-page', '')

    # 2. Add static class to the correct link based on the filename
    filename = os.path.basename(filepath)
    # The links are usually href="./filename" or href="filename"
    # We will search for href="./filename" and href="filename" inside the navbar section.
    
    # A robust way is to use regex to find the <a> tag with this href
    # Since it's a static site, we can just replace the specific href matching this file
    
    # We also need to highlight the parent if it's a dropdown
    # Let's just find the exact string.
    
    # e.g., <a href="./about.html" class="nav-link">
    # we want it to be <a href="./about.html" class="nav-link active-page">
    
    # Pattern: <a href="./{filename}" class="nav-link"
    pattern1 = f'href="./{filename}" class="nav-link"'
    replacement1 = f'href="./{filename}" class="nav-link active-page"'
    
    pattern2 = f'href="{filename}" class="nav-link"'
    replacement2 = f'href="{filename}" class="nav-link active-page"'
    
    pattern3 = f'href="./{filename}" class="mega-dropdown-item"'
    replacement3 = f'href="./{filename}" class="mega-dropdown-item active-page"'
    
    pattern4 = f'href="{filename}" class="mega-dropdown-item"'
    replacement4 = f'href="{filename}" class="mega-dropdown-item active-page"'

    content = content.replace(pattern1, replacement1)
    content = content.replace(pattern2, replacement2)
    content = content.replace(pattern3, replacement3)
    content = content.replace(pattern4, replacement4)
    
    # If it's index.html or home 2.html, we also need to highlight the parent Home link
    if filename in ['index.html', 'home 2.html']:
        # The parent link is id="homeMainLink"
        content = re.sub(r'(id="homeMainLink"[^>]*class="nav-link)', r'\1 active-page', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Done statically highlighting active links.")
