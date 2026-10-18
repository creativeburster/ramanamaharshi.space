#!/usr/bin/env python3
"""
KB01 性能优化脚本 - 更新所有HTML文件（包括子目录）的CSS/JS引用
"""
import re
import os
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")

def update_all_html_references():
    """更新所有HTML文件中的JS/CSS引用"""
    html_files = list(KB01.glob("**/*.html"))
    updated = 0
    errors = []

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # 判断相对路径深度
            depth = len(html_file.relative_to(KB01).parts) - 1
            prefix = "../" * depth if depth > 0 else ""

            # 替换 styles.css 为 styles.min.css
            content = re.sub(
                rf'href=["\']\.\./\*styles\.css["\']',
                f'href="{prefix}styles.min.css"',
                content
            )
            content = re.sub(
                rf'href=["\']styles\.css["\']',
                f'href="{prefix}styles.min.css"',
                content
            )

            # 移除旧的script标签
            content = re.sub(
                r'<script\s+[^>]*src=["\'][^"\']*script\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )
            content = re.sub(
                r'<script\s+[^>]*src=["\'][^"\']*search\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )
            content = re.sub(
                r'<script\s+[^>]*src=["\'][^"\']*app\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )

            # 添加bundle.min.js（在</body>前，如果还没有的话）
            if 'bundle.min.js' not in content:
                # 检查是否已经有任何defer脚本
                if 'defer' in content:
                    # 在最后一个defer脚本后添加
                    content = re.sub(
                        r'(<script[^>]*defer[^>]*></script>\s*)',
                        rf'\1<script src="{prefix}bundle.min.js" defer></script>\n',
                        content
                    )
                else:
                    content = content.replace(
                        '</body>',
                        f'<script src="{prefix}bundle.min.js" defer></script>\n</body>'
                    )

            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1

        except Exception as e:
            errors.append((str(html_file), str(e)))

    return updated, errors

def main():
    print("🔄 更新所有HTML文件引用...")

    updated, errors = update_all_html_references()

    print(f"   ✅ 更新了 {updated} 个HTML文件")

    if errors:
        print(f"   ⚠️ {len(errors)} 个文件出错:")
        for path, err in errors[:5]:
            print(f"      - {path}: {err}")

if __name__ == "__main__":
    main()
