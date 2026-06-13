import difflib
import re

about = open('about.html', encoding='utf-8').read()
index = open('index.html', encoding='utf-8').read()

nav_css_about = re.search(r'/\* ---------- COMPACT NAVBAR.*?/\* ---------- FOOTER SECTION', about, re.DOTALL).group(0)
nav_css_index = re.search(r'/\* ---------- COMPACT NAVBAR.*?/\* ---------- FOOTER SECTION', index, re.DOTALL).group(0)

if nav_css_about == nav_css_index:
    print("Navbar CSS is identical!")
else:
    print("Navbar CSS is DIFFERENT!")
    diff = list(difflib.unified_diff(nav_css_index.splitlines(), nav_css_about.splitlines()))
    for line in diff:
        print(line)
