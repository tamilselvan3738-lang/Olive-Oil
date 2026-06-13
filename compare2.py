import difflib
import re

about = open('about.html', encoding='utf-8').read()
index = open('index.html', encoding='utf-8').read()

nav_about = re.search(r'<header class="navbar">.*?</header>', about, re.DOTALL).group(0)
nav_index = re.search(r'<header class="navbar">.*?</header>', index, re.DOTALL).group(0)

diff = list(difflib.unified_diff(nav_index.splitlines(), nav_about.splitlines()))

for line in diff:
    print(line)
