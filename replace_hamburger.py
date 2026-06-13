import os
import re

directory = r"d:\Projects\olive oil"
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# The CSS block to inject
new_hamburger_css = """    .hamburger { display: none; flex-direction: column; cursor: pointer; gap: 4px; margin-left: 6px; }
    .hamburger span { width: 22px; height: 2px; background-color: #2c2418; transition: 0.3s ease; border-radius: 2px; transform-origin: center; }
    .hamburger.active span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
    .hamburger.active span:nth-child(2) { opacity: 0; }
    .hamburger.active span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }"""

# We'll use a regex that matches the .hamburger block but doesn't have the .active span
pattern = re.compile(
    r'\.hamburger\s*\{\s*display:\s*none;\s*flex-direction:\s*column;\s*cursor:\s*pointer;\s*gap:\s*4px;\s*margin-left:\s*6px;\s*\}\s*'
    r'\.hamburger\s+span\s*\{\s*width:\s*22px;\s*height:\s*2px;\s*background-color:\s*#2c2418;\s*transition:\s*0\.2s;\s*border-radius:\s*2px;\s*\}'
)

for file in files:
    path = os.path.join(directory, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '.hamburger.active' not in content:
        # Check if the pattern exists
        if pattern.search(content):
            new_content = pattern.sub(new_hamburger_css, content)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Pattern not found in {file}, but .hamburger.active is also missing. Manual check might be needed.")
    else:
        print(f"Already updated: {file}")
