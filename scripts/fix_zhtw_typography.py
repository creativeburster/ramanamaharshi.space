# -*- coding: utf-8 -*-
"""
规范化 pages/zh-TW 繁体镜像中的残存简体词与品牌名，提高港台本土化质量
消除 2000+ 处 '拉玛那' -> '拉瑪那'、'阿鲁那' -> '阿魯那' 等半简半繁瑕疵
"""

import os

ZHTW_DIR = r"F:\Ramana\pages\zh-TW"

# 简体遗留词与正体中文严格映射表
TERMS_MAP = {
    "拉玛那": "拉瑪那",
    "阿鲁那": "阿魯那",
    "阿鲁": "阿魯",
    "彻底": "徹底",
    "预加载": "預加載",
    "预解析": "預解析",
    "关键人物": "關鍵人物",
    "大卫·高德曼": "大衛·高德曼",
    "大卫·高德曼": "大衛·高德曼",
    "大卫高德曼": "大衛高德曼",
    "拉玛那马哈希": "拉瑪那馬哈希",
    "拉玛那·马哈希": "拉瑪那·馬哈希",
    "拉玛那知識庫": "拉瑪那知識庫",
    "拉玛那知识库": "拉瑪那知識庫",
}

def process_file(fp):
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    for src, dst in TERMS_MAP.items():
        if src in content:
            content = content.replace(src, dst)

    if content != original:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    modified = 0
    total = 0
    for root, dirs, files in os.walk(ZHTW_DIR):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            if f.lower().endswith('.html'):
                total += 1
                fp = os.path.join(root, f)
                if process_file(fp):
                    modified += 1

    print(f"Scanned {total} zh-TW files, fixed terminology in {modified} files.")

if __name__ == "__main__":
    main()
