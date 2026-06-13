import glob
import re

# Correct navbar script that has NO syntax errors, NO demo alerts, and properly redirects to login.html
correct_script = """<script>
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
    function toggleDarkMode(e) { 
        if(e) e.stopPropagation(); 
        setDarkMode(!body.classList.contains('dark')); 
    }
    if(darkToggleDesktop) darkToggleDesktop.addEventListener('click', toggleDarkMode);
    if(mobileDarkToggle) mobileDarkToggle.addEventListener('click', toggleDarkMode);
    
    let rtlActive = false;
    function setRTL(active) { if(active) body.classList.add('rtl'); else body.classList.remove('rtl'); rtlActive = active; }
    function toggleRTL(e) { 
        if(e) e.stopPropagation(); 
        setRTL(!rtlActive); 
    }
    if(rtlToggleDesktop) rtlToggleDesktop.addEventListener('click', toggleRTL);
    if(mobileRtlToggle) mobileRtlToggle.addEventListener('click', toggleRTL);
    
    // Login Redirect Logic
    function goToLogin(e) {
        if(e) e.stopPropagation();
        window.location.href = './login.html';
    }
    if(loginDesktop) loginDesktop.addEventListener('click', goToLogin);
    if(mobileLogin) mobileLogin.addEventListener('click', goToLogin);
    
    function openMobileMenu() { navMenu.classList.add('active'); if(overlay) overlay.classList.add('active'); document.body.style.overflow = 'hidden'; if(hamburger) hamburger.classList.add('active'); }
    function closeMobileMenu() { navMenu.classList.remove('active'); if(overlay) overlay.classList.remove('active'); document.body.style.overflow = ''; if(homeMegaItem) homeMegaItem.classList.remove('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); if(hamburger) hamburger.classList.remove('active'); }
    function toggleMobileMenu() { navMenu.classList.contains('active') ? closeMobileMenu() : openMobileMenu(); }
    if(hamburger) hamburger.addEventListener('click', (e) => { e.stopPropagation(); toggleMobileMenu(); });
    if(overlay) overlay.addEventListener('click', closeMobileMenu);
    if(mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener('click', (e) => { e.stopPropagation(); closeMobileMenu(); });
    
    function handleMobileAccordion() {
      if(window.innerWidth <= 1024) {
        if(homeMegaItem) {
          const link = homeMegaItem.querySelector('.nav-link');
          if(link && !link.hasAttribute('data-mh')) {
            link.setAttribute('data-mh', 'true');
            link.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); homeMegaItem.classList.toggle('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); });
          }
        }
        if(clubDropdownLi) {
          const link = clubDropdownLi.querySelector('.nav-link');
          if(link && !link.hasAttribute('data-mc')) {
            link.setAttribute('data-mc', 'true');
            link.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); clubDropdownLi.classList.toggle('open'); if(homeMegaItem) homeMegaItem.classList.remove('open'); });
          }
        }
      } else { if(homeMegaItem) homeMegaItem.classList.remove('open'); if(clubDropdownLi) clubDropdownLi.classList.remove('open'); }
    }
    window.addEventListener('resize', () => { handleMobileAccordion(); if(window.innerWidth > 1024 && navMenu.classList.contains('active')) closeMobileMenu(); });
    handleMobileAccordion();
  })();
</script>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use re.DOTALL and .*? to correctly match the script block containing 'handleMobileAccordion'
    # Wait! Some pages have two script blocks, we want to replace the first one that has handleMobileAccordion.
    # The regex r'<script>.*?handleMobileAccordion.*?</script>' will work safely.
    
    # But wait, what if the script tag has attributes? There are none.
    content = re.sub(r'<script>.*?handleMobileAccordion.*?</script>', correct_script.replace('\\', '\\\\'), content, count=1, flags=re.DOTALL)
    
    # Write it back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Replaced navbar scripts with fully working code across all pages.")
