import glob
import re

js_to_inject = """<script>
  (function() {
    const body = document.body;
    const darkToggleDesktop = document.getElementById('darkModeToggle');
    const mobileDarkToggle = document.getElementById('mobileDarkToggle');
    const rtlToggleDesktop = document.getElementById('rtlToggle');
    const mobileRtlToggle = document.getElementById('mobileRtlToggle');
    const loginDesktop = document.getElementById('loginBtn');
    const mobileLogin = document.getElementById('mobileLoginBtn');
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const overlay = document.getElementById('menuOverlay');
    const mobileMenuCloseBtn = document.getElementById('mobileMenuClose');
    const homeMegaItem = document.getElementById('homeMegaDropdown');
    const clubDropdownLi = document.getElementById('clubDropdown');
    
    const desktopDarkIcon = document.getElementById('desktopDarkIcon');
    const mobileDarkIcon = document.getElementById('mobileDarkIcon');
    const mobileDarkText = document.getElementById('mobileDarkText');
    
    // Login Redirect
    if (loginDesktop) loginDesktop.addEventListener('click', () => window.location.href = './login.html');
    if (mobileLogin) mobileLogin.addEventListener('click', () => window.location.href = './login.html');

    function updateDarkModeIcons(isDark) {
      if(desktopDarkIcon) desktopDarkIcon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
      if(mobileDarkIcon) mobileDarkIcon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
      if(mobileDarkText) mobileDarkText.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    }
    
    const DARK_KEY = 'oliveOilDarkMode';
    function setDarkMode(isDark) {
      if(isDark) body.classList.add('dark');
      else body.classList.remove('dark');
      localStorage.setItem(DARK_KEY, isDark);
      updateDarkModeIcons(isDark);
    }
    function loadDarkMode() {
      const saved = localStorage.getItem(DARK_KEY);
      if(saved === 'true') setDarkMode(true);
      else if(saved === 'false') setDarkMode(false);
      else setDarkMode(window.matchMedia('(prefers-color-scheme: dark)').matches);
    }
    loadDarkMode();
    function toggleDarkMode() { setDarkMode(!body.classList.contains('dark')); }
    if(darkToggleDesktop) darkToggleDesktop.addEventListener('click', toggleDarkMode);
    if(mobileDarkToggle) mobileDarkToggle.addEventListener('click', toggleDarkMode);
    
    let rtlActive = false;
    function setRTL(active) { if(active) body.classList.add('rtl'); else body.classList.remove('rtl'); rtlActive = active; }
    function toggleRTL() { setRTL(!rtlActive); }
    if(rtlToggleDesktop) rtlToggleDesktop.addEventListener('click', toggleRTL);
    if(mobileRtlToggle) mobileRtlToggle.addEventListener('click', toggleRTL);
    
    function openMobileMenu() { navMenu.classList.add('active'); if(overlay) overlay.classList.add('active'); document.body.style.overflow = 'hidden'; if(hamburger) hamburger.classList.add('active'); }
    function closeMobileMenu() { navMenu.classList.remove('active'); if(overlay) overlay.classList.remove('active'); document.body.style.overflow = ''; if(homeMegaItem) homeMegaItem.classList.remove('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); if(hamburger) hamburger.classList.remove('active'); }
    function toggleMobileMenu() { navMenu.classList.contains('active') ? closeMobileMenu() : openMobileMenu(); }
    if(hamburger) hamburger.addEventListener('click', (e) => { e.stopPropagation(); toggleMobileMenu(); });
    if(overlay) overlay.addEventListener('click', closeMobileMenu);
    if(mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener('click', (e) => { e.stopPropagation(); closeMobileMenu(); });
    
    // --- Dynamic Active Link Highlighting ---
    function highlightActivePage() {
      const currentPath = decodeURIComponent(window.location.pathname).split('/').pop() || 'index.html';
      document.querySelectorAll('.nav-link, .mega-dropdown-item').forEach(link => {
        // Clear any inline styles that might conflict
        link.style.color = '';
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
             link.classList.remove('active-page');
          }
        }
      });
    }
    highlightActivePage();
  })();
</script>"""

close_btn_html = '<button class="mobile-menu-close" id="mobileMenuClose" aria-label="Close menu"><i class="fas fa-arrow-right"></i></button>'

css_snippet = """
    /* --- Active Page Nav Styling --- */
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
    }
"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject the mobile-menu-close button inside <ul class="nav-menu" id="navMenu">
    if 'id="mobileMenuClose"' not in content:
        content = re.sub(r'(<ul class="nav-menu" id="navMenu">)', r'\1\n      ' + close_btn_html, content)
        
    # 2. Inject Active Page CSS if missing
    if '.nav-link.active-page' not in content:
        if '</style>' in content:
            content = content.replace('</style>', css_snippet + '\n  </style>')
            
    # 3. Strip all inline styles from nav-links to ensure our CSS takes priority
    content = re.sub(r'(<a[^>]*class="[^"]*nav-link[^"]*"[^>]*)style="[^"]*"', r'\1', content)
    
    # 4. Replace the old broken script with the robust new one
    content = re.sub(r'<script>[^<]*handleMobileAccordion[^<]*</script>', js_to_inject, content, flags=re.DOTALL)
    content = re.sub(r'<script>[^<]*const currentPath[^<]*</script>', js_to_inject, content, flags=re.DOTALL)

    # If neither pattern matched, just replace the last script
    if 'highlightActivePage' not in content:
        scripts = list(re.finditer(r'<script>.*?</script>', content, re.DOTALL))
        if scripts:
            last_script = scripts[-1]
            content = content[:last_script.start()] + js_to_inject + content[last_script.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Applied fixes to all files.")
