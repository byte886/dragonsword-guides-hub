#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# 图片尺寸
WIDTH = 1000
HEIGHT = 650
MARGIN = 40

# 颜色
BG_COLOR = (245, 245, 245)
CARD_BG = (255, 255, 255)
HEADER_BG = (248, 249, 250)
BORDER_COLOR = (220, 220, 220)
TEXT_COLOR = (51, 51, 51)
LABEL_COLOR = (85, 85, 85)
GREEN = (16, 185, 129)
YELLOW = (245, 158, 11)
RED = (239, 68, 68)
GREEN_BG = (236, 253, 245)
BLUE_BG = (240, 249, 255)
BLUE_TEXT = (3, 105, 161)

# 创建图片
img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# 加载字体
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 24)
    font_header = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 15)
    font_body = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 14)
    font_small = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 13)
except:
    font_title = ImageFont.load_default()
    font_header = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 卡片背景
card_x = MARGIN
card_y = MARGIN
card_w = WIDTH - 2 * MARGIN
card_h = HEIGHT - 2 * MARGIN
draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=12, fill=CARD_BG)

# 标题
title = "3候选游戏词判断表"
title_bbox = draw.textbbox((0, 0), title, font=font_title)
title_w = title_bbox[2] - title_bbox[0]
draw.text(((WIDTH - title_w) // 2, card_y + 30), title, fill=TEXT_COLOR, font=font_title)

# 表格参数
table_top = card_y + 80
table_left = card_x + 30
table_right = card_x + card_w - 30
table_w = table_right - table_left

col_label_w = 160
col_w = (table_w - col_label_w) // 3

rows = [
    "游戏名",
    "Trends 趋势\n（涨/平/跌）",
    "KD 难度",
    "细分关键词数量",
    "首页竞争难度",
    "做/不做"
]

row_heights = [60, 60, 50, 80, 70, 55]

# 绘制表头
header_y = table_top
draw.rectangle([table_left, header_y, table_right, header_y + 45], fill=HEADER_BG)
draw.line([table_left, header_y, table_right, header_y], fill=BORDER_COLOR, width=1)
draw.line([table_left, header_y + 45, table_right, header_y + 45], fill=BORDER_COLOR, width=1)

# 表头文字
headers = ["", "候选词 1", "候选词 2", "候选词 3"]
x = table_left
for i, h in enumerate(headers):
    if i == 0:
        w = col_label_w
    else:
        w = col_w
    text_bbox = draw.textbbox((0, 0), h, font=font_header)
    text_w = text_bbox[2] - text_bbox[0]
    draw.text((x + (w - text_w) // 2, header_y + 13), h, fill=TEXT_COLOR, font=font_header)
    x += w
    if i < 3:
        draw.line([x, header_y, x, header_y + 45], fill=BORDER_COLOR, width=1)

# 绘制行
current_y = header_y + 45
row_data = [
    # 游戏名
    [
        ("blur", "██████████████"),
        ("text", "Mistfall Hunter"),
        ("text", "Corsair Cove")
    ],
    # Trends
    [
        ("text", "涨（健康企稳）"),
        ("text", "涨（爆发式增长）"),
        ("text", "跌（冲高后快速回落）")
    ],
    # KD难度
    [
        ("text", "14（很低）"),
        ("text", "27（较低）"),
        ("text", "18（低）")
    ],
    # 细分关键词数量
    [
        ("text", "多\n（2,436个语句匹配\n77个问题查询）"),
        ("text", "非常多\n（3,234个语句匹配\n197个问题查询）"),
        ("text", "少\n（661个语句匹配\n22个问题查询）")
    ],
    # 首页竞争难度
    [
        ("text", "低\n（0个大站，1个新攻略站）"),
        ("text", "中等偏低\n（0个大站，0个攻略站）"),
        ("text", "中等\n（1个大站Wikipedia）")
    ],
    # 做/不做
    [
        ("do", "✅ 做"),
        ("candidate", "⚠️ 候选（风险高）"),
        ("dont", "❌ 不做")
    ]
]

for row_idx, row in enumerate(rows):
    h = row_heights[row_idx]
    
    # 行背景
    if row_idx == 5:  # 做/不做 行
        draw.rectangle([table_left, current_y, table_right, current_y + h], fill=GREEN_BG)
    elif row_idx % 2 == 1:
        draw.rectangle([table_left, current_y, table_right, current_y + h], fill=(250, 250, 250))
    
    # 左边标签
    draw.rectangle([table_left, current_y, table_left + col_label_w, current_y + h], fill=HEADER_BG)
    lines = row.split('\n')
    total_text_h = len(lines) * 20
    start_y = current_y + (h - total_text_h) // 2
    for li, line in enumerate(lines):
        text_bbox = draw.textbbox((0, 0), line, font=font_body)
        text_w = text_bbox[2] - text_bbox[0]
        draw.text((table_left + (col_label_w - text_w) // 2, start_y + li * 20), line, fill=LABEL_COLOR, font=font_body)
    
    # 三列数据
    x = table_left + col_label_w
    for col_idx, (data_type, text) in enumerate(row_data[row_idx]):
        w = col_w
        
        if data_type == "blur":
            # 模糊化文字
            text_bbox = draw.textbbox((0, 0), text, font=font_body)
            text_w = text_bbox[2] - text_bbox[0]
            text_x = x + (w - text_w) // 2
            text_y = current_y + (h - 20) // 2
            # 先画模糊背景
            draw.rounded_rectangle([text_x - 10, text_y - 5, text_x + text_w + 10, text_y + 25], radius=5, fill=(200, 200, 200))
            # 画模糊文字（用灰色）
            draw.text((text_x, text_y), text, fill=(180, 180, 180), font=font_body)
        elif data_type == "do":
            text_bbox = draw.textbbox((0, 0), text, font=font_body)
            text_w = text_bbox[2] - text_bbox[0]
            draw.text((x + (w - text_w) // 2, current_y + (h - 20) // 2), text, fill=GREEN, font=font_body)
        elif data_type == "candidate":
            text_bbox = draw.textbbox((0, 0), text, font=font_body)
            text_w = text_bbox[2] - text_bbox[0]
            draw.text((x + (w - text_w) // 2, current_y + (h - 20) // 2), text, fill=YELLOW, font=font_body)
        elif data_type == "dont":
            text_bbox = draw.textbbox((0, 0), text, font=font_body)
            text_w = text_bbox[2] - text_bbox[0]
            draw.text((x + (w - text_w) // 2, current_y + (h - 20) // 2), text, fill=RED, font=font_body)
        else:
            # 普通多行文字
            lines = text.split('\n')
            total_text_h = len(lines) * 20
            start_y = current_y + (h - total_text_h) // 2
            for li, line in enumerate(lines):
                text_bbox = draw.textbbox((0, 0), line, font=font_small)
                text_w = text_bbox[2] - text_bbox[0]
                draw.text((x + (w - text_w) // 2, start_y + li * 20), line, fill=TEXT_COLOR, font=font_small)
        
        x += w
        if col_idx < 2:
            draw.line([x, current_y, x, current_y + h], fill=BORDER_COLOR, width=1)
    
    # 底部边框
    draw.line([table_left, current_y + h, table_right, current_y + h], fill=BORDER_COLOR, width=1)
    # 左边框
    draw.line([table_left, current_y, table_left, current_y + h], fill=BORDER_COLOR, width=1)
    # 右边框
    draw.line([table_right, current_y, table_right, current_y + h], fill=BORDER_COLOR, width=1)
    
    current_y += h

# 底部说明
note_top = current_y + 20
note_text = "最终判定：选择候选词1作为主词。理由：口碑好（87%特别好评）、竞争小（仅1个新攻略站DR35）、KD很低（14）、长尾词充足，适合新手长期运营。"
draw.rounded_rectangle([table_left, note_top, table_right, note_top + 60], radius=8, fill=BLUE_BG)

# 自动换行
words = note_text
lines = []
current_line = ""
for char in words:
    test_line = current_line + char
    bbox = draw.textbbox((0, 0), test_line, font=font_small)
    if bbox[2] - bbox[0] > table_w - 30:
        lines.append(current_line)
        current_line = char
    else:
        current_line = test_line
lines.append(current_line)

for i, line in enumerate(lines):
    draw.text((table_left + 15, note_top + 12 + i * 18), line, fill=BLUE_TEXT, font=font_small)

# 保存图片
output_path = "/Users/wenjiechen/Doubao/chats/2026-08-08/new-chat/homework_table.png"
img.save(output_path)
print(f"图片已保存到: {output_path}")
