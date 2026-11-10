import glob
import re
import os

GA_ID = 'G-MYFWHFPSYB'

OLD_GA_PATTERN = re.compile(
    r'<script data-cfasync="false">\s*'
    r'window\.dataLayer = window\.dataLayer \|\| \[\];\s*'
    r'function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*'
    r'gtag\(\'consent\', \'default\', \{\s*'
    r'\'analytics_storage\': \'granted\'\s*'
    r'\}\);\s*'
    r'gtag\(\'js\', new Date\(\)\);\s*'
    r'gtag\(\'config\', \'' + re.escape(GA_ID) + r'\'\);\s*'
    r'</script>',
    re.MULTILINE
)

NEW_GA_BLOCK = f'''<script data-cfasync="false">
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('consent', 'default', {{
        'analytics_storage': 'granted'
      }});
      gtag('js', new Date());
      (function(){{
        try {{
          var ua = navigator.userAgent || '';
          var sw = window.screen ? window.screen.width : 0;
          var sh = window.screen ? window.screen.height : 0;
          var res = sw + 'x' + sh;
          var bs = {{
            '1280x1200': 1,
            '1366x1366': 1,
            '1280x1280': 1,
            '1600x1600': 1,
            '1280x1600': 1,
            '1600x1200': 1,
            '800x600': 1
          }};
          var isBot = navigator.webdriver === true ||
            /HeadlessChrome|PhantomJS|Playwright|Puppeteer|SlimerJS|CasperJS/i.test(ua) ||
            bs[res] === 1 ||
            (sw > 0 && sw === sh);
          if (!isBot) {{
            var c = document.createElement('canvas');
            var gl = c.getContext('webgl') || c.getContext('experimental-webgl');
            if (gl) {{
              var d = gl.getExtension('WEBGL_debug_renderer_info');
              if (d && /SwiftShader|llvmpipe|Software Rasterizer/i.test(gl.getParameter(d.UNMASKED_RENDERER_WEBGL) || '')) {{
                isBot = true;
              }}
            }}
          }}
          if (isBot) {{
            window['ga-disable-{GA_ID}'] = true;
            return;
          }}
        }} catch (_) {{}}
        gtag('config', '{GA_ID}');
      }})();
    </script>'''

def main():
    html_files = glob.glob('pages/**/*.html', recursive=True) + glob.glob('pages/*.html')
    # Deduplicate while preserving order
    seen = set()
    unique_files = []
    for f in html_files:
        norm = os.path.normpath(f)
        if norm not in seen:
            seen.add(norm)
            unique_files.append(norm)

    print(f'Total target HTML files: {len(unique_files)}')
    
    modified_count = 0
    unmatched_files = []

    for path in unique_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        if OLD_GA_PATTERN.search(content):
            # Detect CRLF vs LF
            has_crlf = '\r\n' in content
            target_replacement = NEW_GA_BLOCK.replace('\n', '\r\n') if has_crlf else NEW_GA_BLOCK
            new_content = OLD_GA_PATTERN.sub(target_replacement, content, count=1)
            
            with open(path, 'w', encoding='utf-8', newline='') as fp:
                fp.write(new_content)
            modified_count += 1
        else:
            unmatched_files.append(path)

    print(f'Successfully updated: {modified_count} files.')
    print(f'Unmatched files: {len(unmatched_files)}')
    if unmatched_files:
        print('First 5 unmatched:', unmatched_files[:5])

if __name__ == '__main__':
    main()
