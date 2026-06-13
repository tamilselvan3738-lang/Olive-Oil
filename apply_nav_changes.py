import os
import glob

# Changes to apply
CSS_HAMBURGER_OLD = """    .hamburger { display: none; flex-direction: column; cursor: pointer; gap: 4px; margin-left: 6px; }
    .hamburger span { width: 22px; height: 2px; background-color: #2c2418; transition: 0.2s; border-radius: 2px; }"""

CSS_HAMBURGER_NEW = """    .hamburger { display: none; flex-direction: column; cursor: pointer; gap: 4px; margin-left: 6px; }
    .hamburger span { width: 22px; height: 2px; background-color: #2c2418; transition: 0.3s ease; border-radius: 2px; transform-origin: center; }
    .hamburger.active span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
    .hamburger.active span:nth-child(2) { opacity: 0; }
    .hamburger.active span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }"""

CSS_OVERLAY_OLD = """      .menu-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.4); z-index: 998; opacity: 0; visibility: hidden; transition: all 0.25s ease; }
      .menu-overlay.active { opacity: 1; visibility: visible; }
    }"""

CSS_OVERLAY_NEW = """      .menu-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.4); z-index: 998; opacity: 0; visibility: hidden; transition: all 0.25s ease; }
      .menu-overlay.active { opacity: 1; visibility: visible; }
      .mobile-menu-close { position: absolute; top: 20px; right: 20px; background: none; border: none; font-size: 1.5rem; color: #2c2418; cursor: pointer; padding: 5px; transition: color 0.2s; display: block; z-index: 1000; }
      .mobile-menu-close:hover { color: #5f8b6f; }
      body.dark .mobile-menu-close { color: #f0e9df; }
    }"""

HTML_MENU_OLD = """    <ul class="nav-menu" id="navMenu">
      <li class="nav-item mega-dropdown" id="homeMegaDropdown">"""

HTML_MENU_NEW = """    <ul class="nav-menu" id="navMenu">
      <button class="mobile-menu-close" id="mobileMenuClose" aria-label="Close menu"><i class="fas fa-arrow-right"></i></button>
      <li class="nav-item mega-dropdown" id="homeMegaDropdown">"""

JS_CONST_OLD = """    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const overlay = document.getElementById('menuOverlay');
    const homeMegaItem = document.getElementById('homeMegaDropdown');"""

JS_CONST_NEW = """    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const overlay = document.getElementById('menuOverlay');
    const mobileMenuCloseBtn = document.getElementById('mobileMenuClose');
    const homeMegaItem = document.getElementById('homeMegaDropdown');"""

JS_FUNCS_OLD = """    function openMobileMenu() { navMenu.classList.add('active'); if(overlay) overlay.classList.add('active'); document.body.style.overflow = 'hidden'; }
    function closeMobileMenu() { navMenu.classList.remove('active'); if(overlay) overlay.classList.remove('active'); document.body.style.overflow = ''; if(homeMegaItem) homeMegaItem.classList.remove('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); }"""

JS_FUNCS_NEW = """    function openMobileMenu() { navMenu.classList.add('active'); if(overlay) overlay.classList.add('active'); document.body.style.overflow = 'hidden'; if(hamburger) hamburger.classList.add('active'); }
    function closeMobileMenu() { navMenu.classList.remove('active'); if(overlay) overlay.classList.remove('active'); document.body.style.overflow = ''; if(homeMegaItem) homeMegaItem.classList.remove('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); if(hamburger) hamburger.classList.remove('active'); }"""

JS_EVENT_OLD = """    if(hamburger) hamburger.addEventListener('click', (e) => { e.stopPropagation(); toggleMobileMenu(); });
    if(overlay) overlay.addEventListener('click', closeMobileMenu);"""

JS_EVENT_NEW = """    if(hamburger) hamburger.addEventListener('click', (e) => { e.stopPropagation(); toggleMobileMenu(); });
    if(overlay) overlay.addEventListener('click', closeMobileMenu);
    if(mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener('click', (e) => { e.stopPropagation(); closeMobileMenu(); });"""

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'about.html':
        continue # Already updated

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if CSS_HAMBURGER_OLD in content:
        content = content.replace(CSS_HAMBURGER_OLD, CSS_HAMBURGER_NEW)
        changed = True
    
    if CSS_OVERLAY_OLD in content:
        content = content.replace(CSS_OVERLAY_OLD, CSS_OVERLAY_NEW)
        changed = True
        
    if HTML_MENU_OLD in content:
        content = content.replace(HTML_MENU_OLD, HTML_MENU_NEW)
        changed = True
        
    if JS_CONST_OLD in content:
        content = content.replace(JS_CONST_OLD, JS_CONST_NEW)
        changed = True
        
    if JS_FUNCS_OLD in content:
        content = content.replace(JS_FUNCS_OLD, JS_FUNCS_NEW)
        changed = True
        
    if JS_EVENT_OLD in content:
        # Avoid duplicate appending
        if JS_EVENT_NEW not in content:
            content = content.replace(JS_EVENT_OLD, JS_EVENT_NEW)
            changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')
