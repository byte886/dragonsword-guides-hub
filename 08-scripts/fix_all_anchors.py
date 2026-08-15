#!/usr/bin/env python3
"""
自动给所有HTML页面的h2/h3标题添加侧边栏锚点对应的id
"""
import re
import os

def add_anchor_ids(filepath):
    """给单个HTML文件添加锚点id"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有锚点链接: <a href="#xxx">文本</a>
    anchor_pattern = re.compile(r'<a href="#([a-zA-Z0-9_-]+)">([^<]+)</a>')
    anchors = anchor_pattern.findall(content)
    
    if not anchors:
        return 0
    
    modified = 0
    used_ids = set()
    
    for anchor_id, anchor_text in anchors:
        if anchor_id in used_ids:
            continue
        # 检查是否已经有这个id
        if f'id="{anchor_id}"' in content:
            used_ids.add(anchor_id)
            continue
        used_ids.add(anchor_id)
        
        # 清理锚点文本（去掉emoji、空格、特殊字符）
        clean_anchor = re.sub(r'[^\w\u4e00-\u9fff\uac00-\ud7af\u3040-\u30ff\u0400-\u04ff]', '', anchor_text).lower()
        
        if not clean_anchor:
            continue
        
        # 找到所有h2和h3标题
        heading_pattern = re.compile(r'<h([23])>([^<]+)</h\1>')
        headings = list(heading_pattern.finditer(content))
        
        best_match = None
        best_score = 0
        
        for heading_match in headings:
            heading_text = heading_match.group(2)
            level = heading_match.group(1)
            # 清理标题文本
            clean_heading = re.sub(r'[^\w\u4e00-\u9fff\uac00-\ud7af\u3040-\u30ff\u0400-\u04ff]', '', heading_text).lower()
            
            if not clean_heading:
                continue
            
            # 计算匹配分数
            score = 0
            if clean_anchor == clean_heading:
                score = 200
            elif clean_anchor in clean_heading:
                score = 150
            elif clean_heading in clean_anchor:
                score = 140
            else:
                # 计算公共字符比例
                common = len(set(clean_anchor) & set(clean_heading))
                score = common * 8
            
            # h2比h3优先
            if level == '2':
                score += 10
            
            if score > best_score and score >= 25:
                best_score = score
                best_match = heading_match
        
        if best_match and best_score >= 25:
            full_match = best_match.group(0)
            level = best_match.group(1)
            heading_text = best_match.group(2)
            # 检查是否已经有id
            if 'id=' not in full_match:
                new_heading = f'<h{level} id="{anchor_id}">{heading_text}</h{level}>'
                content = content.replace(full_match, new_heading, 1)
                modified += 1
    
    if modified > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return modified

def main():
    base_dir = '/Users/wenjiechen/Doubao/chats/2026-08-08/new-chat/dragonsword-guides'
    languages = ['en', 'zh', 'ko', 'ru', 'ja']
    
    total_modified = 0
    total_pages = 0
    
    for lang in languages:
        lang_dir = os.path.join(base_dir, lang)
        if not os.path.exists(lang_dir):
            continue
        
        for filename in sorted(os.listdir(lang_dir)):
            if not filename.endswith('.html'):
                continue
            
            filepath = os.path.join(lang_dir, filename)
            count = add_anchor_ids(filepath)
            if count > 0:
                print(f'  {lang}/{filename}: 添加了 {count} 个id')
                total_modified += count
                total_pages += 1
    
    # 也处理根目录的index.html
    index_file = os.path.join(base_dir, 'index.html')
    if os.path.exists(index_file):
        count = add_anchor_ids(index_file)
        if count > 0:
            print(f'  index.html: 添加了 {count} 个id')
            total_modified += count
            total_pages += 1
    
    print(f'\n共处理 {total_pages} 个页面，添加了 {total_modified} 个锚点id')

if __name__ == '__main__':
    main()
