import re

index = open('index.html', encoding='utf-8').read()
about = open('about.html', encoding='utf-8').read()

print("Index viewport:", re.search(r'<meta name="viewport".*?>', index).group(0))
print("About viewport:", re.search(r'<meta name="viewport".*?>', about).group(0))
