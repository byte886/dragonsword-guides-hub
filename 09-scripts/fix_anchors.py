#!/usr/bin/env python3
"""
自动给角色详情页的h2标题添加侧边栏锚点对应的id
"""
import re
import os
import glob

def add_anchor_ids(filepath):
    """给单个HTML文件添加锚点id"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到侧边栏中的所有锚点链接: <a href="#xxx">文本</a>
    sidebar_pattern = re.compile(r'<a href="#([a-zA-Z0-9_-]+)">([^<]+)</a>')
    anchors = sidebar_pattern.findall(content)
    
    if not anchors:
        return 0
    
    modified = 0
    used_ids = set()
    
    for anchor_id, anchor_text in anchors:
        if anchor_id in used_ids:
            continue
        used_ids.add(anchor_id)
        
        # 清理锚点文本（去掉emoji、空格等）
        clean_anchor = re.sub(r'[^\w\u4e00-\u9fff\uac00-\ud7af\u3040-\u30ff\u0400-\u04ff]', '', anchor_text).lower()
        
        # 找到所有h2标题
        h2_pattern = re.compile(r'<h2>([^<]+)</h2>')
        h2_matches = list(h2_pattern.finditer(content))
        
        best_match = None
        best_score = 0
        
        for h2_match in h2_matches:
            h2_text = h2_match.group(1)
            # 清理h2文本
            clean_h2 = re.sub(r'[^\w\u4e00-\u9fff\uac00-\ud7af\u3040-\u30ff\u0400-\u04ff]', '', h2_text).lower()
            
            # 计算匹配分数
            score = 0
            if clean_anchor in clean_h2:
                score = 100
            elif clean_h2 in clean_anchor:
                score = 90
            else:
                # 计算公共字符
                common = len(set(clean_anchor) & set(clean_h2))
                score = common * 10
            
            if score > best_score and score >= 30:
                best_score = score
                best_match = h2_match
        
        if best_match and best_score >= 30:
            h2_text = best_match.group(0)
            # 检查是否已经有id
            if 'id=' not in h2_text:
                new_h2 = f'<h2 id="{anchor_id}">{best_match.group(1)}</h2>'
                content = content.replace(h2_text, new_h2, 1)
                modified += 1
    
    if modified > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return modified

def main():
    base_dir = '/Users/wenjiechen/Doubao/chats/2026-08-08/new-chat/dragonsword-guides'
    character_pages = ['lute', 'theresia', 'charlotte', 'reina']
    languages = ['en', 'zh', 'ko', 'ru', 'ja']
    
    total_modified = 0
    for lang in languages:
        for page in character_pages:
            filepath = os.path.join(base_dir, lang, f'{page}.html')
            if os.path.exists(filepath):
                count = add_anchor_ids(filepath)
                if count > 0:
                    print(f'  {lang}/{page}.html: 添加了 {count} 个id')
                    total_modified += count
    
    print(f'\n总计添加了 {total_modified} 个锚点id')

if __name__ == '__main__':
    main()
