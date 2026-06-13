import glob
import re

observer_script = """
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.reveal, .reveal-on-scroll').forEach(el => observer.observe(el));
  });
</script>
"""

# We'll inject this right before </body> if it has 'reveal' but no 'IntersectionObserver'
for f in glob.glob('*.html'):
    content = open(f, encoding='utf-8').read()
    if ('reveal' in content or 'reveal-on-scroll' in content) and 'IntersectionObserver' not in content:
        print(f"Fixing {f}...")
        content = content.replace('</body>', observer_script + '\n</body>')
        open(f, 'w', encoding='utf-8').write(content)
print("Done fixing observers.")
