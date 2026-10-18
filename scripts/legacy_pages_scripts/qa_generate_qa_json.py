#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成合并的QA JSON文件，实现瞬间加载
"""

import os
import re
import json
import glob
from html.parser import HTMLParser

class QAExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.qa_items = []
        self.current_item = None
        self.in_qa_item = False
        self.in_qa_q = False
        self.in_qa_a = False
        self.in_qa_meta = False
        self.current_tag = None
        self.current_data = []
        self.current_attrs = {}
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'div' and attrs_dict.get('class') == 'qa-item':
            self.in_qa_item = True
            self.current_item = {
                'category': attrs_dict.get('data-category', '其他')
            }
        elif self.in_qa_item:
            if tag in ['div', 'h3'] and attrs_dict.get('class') == 'qa-q':
                self.in_qa_q = True
                self.current_data = []
            elif tag == 'div' and attrs_dict.get('class') == 'qa-a':
                self.in_qa_a = True
                self.current_data = []
            elif tag == 'p' and attrs_dict.get('class') == 'qa-meta':
                self.in_qa_meta = True
                self.current_data = []
        
        self.current_tag = tag
        
    def handle_endtag(self, tag):
        if tag == 'div' and self.in_qa_item and not self.in_qa_q and not self.in_qa_a and not self.in_qa_meta:
            if self.current_item and ('question' in self.current_item or 'answer' in self.current_item):
                self.qa_items.append(self.current_item)
            self.in_qa_item = False
            self.current_item = None
        elif self.in_qa_q and tag in ['div', 'h3']:
            self.in_qa_q = False
            if self.current_item:
                self.current_item['question'] = ''.join(self.current_data)
            self.current_data = []
        elif self.in_qa_a and tag == 'div':
            self.in_qa_a = False
            if self.current_item:
                self.current_item['answer'] = ''.join(self.current_data)
            self.current_data = []
        elif self.in_qa_meta and tag == 'p':
            self.in_qa_meta = False
            if self.current_item:
                self.current_item['meta'] = ''.join(self.current_data)
            self.current_data = []
            
    def handle_data(self, data):
        if self.in_qa_q or self.in_qa_a or self.in_qa_meta:
            self.current_data.append(data)
            
    def handle_entityref(self, name):
        if self.in_qa_q or self.in_qa_a or self.in_qa_meta:
            self.current_data.append(f'&{name};')
            
    def handle_charref(self, name):
        if self.in_qa_q or self.in_qa_a or self.in_qa_meta:
            self.current_data.append(f'&#{name};')

def extract_qa_simple(filepath):
    """简单正则提取QA"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    items = []
    # 匹配 qa-item 块 - 支持有meta和无meta的情况
    # 先尝试匹配带meta的（qa-a内部有span.qa-meta）
    pattern_with_meta = r'<div class="qa-item"[^>]*data-category="([^"]*)"[^>]*>\s*<h3 class="qa-q">(.*?)</h3>\s*<div class="qa-a">(.*?)<span class="qa-meta">(.*?)</span>\s*</div>\s*</div>'
    matches_with_meta = re.findall(pattern_with_meta, content, re.DOTALL)
    
    for category, q_html, a_html, meta_html in matches_with_meta:
        # 清理HTML标签
        question = re.sub(r'<[^>]+>', '', q_html).strip()
        answer = re.sub(r'<[^>]+>', '', a_html).strip()
        meta = re.sub(r'<[^>]+>', '', meta_html).strip()
        
        # 移除问题开头的 ❓
        question = re.sub(r'^❓\s*', '', question)
        
        if question and answer:
            items.append({
                'question': question,
                'answer': answer,
                'meta': meta,
                'category': category or '其他'
            })
    
    # 再匹配不带meta的（旧格式）
    # 找到所有qa-item，排除已经匹配的
    pattern_all = r'<div class="qa-item"[^>]*>\s*<h3 class="qa-q">(.*?)</h3>\s*<div class="qa-a">(.*?)</div>\s*</div>'
    all_matches = re.findall(pattern_all, content, re.DOTALL)
    
    for q_html, a_html in all_matches:
        # 检查这个QA是否已经处理过（有meta的）
        if '<span class="qa-meta">' in a_html:
            continue  # 已经处理过了
        
        # 清理HTML标签
        question = re.sub(r'<[^>]+>', '', q_html).strip()
        answer = re.sub(r'<[^>]+>', '', a_html).strip()
        
        # 移除问题开头的 ❓
        question = re.sub(r'^❓\s*', '', question)
        
        if question and answer:
            items.append({
                'question': question,
                'answer': answer,
                'meta': '',
                'category': '其他'
            })
    
    return items

# 文件来源映射表
SOURCE_MAP = {
    'qa-1.html': '《走向静默，如你本来》',
    'qa-2.html': '《回到你心中》',
    'qa-3.html': '《回到你心中》',
    'qa-4.html': '《以言传意》',
    'qa-5.html': '《以言传意》',
    'qa-6.html': '《宝钻集》',
    'qa-7.html': '《宝钻集》',
    'qa-8.html': '《对谈录》',
    'qa-9.html': '《对谈录》',
    'qa-10.html': '《日日与彼》',
    'qa-11.html': '《日日与彼》',
    'qa-12.html': '《日日与彼》',
    'qa-13.html': '《面对面》',
    'qa-14.html': '《面对面》',
    'qa-15.html': '《秘密印度》',
    'qa-16.html': '《圣者》',
    'qa-17.html': '《马哈希福音》',
    'qa-18.html': '《大瑜伽》',
    'qa-19.html': '《上师言颂》',
    'qa-20.html': '《时代中的永恒》',
    'qa-21.html': '《反思录》',
    'qa-22.html': '《灵性故事》',
    'qa-23.html': '《超越爱与恩典》',
    'qa-24.html': '《桌边碎语》',
    'qa-25.html': '《桌边碎语》',
    'qa-26.html': '《全集》',
    'qa-27.html': '《全集》',
    'qa-28.html': '《全集》',
    'qa-29.html': '《时代中的永恒》',
    'qa-30.html': '《桌边碎语》',
    'qa-31.html': '《桌边碎语》',
    'qa-32.html': '《桌边碎语》',
    'qa-33.html': '《超越爱与恩典》',
    'qa-34.html': '《超越爱与恩典》',
    'qa-35.html': '《超越爱与恩典》',
    'qa-36.html': '《超越爱与恩典》',
    'qa-37.html': '《超越爱与恩典》',
    'qa-38.html': '《超越爱与恩典》',
    'qa-39.html': '《超越爱与恩典》',
    'qa-40.html': '《反思录》',
    'qa-41.html': '《反思录》',
}

def main():
    qa_dir = os.path.dirname(os.path.abspath(__file__))
    all_items = []
    
    # 获取所有qa文件
    qa_files = sorted(glob.glob(os.path.join(qa_dir, 'qa-*.html')))
    
    for filepath in qa_files:
        filename = os.path.basename(filepath)
        items = extract_qa_simple(filepath)
        
        # 为每个item添加来源
        source = SOURCE_MAP.get(filename, '拉玛那马哈希教导')
        for item in items:
            if not item.get('meta'):
                item['meta'] = f'来源：{source}'
        
        all_items.extend(items)
        print(f'✓ {filename}: {len(items)} 条 ({source})')
    
    # 保存为JSON
    output_path = os.path.join(qa_dir, 'qa-data.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    
    print(f'\n总计: {len(all_items)} 条QA')
    print(f'输出: {output_path}')
    print(f'文件大小: {os.path.getsize(output_path) / 1024:.1f} KB')

if __name__ == '__main__':
    main()
