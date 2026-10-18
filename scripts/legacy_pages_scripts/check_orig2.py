import subprocess

result = subprocess.run(['git', 'show', 'HEAD:pages/concepts/turiya.html'], 
                       capture_output=True, text=True, cwd=r'c:\Users\willp\Desktop\2026年4月\kb01')
content = result.stdout

cw = content.index('content-wrapper')
# Show lines around content-wrapper
lines = content[cw-50:cw+2000].split('\n')
for i, line in enumerate(lines):
    print(f'{i}: {line.rstrip()[:120]}')
