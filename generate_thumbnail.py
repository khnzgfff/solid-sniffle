#!/usr/bin/env python3
"""
🖼️ Thumbnail Generator
ينشئ صور مصغرة جذابة للفيديوهات
"""

import os
import json
import random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def create_thumbnail(match_data: dict, script_data: dict):
    """إنشاء صورة مصغرة جذابة"""
    
    # إعدادات الصورة
    width, height = 1280, 720
    background_color = (20, 20, 40)
    
    # إنشاء الصورة
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # إضافة تدرج لوني
    for y in range(height):
        alpha = int(255 * (y / height))
        color = (20 + alpha//10, 20 + alpha//10, 40 + alpha//5)
        draw.line([(0, y), (width, y)], fill=color)
    
    # النص الرئيسي
    home_team = match_data.get('home_team', 'Team 1')
    away_team = match_data.get('away_team', 'Team 2')
    score = match_data.get('score', '0-0')
    
    # عناوين جذابة
    titles = [
        "كارثة كروية! 😱",
        "مش هتصدق! 🤣",
        "فضيحة التحكيم! ⚽",
        "أغرب مباراة! 🔥",
        "ضحك ولا مصيبة؟ 😂"
    ]
    
    main_title = random.choice(titles)
    
    # محاولة استخدام خط عربي
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # رسم العنوان الرئيسي
    title_text = main_title
    title_bbox = draw.textbbox((0, 0), title_text, font=font_large)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 100), title_text, fill=(255, 255, 255), font=font_large)
    
    # رسم اسمي الفريقين
    teams_text = f"{home_team} vs {away_team}"
    teams_bbox = draw.textbbox((0, 0), teams_text, font=font_medium)
    teams_width = teams_bbox[2] - teams_bbox[0]
    teams_x = (width - teams_width) // 2
    draw.text((teams_x, 250), teams_text, fill=(0, 255, 135), font=font_medium)
    
    # رسم النتيجة
    score_text = f"النتيجة: {score}"
    score_bbox = draw.textbbox((0, 0), score_text, font=font_large)
    score_width = score_bbox[2] - score_bbox[0]
    score_x = (width - score_width) // 2
    draw.text((score_x, 350), score_text, fill=(255, 65, 108), font=font_large)
    
    # إضافة عناصر زخرفية
    # دائرة في الزاوية
    draw.ellipse([50, 50, 150, 150], outline=(0, 255, 135), width=5)
    draw.ellipse([width-150, height-150, width-50, height-50], outline=(255, 65, 108), width=5)
    
    # خطوط زخرفية
    draw.line([(0, height//2), (width, height//2)], fill=(0, 255, 135, 128), width=2)
    
    # حفظ الصورة
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    thumbnail_path = os.path.join(output_dir, 'thumbnail.jpg')
    img.save(thumbnail_path, 'JPEG', quality=95)
    
    print(f"✅ تم إنشاء الصورة المصغرة: {thumbnail_path}")
    return thumbnail_path


def main():
    print("🖼️ Starting Thumbnail Generator...")
    
    # تحميل البيانات
    match_data_path = 'output/match_data.json'
    if os.path.exists(match_data_path):
        with open(match_data_path, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
            comedy_moments = all_data.get('comedy_moments', [])
            match_data = comedy_moments[0] if comedy_moments else {}
    else:
        match_data = {
            'home_team': 'ريال مدريد',
            'away_team': 'برشلونة',
            'score': '2-3'
        }
    
    script_data = {}
    script_path = 'output/comedy_script.json'
    if os.path.exists(script_path):
        with open(script_path, 'r', encoding='utf-8') as f:
            script_data = json.load(f)
    
    # إنشاء الصورة المصغرة
    create_thumbnail(match_data, script_data)
    
    print("✅ Thumbnail generation complete!")


if __name__ == '__main__':
    main()
