import re
content = open('index.html', encoding='utf-8').read()
sections = re.findall(r'<section class="(.*?)"', content)
print("Sections:", sections)

# Also check for invisible text due to color
print("body color:", re.findall(r'body\s*\{[^}]*color:\s*([^;]+)', content))
print("bg color:", re.findall(r'body\s*\{[^}]*background-color:\s*([^;]+)', content))

# Let's check for any missing closing tags in head
head = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
if head:
    head_content = head.group(1)
    styles = re.findall(r'<style.*?>', head_content)
    end_styles = re.findall(r'</style>', head_content)
    print("Styles count:", len(styles), "End styles:", len(end_styles))
