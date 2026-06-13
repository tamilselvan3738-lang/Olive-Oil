import glob
import re

favicon_tag = '\n  <!-- Favicon -->\n  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🫒</text></svg>">'

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has a favicon
    if 'rel="icon"' in content:
        print(f"Skipping {filepath}, already has a favicon.")
        continue
        
    # Insert right before </head>
    content = content.replace('</head>', favicon_tag + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully added favicon to all pages.")
