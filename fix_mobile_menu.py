import os
import glob

html_files = glob.glob('d:/Projects/olive oil/*.html')

css_addition = """      .nav-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 280px;
        height: 100vh;"""

close_btn_css = """
      .mobile-menu-close {
        position: absolute;
        top: 15px;
        right: 20px;
        background: transparent;
        border: none;
        font-size: 1.4rem;
        cursor: pointer;
        color: #2c2418;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        transition: background-color 0.2s;
        z-index: 1001;
      }
      .mobile-menu-close:hover {
        background-color: #e7dfd6;
      }
      body.dark .mobile-menu-close {
        color: #f0e9df;
      }
      body.dark .mobile-menu-close:hover {
        background-color: #3a2e26;
      }
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if '$1100vh;' in content:
        content = content.replace('$1100vh;', css_addition)
        modified = True
        
    if '.mobile-menu-close {' not in content:
        target = "body.dark .nav-menu {"
        if target in content:
            content = content.replace(target, close_btn_css + "\n      " + target)
            modified = True
            
    # Check if the button actually exists
    if '<button class="mobile-menu-close"' not in content:
        # Add it right after <ul class="nav-menu" id="navMenu">
        nav_ul = '<ul class="nav-menu" id="navMenu">'
        if nav_ul in content:
            btn_html = '\n      <button class="mobile-menu-close" id="mobileMenuClose" aria-label="Close menu"><i class="fas fa-arrow-right"></i></button>'
            content = content.replace(nav_ul, nav_ul + btn_html)
            modified = True
            
    # Check JS
    js_target = "if(mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener('click', (e) => { e.stopPropagation(); closeMobileMenu(); });"
    if js_target not in content:
        # Check if mobileMenuCloseBtn is defined
        def_target = "const overlay = document.getElementById('menuOverlay');"
        if def_target in content and "const mobileMenuCloseBtn" not in content:
            content = content.replace(def_target, def_target + "\n    const mobileMenuCloseBtn = document.getElementById('mobileMenuClose');")
            modified = True
        
        js_hook_target = "if(overlay) overlay.addEventListener('click', closeMobileMenu);"
        if js_hook_target in content:
            content = content.replace(js_hook_target, js_hook_target + "\n    " + js_target)
            modified = True

    if modified:
        print(f"Fixed {os.path.basename(filepath)}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
