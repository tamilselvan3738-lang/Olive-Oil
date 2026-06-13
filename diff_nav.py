import re
import difflib

def get_nav(fpath):
    content = open(fpath, encoding='utf-8').read()
    match = re.search(r'<header class="navbar">.*?</header>', content, re.DOTALL)
    if match: return match.group(0)
    return ""

about_nav = get_nav("about.html")
index_nav = get_nav("index.html")

diff = list(difflib.context_diff(about_nav.splitlines(), index_nav.splitlines(), fromfile='about', tofile='index'))
for line in diff:
    print(line)
