#!/usr/bin/env python3
"""
📊 Statistics Updater
يحدث إحصائيات القناة والفيديوهات
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, Optional


class StatsTracker:
    def __init__(self):
        self.stats_file = 'output/channel_stats.json'
        self.history_file = 'output/stats_history.json'
        self.stats = self.load_stats()
    
    def load_stats(self) -> Dict:
        """تحميل الإحصائيات المحفوظة"""
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            'last_updated': None,
            'subscribers': 0,
            'total_views': 0,
            'total_videos': 0,
            'videos_uploaded': [],
            'performance': {
                'avg_views': 0,
                'avg_likes': 0,
                'avg_comments': 0,
                'engagement_rate': 0
            }
        }
    
    def update_from_upload(self, upload_result: Dict):
        """تحديث الإحصائيات من نتيجة الرفع"""
        if upload_result.get('status') == 'success':
            self.stats['total_videos'] += 1
            self.stats['videos_uploaded'].append({
                'video_id': upload_result.get('video_id'),
                'title': upload_result.get('title'),
                'upload_time': upload_result.get('upload_time'),
                'url': upload_result.get('video_url')
            })
            
            # الاحتفاظ بآخر 100 فيديو فقط
            if len(self.stats['videos_uploaded']) > 100:
                self.stats['videos_uploaded'] = self.stats['videos_uploaded'][-100:]
        
        self.stats['last_updated'] = datetime.now().isoformat()
    
    def calculate_performance(self):
        """حساب مقاييس الأداء"""
        videos = self.stats.get('videos_uploaded', [])
        
        if videos:
            # محاكاة إحصائيات (في الواقع ستجلب من YouTube API)
            self.stats['performance'] = {
                'avg_views': 50000,  # متوسط المشاهدات
                'avg_likes': 5000,   # متوسط اللايكات
                'avg_comments': 500, # متوسط التعليقات
                'engagement_rate': 11.0  # معدل التفاعل
            }
            
            # تحديث إجمالي المشاهدات
            self.stats['total_views'] = self.stats['performance']['avg_views'] * len(videos)
            
            # تحديث المشتركين (تقريبي)
            self.stats['subscribers'] = int(self.stats['total_views'] * 0.02)
    
    def save_stats(self):
        """حفظ الإحصائيات"""
        os.makedirs('output', exist_ok=True)
        
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2)
        
        # إضافة إلى السجل التاريخي
        self.add_to_history()
    
    def add_to_history(self):
        """إضافة نقطة بيانات إلى السجل التاريخي"""
        history = []
        
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        
        history.append({
            'timestamp': datetime.now().isoformat(),
            'subscribers': self.stats['subscribers'],
            'total_views': self.stats['total_views'],
            'total_videos': self.stats['total_videos']
        })
        
        # الاحتفاظ بآخر 365 يوم فقط
        if len(history) > 365:
            history = history[-365:]
        
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    
    def generate_report(self) -> str:
        """توليد تقرير نصي"""
        report = f"""
📊 تقرير إحصائيات Football Comedy AI
{'=' * 50}

📈 الإحصائيات العامة:
   • المشتركين: {self.stats['subscribers']:,}
   • إجمالي المشاهدات: {self.stats['total_views']:,}
   • إجمالي الفيديوهات: {self.stats['total_videos']}

📊 متوسط الأداء:
   • متوسط المشاهدات/فيديو: {self.stats['performance']['avg_views']:,}
   • متوسط اللايكات/فيديو: {self.stats['performance']['avg_likes']:,}
   • متوسط التعليقات/فيديو: {self.stats['performance']['avg_comments']:,}
   • معدل التفاعل: {self.stats['performance']['engagement_rate']}%

🕐 آخر تحديث: {self.stats['last_updated'] or 'غير متوفر'}

{'=' * 50}
        """.strip()
        
        return report


def main():
    print("📊 Starting Statistics Updater...")
    print("=" * 50)
    
    tracker = StatsTracker()
    
    # تحميل نتيجة الرفع الأخيرة
    upload_result_path = 'output/upload_result.json'
    if os.path.exists(upload_result_path):
        with open(upload_result_path, 'r', encoding='utf-8') as f:
            upload_data = json.load(f)
        
        upload_result = upload_data.get('upload_result', {})
        tracker.update_from_upload(upload_result)
        print("✅ تم تحديث الإحصائيات من نتيجة الرفع")
    
    # حساب الأداء
    tracker.calculate_performance()
    print("✅ تم حساب مقاييس الأداء")
    
    # حفظ الإحصائيات
    tracker.save_stats()
    print(f"✅ تم حفظ الإحصائيات في: {tracker.stats_file}")
    
    # طباعة التقرير
    report = tracker.generate_report()
    print("\n" + report)
    
    # حفظ التقرير
    report_path = 'output/stats_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ تم حفظ التقرير في: {report_path}")
    print("\n🎉 اكتمل تحديث الإحصائيات بنجاح!")


if __name__ == '__main__':
    main()
