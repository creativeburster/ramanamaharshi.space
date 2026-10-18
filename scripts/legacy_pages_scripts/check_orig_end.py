import subprocess

result = subprocess.run(['git', 'show', 'HEAD:pages/concepts/turiya.html'], 
                       capture_output=True, text=True, cwd=r'c:\Users\willp\Desktop\2026年4月\kb01')
content = result.stdout

lines = content.split('\n')
# Show last 30 lines
for i in range(max(0, len(lines)-30), len(lines)):
    print(f'{i+1}: {lines[i].rstrip()[:120]}')
