import glob
import re

css_to_add = """
    .mobile-menu-close { position: absolute; top: 20px; right: 20px; background: none; border: none; font-size: 1.5rem; color: #2c2418; cursor: pointer; padding: 5px; transition: color 0.2s; display: block; z-index: 1000; }
    body.dark .mobile-menu-close { color: #f0e9df; }
    .mobile-menu-close:hover { color: #5f8b6f; }
    body.dark .mobile-menu-close:hover { color: #8fbc9f; }
"""

for filepath in glob.glob('*.html'):
    if filepath in ['login.html', 'registeration.html', 'navbar.html']:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the CSS is missing, add it right before </style>
    if '.mobile-menu-close { position: absolute' not in content:
        # We also need to remove any old broken display rules for mobile-menu-close if they exist
        content = re.sub(r'\.mobile-controls,\s*\.mobile-menu-close\s*\{[^}]*\}', '', content)
        
        # Insert new CSS
        content = content.replace('</style>', css_to_add + '\n  </style>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed CSS in {filepath}")

print("Done syncing mobile-menu-close CSS.")
