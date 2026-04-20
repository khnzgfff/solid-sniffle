#!/usr/bin/env python3
"""
📢 Notification Sender
يرسل إشعارات عن حالة الرفع إلى Discord و Telegram
"""

import os
import json
import requests
from datetime import datetime


def send_discord_notification(webhook_url: str, message: dict) -> bool:
    """إرسال إشعار إلى Discord"""
    try:
        embed = {
            'title': message.get('title', '🎬 Football Comedy AI'),
            'description': message.get('description', ''),
            'color': message.get('color', 65280),
            'fields': message.get('fields', []),
            'footer': {
                'text': 'Football Comedy AI System',
                'icon_url': 'https://img.icons8.com/color/48/football.png'
            },
            'timestamp': datetime.now().isoformat()
        }
        
        payload = {
            'embeds': [embed],
            'username': 'Football Comedy Bot',
            'avatar_url': 'https://img.icons8.com/color/48/football.png'
        }
        
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        
        print("✅ تم إرسال إشعار Discord")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في إرسال Discord: {e}")
        return False


def send_telegram_notification(bot_token: str, chat_id: str, message: str) -> bool:
    """إرسال إشعار إلى Telegram"""
    try:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        print("✅ تم إرسال إشعار Telegram")
        return True
        
    except Exception as e:
        print(f"❌ خطأ في إرسال Telegram: {e}")
        return False


def main():
    print("📢 Starting Notification Sender...")
    
    discord_webhook = os.getenv('DISCORD_WEBHOOK')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat = os.getenv('TELEGRAM_CHAT_ID')
    
    # تحميل نتيجة الرفع
    result_path = 'output/upload_result.json'
    if os.path.exists(result_path):
        with open(result_path, 'r', encoding='utf-8') as f:
            upload_result = json.load(f)
        
        upload_info = upload_result.get('upload_result', {})
        success = upload_info.get('status') == 'success'
        
        # رسالة Discord
        discord_message = {
            'title': '✅ تم رفع الفيديو بنجاح!' if success else '❌ فشل رفع الفيديو',
            'description': upload_info.get('title', 'Unknown Video'),
            'color': 65280 if success else 16711680,
            'fields': [
                {'name': '🔗 الرابط', 'value': upload_info.get('video_url', 'N/A'), 'inline': False},
                {'name': '📹 Video ID', 'value': upload_info.get('video_id', 'N/A'), 'inline': True},
                {'name': '⏰ الوقت', 'value': upload_info.get('upload_time', 'N/A'), 'inline': True}
            ]
        }
        
        # رسالة Telegram
        telegram_message = f"""
🎬 <b>Football Comedy AI - تقرير الرفع</b>

{'✅ تم رفع الفيديو بنجاح!' if success else '❌ فشل رفع الفيديو'}

📹 <b>العنوان:</b> {upload_info.get('title', 'Unknown')}
🔗 <b>الرابط:</b> {upload_info.get('video_url', 'N/A')}
⏰ <b>الوقت:</b> {upload_info.get('upload_time', 'N/A')}

#FootballComedy #Automation
        """.strip()
        
        # إرسال الإشعارات
        if discord_webhook:
            send_discord_notification(discord_webhook, discord_message)
        
        if telegram_token and telegram_chat:
            send_telegram_notification(telegram_token, telegram_chat, telegram_message)
    
    else:
        # رسالة افتراضية
        default_message = {
            'title': '⚠️ لم يتم العثور على نتيجة رفع',
            'description': 'تحقق من سجلات GitHub Actions',
            'color': 16776960,
            'fields': []
        }
        
        if discord_webhook:
            send_discord_notification(discord_webhook, default_message)
    
    print("✅ Notification process complete!")


if __name__ == '__main__':
    main()
