import os

def fix_favicon_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 正确的favicon
    correct_favicon = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'%3E%3Ctext y=\'.9em\' font-size=\'90\'%3E🙏%3C/text%3E%3C/svg%3E">'
    
    # 检查是否有错误的favicon
    modified = False
    if '🙏</text></svg>' in content and 'link rel="icon"' in content:
        # 查找包含favicon的行
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'link rel="icon"' in line and '🙏</text></svg>' in line:
                # 替换为正确的favicon
                new_lines.append(correct_favicon)
                if line != correct_favicon:
                    modified = True
            else:
                new_lines.append(line)
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"Fixed favicon in {file_path}")
            return True
    
    return False

def main():
    pages_dir = '.'
    files_to_check = []
    
    # 收集所有HTML文件
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                files_to_check.append(os.path.join(root, file))
    
    fixed_count = 0
    for file_path in files_to_check:
        if fix_favicon_in_file(file_path):
            fixed_count += 1
    
    print(f"\nFixed favicon in {fixed_count} files")

if __name__ == '__main__':
    main()
