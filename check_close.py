import glob

for f in glob.glob('*.html'):
    if f == 'navbar.html': continue
    content = open(f, encoding='utf-8').read()
    print(f, 'id="mobileMenuClose"' in content)
