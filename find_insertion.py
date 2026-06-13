import os

with open('Gift Box Builder.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_start = content.find('<main')
footer_start = content.find('<footer class="footer">')

if main_start != -1 and footer_start != -1:
    print(f'Found <main> at index {main_start}')
    print(f'Found footer at index {footer_start}')
else:
    # If no <main>, look for container
    container_start = content.find('<div class="container"')
    print(f'Container start: {container_start}, Footer start: {footer_start}')
