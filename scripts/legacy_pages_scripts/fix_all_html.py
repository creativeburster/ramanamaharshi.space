#!/usr/bin/env python3
"""
KB01 性能优化脚本 - 完整更新所有HTML文件
"""
import re
import os
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")

def update_all_html():
    """更新所有HTML文件"""
    html_files = list(KB01.glob("**/*.html"))
    updated = 0

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # 判断相对路径深度
            depth = len(html_file.relative_to(KB01).parts) - 1
            prefix = "../" * depth if depth > 0 else ""

            # 1. 替换 CSS 引用
            # styles.css -> styles.min.css
            content = re.sub(
                rf'href=["\']\.\./\*styles\.css["\']',
                f'href="{prefix}styles.min.css"',
                content
            )
            content = re.sub(
                r'href=["\'][^"\']*styles\.css["\']',
                f'href="{prefix}styles.min.css"',
                content
            )

            # 2. 替换 preload 引用
            # app.js -> bundle.min.js
            content = re.sub(
                r'href=["\'][^"\']*app\.js["\']',
                f'href="{prefix}bundle.min.js"',
                content
            )
            content = re.sub(
                r'href=["\'][^"\']*script\.js["\']',
                f'href="{prefix}bundle.min.js"',
                content
            )
            content = re.sub(
                r'href=["\'][^"\']*search\.js["\']',
                f'href="{prefix}bundle.min.js"',
                content
            )

            # 3. 移除旧的 script 标签并添加 bundle.min.js
            # 先移除
            content = re.sub(
                r'<script[^>]*src=["\'][^"\']*app\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )
            content = re.sub(
                r'<script[^>]*src=["\'][^"\']*script\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )
            content = re.sub(
                r'<script[^>]*src=["\'][^"\']*search\.js["\'][^>]*>\s*</script>\s*',
                '',
                content
            )

            # 如果没有 bundle.min.js，添加它
            if 'bundle.min.js' not in content:
                content = content.replace(
                    '</body>',
                    f'<script src="{prefix}bundle.min.js" defer></script>\n</body>'
                )
                # 也替换所有 styles.css 为 styles.min.css
                content = content.replace('styles.css', 'styles.min.css')

            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1

        except Exception as e:
            print(f"Error: {html_file}: {e}")

    return updated

def main():
    print("🔄 更新所有HTML文件...")

    updated = update_all_html()

    print(f"✅ 更新了 {updated} 个HTML文件")

    # 验证
    sample = KB01 / "books/be-as-you-are.html"
    with open(sample, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n📋 验证示例 ({sample.name}):")
    print(f"   styles.min.css: {'✅' if 'styles.min.css' in content else '❌'}")
    print(f"   bundle.min.js: {'✅' if 'bundle.min.js' in content else '❌'}")
    print(f"   styles.css (旧): {'❌ 有残留' if 'href=\"../styles.css\"' in content else '✅ 已清除'}")

if __name__ == "__main__":
    main()
