import glob
import os
import re
import sys

all_passed = True

print("Verifying responsive scaling integration...")

for filepath in glob.glob('d:/Projects/olive oil/*.html'):
    filename = os.path.basename(filepath)
    content = open(filepath, encoding='utf-8').read()
    
    # Check viewport tag
    viewport = re.search(r'<meta name="viewport".*?>', content)
    
    # Check global responsive scaling style tag
    has_global_style = 'id="global-responsive-scaling"' in content
    

    # Check for other pages
    issues = []
    if not viewport:
        issues.append("Missing viewport meta tag")
    if not has_global_style:
        issues.append("Missing global responsive scaling style tag (<style id=\"global-responsive-scaling\">)")
        
    if issues:
        print(f"[-] FAIL: {filename} has issues: {', '.join(issues)}")
        all_passed = False
    else:
        print(f"[+] PASS: {filename} is fully equipped with responsive configurations.")

if all_passed:
    print("\n[SUCCESS] All checks passed! All pages (including index.html) are ready with responsive configurations.")
    sys.exit(0)
else:
    print("\n[FAILURE] One or more pages failed responsiveness validation checks.")
    sys.exit(1)
