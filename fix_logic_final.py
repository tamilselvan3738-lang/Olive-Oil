import glob
import re

js_to_inject = """<script>
document.addEventListener("DOMContentLoaded", function() {
    const body = document.body;
    
    // Elements
    const darkToggleDesktop = document.getElementById('darkModeToggle');
    const mobileDarkToggle = document.getElementById('mobileDarkToggle');
    const themeToggle = document.getElementById('themeToggle'); // For login/register pages
    
    const rtlToggleDesktop = document.getElementById('rtlToggle');
    const mobileRtlToggle = document.getElementById('mobileRtlToggle');
    
    const loginDesktop = document.getElementById('loginBtn');
    const mobileLogin = document.getElementById('mobileLoginBtn');
    
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const overlay = document.getElementById('menuOverlay');
    const mobileMenuCloseBtn = document.getElementById('mobileMenuClose');
    
    // Icons
    const desktopDarkIcon = document.getElementById('desktopDarkIcon');
    const mobileDarkIcon = document.getElementById('mobileDarkIcon');
    const mobileDarkText = document.getElementById('mobileDarkText');
    const themeIcon = document.getElementById('themeIcon');
    
    // --- Login Redirect ---
    function redirectToLogin(e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        window.location.href = 'login.html';
    }
    if (loginDesktop) loginDesktop.addEventListener('click', redirectToLogin);
    if (mobileLogin) mobileLogin.addEventListener('click', redirectToLogin);

    // --- Dark Mode Logic ---
    const DARK_KEY = 'oliveOilDarkMode';
    
    function updateDarkModeUI(isDark) {
        const iconClass = isDark ? 'fas fa-sun' : 'fas fa-moon';
        if(desktopDarkIcon) desktopDarkIcon.className = iconClass;
        if(mobileDarkIcon) mobileDarkIcon.className = iconClass;
        if(themeIcon) themeIcon.className = iconClass;
        if(mobileDarkText) mobileDarkText.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    }
    
    function setDarkMode(isDark) {
        if(isDark) body.classList.add('dark');
        else body.classList.remove('dark');
        localStorage.setItem(DARK_KEY, isDark);
        updateDarkModeUI(isDark);
    }
    
    function toggleDarkMode(e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        setDarkMode(!body.classList.contains('dark'));
    }
    
    // Load saved or system preference
    const savedDark = localStorage.getItem(DARK_KEY);
    if(savedDark === 'true') setDarkMode(true);
    else if(savedDark === 'false') setDarkMode(false);
    else setDarkMode(window.matchMedia('(prefers-color-scheme: dark)').matches);
    
    // Attach listeners
    if(darkToggleDesktop) darkToggleDesktop.addEventListener('click', toggleDarkMode);
    if(mobileDarkToggle) mobileDarkToggle.addEventListener('click', toggleDarkMode);
    if(themeToggle) themeToggle.addEventListener('click', toggleDarkMode);
    
    // --- RTL Logic ---
    const RTL_KEY = 'oliveOilRTLMode';
    
    function setRTL(isRTL) {
        if(isRTL) { body.classList.add('rtl'); body.setAttribute('dir', 'rtl'); }
        else { body.classList.remove('rtl'); body.removeAttribute('dir'); }
        localStorage.setItem(RTL_KEY, isRTL);
    }
    
    function toggleRTL(e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        setRTL(!body.classList.contains('rtl'));
    }
    
    // Load saved RTL preference
    const savedRTL = localStorage.getItem(RTL_KEY);
    if(savedRTL === 'true') setRTL(true);
    else setRTL(false);
    
    // Attach listeners
    if(rtlToggleDesktop) rtlToggleDesktop.addEventListener('click', toggleRTL);
    if(mobileRtlToggle) mobileRtlToggle.addEventListener('click', toggleRTL);
    
    // --- Mobile Menu Drawer ---
    function openMobileMenu() {
        if(navMenu) navMenu.classList.add('active');
        if(overlay) overlay.classList.add('active');
        body.style.overflow = 'hidden';
        if(hamburger) hamburger.classList.add('active');
    }
    
    function closeMobileMenu() {
        if(navMenu) navMenu.classList.remove('active');
        if(overlay) overlay.classList.remove('active');
        body.style.overflow = '';
        if(hamburger) hamburger.classList.remove('active');
        
        // Close accordions
        document.querySelectorAll('.nav-item.mega-dropdown, .nav-item.dropdown').forEach(item => {
            item.classList.remove('open');
        });
    }
    
    function toggleMobileMenu(e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        if(navMenu && navMenu.classList.contains('active')) closeMobileMenu();
        else openMobileMenu();
    }
    
    if(hamburger) hamburger.addEventListener('click', toggleMobileMenu);
    if(overlay) overlay.addEventListener('click', closeMobileMenu);
    if(mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener('click', closeMobileMenu);
    
    // --- Mobile Menu Accordion ---
    document.querySelectorAll('.nav-item.mega-dropdown, .nav-item.dropdown').forEach(item => {
        const link = item.querySelector('.nav-link');
        if(link) {
            link.addEventListener('click', (e) => {
                // Only act as accordion on mobile (when hamburger is visible)
                if (window.innerWidth <= 1024) {
                    e.preventDefault(); // Prevent redirect
                    e.stopPropagation();
                    item.classList.toggle('open');
                }
            });
        }
    });
    
    // --- Dynamic Active Link Highlighting ---
    function highlightActivePage() {
        const currentPath = decodeURIComponent(window.location.pathname).split('/').pop() || 'index.html';
        document.querySelectorAll('.nav-link, .mega-dropdown-item').forEach(link => {
            link.style.color = ''; // Clear inline
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
});
</script>"""

rtl_css = """
    /* --- RTL Support --- */
    body.rtl { direction: rtl; text-align: right; }
    body.rtl .navbar .logo-area { flex-direction: row-reverse; }
    body.rtl .nav-menu { right: auto; left: -100%; transition: left 0.3s cubic-bezier(0.2, 0.9, 0.4, 1.1); border-left: none; border-right: 1px solid #e2d6ca; }
    body.rtl .nav-menu.active { right: auto; left: 0; }
    body.rtl .mobile-menu-close { right: auto; left: 20px; }
    body.rtl .desktop-controls { margin-left: 0; margin-right: auto; }
"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace script
    if '<script>' in content:
        # Find the last script block, which is usually our app script
        scripts = list(re.finditer(r'<script>.*?</script>', content, re.DOTALL))
        if scripts:
            last_script = scripts[-1]
            content = content[:last_script.start()] + js_to_inject + content[last_script.end():]

    # 2. Add RTL CSS if missing
    if 'body.rtl' not in content and '</style>' in content:
        content = content.replace('</style>', rtl_css + '\n  </style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied robust Javascript and RTL fixes.")
