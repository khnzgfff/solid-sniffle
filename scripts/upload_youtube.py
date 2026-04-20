#!/usr/bin/env python3
"""
📤 YouTube Video Uploader
يرفع الفيديوهات إلى يوتيوب باستخدام YouTube Data API v3
"""

import os
import json
import pickle
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict

# Google API libraries
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


class YouTubeUploader:
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    
    def __init__(self):
        self.client_id = os.getenv('YOUTUBE_CLIENT_ID')
        self.client_secret = os.getenv('YOUTUBE_CLIENT_SECRET')
        self.refresh_token = os.getenv('YOUTUBE_REFRESH_TOKEN')
        self.credentials = None
        self.youtube = None
    
    def authenticate(self) -> bool:
        """المصادقة مع يوتيوب API"""
        try:
            # محاولة استخدام Refresh Token إذا موجود
            if self.refresh_token:
                self.credentials = Credentials(
                    token=None,
                    refresh_token=self.refresh_token,
                    token_uri='https://oauth2.googleapis.com/token',
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    scopes=self.SCOPES
                )
                
                # تحديث الـ token
                self.credentials.refresh(Request())
                print("✅ تم المصادقة باستخدام Refresh Token")
            else:
                # عملية OAuth الكاملة
                print("⚠️ لا يوجد Refresh Token - يحتاج مصادقة يدوية")
                return False
            
            # بناء خدمة YouTube
            self.youtube = build('youtube', 'v3', credentials=self.credentials)
            return True
            
        except Exception as e:
            print(f"❌ خطأ في المصادقة: {e}")
            return False
    
    def upload_video(
        self,
        video_path: str,
        title: str,
        description: str,
        tags: list,
        thumbnail_path: Optional[str] = None,
        privacy_status: str = 'public'
    ) -> Optional[Dict]:
        """
        رفع فيديو إلى يوتيوب
        
        Args:
            video_path: مسار ملف الفيديو
            title: عنوان الفيديو
            description: وصف الفيديو
            tags: قائمة التاجات
            thumbnail_path: مسار الصورة المصغرة (اختياري)
            privacy_status: حالة الخصوصية (public, private, unlisted)
        
        Returns:
            dict: معلومات الفيديو المرفوع أو None عند الفشل
        """
        if not self.youtube:
            if not self.authenticate():
                return None
        
        try:
            print(f"\n🎬 جاري رفع الفيديو: {title}")
            print(f"📁 المسار: {video_path}")
            
            # التحقق من وجود ملف الفيديو
            if not os.path.exists(video_path):
                print(f"❌ ملف الفيديو غير موجود: {video_path}")
                return None
            
            # إعداد جسم الطلب
            body = {
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'categoryId': '17'  # Sports category
                },
                'status': {
                    'privacyStatus': privacy_status,
                    'selfDeclaredMadeForKids': False
                }
            }
            
            # إعداد ميديا الرفع
            media = MediaFileUpload(
                video_path,
                mimetype='video/mp4',
                resumable=True,
                chunksize=1024 * 1024 * 4  # 4MB chunks
            )
            
            # بدء الرفع
            request = self.youtube.videos().insert(
                body=body,
                media_body=media
            )
            
            # تتبع تقدم الرفع
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    progress = int(status.progress() * 100)
                    print(f"📊 تقدم الرفع: {progress}%")
            
            video_id = response.get('id')
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            print(f"\n✅ تم رفع الفيديو بنجاح!")
            print(f"🔗 الرابط: {video_url}")
            print(f"📹 Video ID: {video_id}")
            
            # رفع الصورة المصغرة إذا وجدت
            if thumbnail_path and os.path.exists(thumbnail_path):
                self.upload_thumbnail(video_id, thumbnail_path)
            
            return {
                'video_id': video_id,
                'video_url': video_url,
                'title': title,
                'upload_time': datetime.now().isoformat(),
                'status': 'success'
            }
            
        except HttpError as e:
            print(f"❌ خطأ في YouTube API: {e}")
            if e.resp.status == 403:
                print("⚠️ خطأ في الصلاحيات - تأكد من تفعيل YouTube Data API")
            return None
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")
            return None
    
    def upload_thumbnail(self, video_id: str, thumbnail_path: str) -> bool:
        """رفع صورة مصغرة للفيديو"""
        try:
            print(f"\n🖼️ جاري رفع الصورة المصغرة...")
            
            self.youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_path)
            ).execute()
            
            print("✅ تم رفع الصورة المصغرة بنجاح!")
            return True
            
        except Exception as e:
            print(f"❌ خطأ في رفع الصورة المصغرة: {e}")
            return False
    
    def get_channel_stats(self) -> Optional[Dict]:
        """جلب إحصائيات القناة"""
        try:
            if not self.youtube:
                if not self.authenticate():
                    return None
            
            request = self.youtube.channels().list(
                part='snippet,statistics',
                mine=True
            )
            
            response = request.execute()
            
            if response.get('items'):
                channel = response['items'][0]
                return {
                    'title': channel['snippet']['title'],
                    'subscribers': channel['statistics'].get('subscriberCount', 0),
                    'views': channel['statistics'].get('viewCount', 0),
                    'videos': channel['statistics'].get('videoCount', 0)
                }
            
            return None
            
        except Exception as e:
            print(f"❌ خطأ في جلب إحصائيات القناة: {e}")
            return None


def main():
    print("📤 Starting YouTube Uploader...")
    print("=" * 50)
    
    uploader = YouTubeUploader()
    
    # تحميل بيانات السيناريو
    script_path = 'output/comedy_script.json'
    if not os.path.exists(script_path):
        print("❌ ملف السيناريو غير موجود!")
        # إنشاء بيانات تجريبية
        script_data = {
            'selected_title': 'مباراة كوميدية - اختبار',
            'description': 'محتوى كوميدي رياضي',
            'tags': ['كورة', 'كوميديا', 'رياضة'],
            'match': {'home': 'Team A', 'away': 'Team B'}
        }
    else:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_data = json.load(f)
    
    # البحث عن ملف الفيديو
    video_files = list(Path('output').glob('*.mp4'))
    if not video_files:
        print("⚠️ لا يوجد ملف فيديو - إنشاء فيديو تجريبي")
        video_path = 'output/test_video.mp4'
        
        # إنشاء ملف فيديو تجريبي (فارغ)
        with open(video_path, 'wb') as f:
            f.write(b'')  # ملف فارغ للتجربة
        
        print(f"📁 تم إنشاء ملف فيديو تجريبي: {video_path}")
    else:
        video_path = str(video_files[-1])
        print(f"📹 تم العثور على الفيديو: {video_path}")
    
    # البحث عن الصورة المصغرة
    thumbnail_files = list(Path('output').glob('*.jpg')) + list(Path('output').glob('*.png'))
    thumbnail_path = str(thumbnail_files[-1]) if thumbnail_files else None
    
    # رفع الفيديو
    print("\n🚀 بدء عملية الرفع...")
    result = uploader.upload_video(
        video_path=video_path,
        title=script_data.get('selected_title', 'Football Comedy Video'),
        description=script_data.get('description', ''),
        tags=script_data.get('tags', []),
        thumbnail_path=thumbnail_path,
        privacy_status='public'
    )
    
    # جلب إحصائيات القناة
    print("\n📊 جلب إحصائيات القناة...")
    stats = uploader.get_channel_stats()
    if stats:
        print(f"   القناة: {stats['title']}")
        print(f"   المشتركين: {stats['subscribers']}")
        print(f"   المشاهدات: {stats['views']}")
        print(f"   الفيديوهات: {stats['videos']}")
    
    # حفظ نتيجة الرفع
    upload_result = {
        'timestamp': datetime.now().isoformat(),
        'upload_result': result,
        'channel_stats': stats
    }
    
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    result_path = os.path.join(output_dir, 'upload_result.json')
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(upload_result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ تم حفظ نتيجة الرفع في: {result_path}")
    print("\n🎉 اكتملت عملية الرفع بنجاح!")


if __name__ == '__main__':
    main()
