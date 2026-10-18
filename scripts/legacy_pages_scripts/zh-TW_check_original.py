import subprocess, re

# Get original turiya.html from git
result = subprocess.run(['git', 'show', 'HEAD:pages/concepts/turiya.html'], 
                       capture_output=True, text=True, cwd=r'c:\Users\willp\Desktop\2026年4月\kb01')
content = result.stdout

cw = content.index('content-wrapper')
stop = content.find('<footer')
region = content[cw:stop]
lines = region.split('\n')

for i, line in enumerate(lines):
    s = line.strip()
    if '<div' in s or '</div>' in s or '</section>' in s or '<section' in s or '</article>' in s:
        d_o = s.count('<div')
        d_c = s.count('</div>')
        marker = ''
        if d_o or d_c:
            marker = f' div:+{d_o}/-{d_c}'
        print(f'{i}: {s[:90]}{marker}')
