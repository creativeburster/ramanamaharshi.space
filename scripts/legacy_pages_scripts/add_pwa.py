import glob, re

sw_script = '''
    <script>
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').catch(() => {});
      }
    </script>
'''

pwa_meta = '''    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="apple-touch-icon" href="icons/icon-192.png">
'''

count = 0
for fp in sorted(glob.glob('**/*.html', recursive=True)):
    if 'node_modules' in fp or 'test' in fp: continue
    with open(fp, encoding='utf-8') as f:
        c = f.read()

    original = c

    # Add PWA meta tags in <head> (if not already present)
    if 'manifest.json' not in c:
        if '</head>' in c:
            c = c.replace('</head>', pwa_meta + '</head>')

    # Add SW registration before </body>
    if "serviceWorker.register" not in c and '</body>' in c:
        c = c.replace('</body>', sw_script + '</body>')
        count += 1

    if c != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)

print(f'Updated {count} files with PWA support')
