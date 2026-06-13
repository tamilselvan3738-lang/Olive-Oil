import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "classList.add('is-visible');" in content and "observerOptions = { root: null" in content:
        # It's our injected script, replace it to add both classes
        content = content.replace("classList.add('is-visible');", "classList.add('is-visible', 'active');")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed classes in {filepath}")

print("Done updating observer scripts.")
