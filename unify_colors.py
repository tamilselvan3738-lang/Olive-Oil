import os

files = [f for f in os.listdir('.') if f.endswith('.html')]

# Color mapping to enforce a strictly unified color theme
color_map = {
    # Light Mode Backgrounds -> #fefaf5
    '#fdfcfb': '#fefaf5',
    '#fcf8f2': '#fefaf5',
    '#fdfaf6': '#fefaf5',
    '#f4f0ea': '#fefaf5',
    
    # Light Mode Text -> #2c2418
    '#3e3227': '#2c2418',
    '#3e2c1c': '#2c2418',
    
    # Gold Accents -> #cfbcab
    '#d4b88b': '#cfbcab',
    
    # Dark Mode Backgrounds -> #121212 (Base) or #1f1b16 (Surface)
    '#1a1614': '#121212',
    '#1a1613': '#121212',
    '#16120f': '#121212',
    '#1e1915': '#1f1b16',
    '#221c19': '#1f1b16',
    '#2a241e': '#1f1b16'
}

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for old_color, new_color in color_map.items():
        # Case insensitive replace for hex codes
        content = content.replace(old_color, new_color)
        content = content.replace(old_color.upper(), new_color)
        
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated colors in {filename}")
    else:
        print(f"No color updates needed for {filename}")

print("Unified color theme applied to all HTML pages.")
