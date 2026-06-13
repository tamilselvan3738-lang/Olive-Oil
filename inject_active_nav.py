import os
import glob
import re

css_snippet = """
    /* --- Active Page Nav Styling --- */
    .nav-link.active-page {
      color: #c98a3c !important;
    }
    body.dark .nav-link.active-page {
      color: #e6b975 !important;
    }
    .nav-link.active-page::after {
      width: 80% !important;
      left: 10% !important;
      opacity: 1 !important;
    }
"""

js_snippet = """
    // --- Dynamic Active Link Highlighting ---
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
    });
"""

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'navbar.html':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # Inject CSS
    if '/* --- Active Page Nav Styling --- */' not in content:
        if '</style>' in content:
            content = content.replace('</style>', css_snippet + '  </style>')
            changed = True
            
    # Inject JS
    if '// --- Dynamic Active Link Highlighting ---' not in content:
        # We look for the end of the IIFE in the script block
        end_script_idx = content.rfind('  })();\n</script>')
        if end_script_idx != -1:
            content = content[:end_script_idx] + js_snippet + content[end_script_idx:]
            changed = True
        else:
            # Fallback if the IIFE doesn't end exactly like that
            end_body_idx = content.rfind('</body>')
            if end_body_idx != -1:
                content = content[:end_body_idx] + '<script>' + js_snippet + '</script>\n' + content[end_body_idx:]
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (already updated or no matching tags found)")
