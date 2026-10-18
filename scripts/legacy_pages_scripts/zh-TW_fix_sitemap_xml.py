import os
import re

def fix_sitemap_xml():
    sitemap_path = 'sitemap.xml'
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义需要处理的模式
    patterns = [
        # 处理普通页面（如 /graph -> /graph.html）
        (r'https://ramanamaharshi\.space/(graph|methods|persons|qa)(?=</loc>)', r'https://ramanamaharshi.space/\1.html'),
        # 处理书籍页面（如 /books/back-to-heart/ -> /books/back-to-heart.html）
        (r'https://ramanamaharshi\.space/books/([^/]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        # 处理概念页面（如 /concepts/atman/ -> /concepts/atman.html）
        (r'https://ramanamaharshi\.space/concepts/([^/]+)/(?=</loc>)', r'https://ramanamaharshi.space/concepts/\1.html'),
        # 处理人物页面（如 /persons/ramana/ -> /persons/ramana.html）
        (r'https://ramanamaharshi\.space/persons/([^/]+)/(?=</loc>)', r'https://ramanamaharshi.space/persons/\1.html'),
        # 处理书籍章节页面（如 /books/back-to-heart-ch1/ -> /books/back-to-heart-ch1.html）
        (r'https://ramanamaharshi\.space/books/([^/]+)-ch[0-9]+/(?=</loc>)', r'https://ramanamaharshi.space/books/\1-ch[0-9]+.html'),
        # 处理gems章节页面（如 /books/gems-ch1/ -> /books/gems-ch1.html）
        (r'https://ramanamaharshi\.space/books/gems-ch[0-9]+/(?=</loc>)', r'https://ramanamaharshi.space/books/gems-ch[0-9]+.html'),
        # 处理问答页面（如 /qa/qa-1/ -> /qa/qa-1.html）
        (r'https://ramanamaharshi\.space/qa/qa-[0-9]+/(?=</loc>)', r'https://ramanamaharshi.space/qa/qa-[0-9]+.html'),
    ]
    
    # 应用所有替换
    modified = False
    for pattern, replacement in patterns:
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            modified = True
    
    # 特殊处理 /books 页面
    content = re.sub(r'https://ramanamaharshi\.space/books(?=</loc>)', r'https://ramanamaharshi.space/books/index.html', content)
    # 特殊处理 /concepts 页面
    content = re.sub(r'https://ramanamaharshi\.space/concepts(?=</loc>)', r'https://ramanamaharshi.space/concepts/index.html', content)
    # 特殊处理 /qa 页面
    content = re.sub(r'https://ramanamaharshi\.space/qa(?=</loc>)', r'https://ramanamaharshi.space/qa/index.html', content)
    # 特殊处理 /persons 页面
    content = re.sub(r'https://ramanamaharshi\.space/persons(?=</loc>)', r'https://ramanamaharshi.space/persons/index.html', content)
    # 特殊处理 /methods 页面
    content = re.sub(r'https://ramanamaharshi\.space/methods(?=</loc>)', r'https://ramanamaharshi.space/methods/index.html', content)
    # 特殊处理 /graph 页面
    content = re.sub(r'https://ramanamaharshi\.space/graph(?=</loc>)', r'https://ramanamaharshi.space/graph.html', content)
    
    # 处理具体的章节页面
    chapter_patterns = [
        (r'https://ramanamaharshi\.space/books/(back-to-heart-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(be-as-you-are-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(crumbs-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(gems-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(reflections-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(spiritual-stories-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(surpassing-love-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(talks-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(teachings-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/books/(timeless-ch[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/books/\1.html'),
        (r'https://ramanamaharshi\.space/qa/(qa-[0-9]+)/(?=</loc>)', r'https://ramanamaharshi.space/qa/\1.html'),
    ]
    
    for pattern, replacement in chapter_patterns:
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            modified = True
    
    if modified:
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed sitemap.xml")
        return True
    return False

def main():
    if fix_sitemap_xml():
        print("Sitemap.xml has been updated with .html extensions")
    else:
        print("No changes needed for sitemap.xml")

if __name__ == '__main__':
    main()
