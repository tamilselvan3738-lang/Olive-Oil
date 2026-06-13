import re

about = open('about.html', encoding='utf-8').read()
index = open('index.html', encoding='utf-8').read()

nav_about = re.search(r'<header class="navbar">.*?</header>', about, re.DOTALL).group(0)
nav_index = re.search(r'<header class="navbar">.*?</header>', index, re.DOTALL).group(0)

if nav_about != nav_index:
    print("Navbars are DIFFERENT!")
else:
    print("Navbars are identical!")

style_about = re.search(r'<style>.*?</style>', about, re.DOTALL).group(0)
style_index = re.search(r'<style>.*?</style>', index, re.DOTALL).group(0)

print(f"About style length: {len(style_about)}")
print(f"Index style length: {len(style_index)}")
