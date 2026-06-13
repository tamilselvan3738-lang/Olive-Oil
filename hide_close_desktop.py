import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to hide the mobile-menu-close on desktop.
    # The best way is to add it to the custom CSS block we injected.
    if '.mobile-menu-close { display: none !important; }' not in content:
        # Add it right before </style>
        content = content.replace('</style>', '    @media (min-width: 1025px) { .mobile-menu-close { display: none !important; } }\n  </style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed desktop mobile menu close button visibility.")
