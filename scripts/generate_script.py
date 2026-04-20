#!/usr/bin/env python3
"""
🤖 Comedy Script Generator
يولد سيناريوهات كوميدية باستخدام DeepSeek و Gemini AI
"""

import os
import json
import random
import requests
from datetime import datetime
from typing import Dict, List, Optional

class ComedyScriptGenerator:
    def __init__(self):
        self.deepseek_key = os.getenv('DEEPSEEK_KEY')
        self.gemini_key = os.getenv('GEMINI_KEY')
        self.deepseek_url = 'https://api.deepseek.com/v1/chat/completions'
        self.gemini_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
        
        # قوالب كوميدية باللهجة المصرية
        self.comedy_templates = [
            "يا ساتر! {event} ده كان حاجة تانية خالص!",
            "إيه اللي حصل ده؟ {event} في المباراة دي!",
            "الحكم دا رايح فين؟ {event} ودايخ الدنيا!",
            "يا خيبتك! {event} - الموقف ده هيفضل في التاريخ!",
            "مش مصدق اللي شفته! {event} في الكورة!",
            "اللاعب ده عامل إيه؟ {event} - ضحك ولا مصيبة؟",
            "دي مباراة ولا فيلم كوميدي؟ {event}!",
            "يا نهار أبيض! {event} - محدش يتخيل!",
        ]
        
        # نكات جاهزة عن كرة القدم
        self.football_jokes = [
            "الحكم كان شايف الحاجة وهو مش شايفها",
            "اللاعب لعب المباراة وهو بيفكر في الفول",
            "المرمى كان صغير عليه",
            "الكرة كانت زعلانة من اللاعب",
            "التحكيم كان عنده أجندة تانية",
            "المدرب كان بيشجع الفريق التاني",
            "الجمهور كان ألعب من اللاعبين",
        ]
    
    def generate_deepseek_script(self, match_data: Dict) -> str:
        """توليد سيناريو باستخدام DeepSeek"""
        try:
            prompt = f"""
أنت كاتب كوميدي محترف متخصص في المحتوى الرياضي. 
اكتب سيناريو كوميدي قصير (60-90 ثانية) عن مباراة كرة قدم باللهجة المصرية العامية.

بيانات المباراة:
- الفريق الأول: {match_data.get('home_team', 'غير معروف')}
- الفريق الثاني: {match_data.get('away_team', 'غير معروف')}
- النتيجة: {match_data.get('score', 'غير معروف')}
- الأحداث الكوميدية: {json.dumps(match_data.get('comedy_elements', []), ensure_ascii=False)}

المطلوب:
1. مقدمة جذابة (Hook) في أول 3 ثواني
2. سرد كوميدي للأحداث
3. نكت ومواقف مضحكة
4. خاتمة قوية تدعو للتفاعل

اكتب السيناريو فقط بدون أي شروحات إضافية.
استخدم لغة عامية مصرية طبيعية ومضحكة.
            """
            
            headers = {
                'Authorization': f'Bearer {self.deepseek_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'model': 'deepseek-chat',
                'messages': [
                    {'role': 'system', 'content': 'أنت كاتب كوميدي مصري محترف. تكتب محتوى رياضي مضحك viral.'},
                    {'role': 'user', 'content': prompt}
                ],
                'temperature': 0.8,
                'max_tokens': 500
            }
            
            response = requests.post(self.deepseek_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            return data.get('choices', [{}])[0].get('message', {}).get('content', '')
            
        except Exception as e:
            print(f"❌ خطأ في DeepSeek: {e}")
            return self.generate_fallback_script(match_data)
    
    def generate_gemini_script(self, match_data: Dict) -> str:
        """توليد سيناريو باستخدام Gemini"""
        try:
            prompt = f"""
أنت صانع محتوى رياضي كوميدي محترف لليوتيوب.
اكتب نص كوميدي قصير (60-90 ثانية) عن مباراة كرة قدم.

المباراة: {match_data.get('home_team', '')} ضد {match_data.get('away_team', '')}
النتيجة: {match_data.get('score', '')}
الأحداث المثيرة: {match_data.get('comedy_elements', [])}

اكتب:
1. عنوان Viral جذاب
2. نص التعليق الكوميدي
3. 5 hashtags مناسبة

باللهجة المصرية العامية.
            """
            
            headers = {'Content-Type': 'application/json'}
            payload = {
                'contents': [{
                    'parts': [{'text': prompt}]
                }],
                'generationConfig': {
                    'temperature': 0.8,
                    'maxOutputTokens': 500
                }
            }
            
            response = requests.post(
                f'{self.gemini_url}?key={self.gemini_key}',
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            return data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            
        except Exception as e:
            print(f"❌ خطأ في Gemini: {e}")
            return ""
    
    def generate_fallback_script(self, match_data: Dict) -> str:
        """توليد سيناريو بديل عند فشل APIs"""
        home = match_data.get('home_team', 'الفريق الأول')
        away = match_data.get('away_team', 'الفريق الثاني')
        score = match_data.get('score', '0-0')
        
        template = random.choice(self.comedy_templates)
        joke = random.choice(self.football_jokes)
        
        script = f"""
🎬 عنوان: كارثة كروية في مباراة {home} و {away}!

📝 النص:
يا ساتر! المباراة دي كانت حاجة تانية خالص!
{home} ضد {away} والنتيجة {score}... بس اللي حصل ده مش معقول!

{joke}

الحكم كان تايه في الملعب، واللاعبين كانوا بيلعبوا كل واحد لوحده!
الجمهور كان بيشجع واللاعبين كان بيفككوا!

متنسوش اللايك والاشتراك عشان نوصل لـ 100K! 🔥

#كورة #كوميديا #{home.replace(' ', '')} #{away.replace(' ', '')}
        """.strip()
        
        return script
    
    def generate_title_variations(self, match_data: Dict) -> List[str]:
        """توليد عدة عناوين Viral"""
        home = match_data.get('home_team', 'Team1')
        away = match_data.get('away_team', 'Team2')
        score = match_data.get('score', 'X-X')
        
        titles = [
            f"كارثة في مباراة {home} و {away}! النتيجة {score} 😂",
            f"المباراة دي كانت فيلم كوميدي! {home} vs {away}",
            f"مش هتصدق اللي حصل في مباراة {home}! 🤣",
            f"الحكم جنن الدنيا في {home} ضد {away}!",
            f"أغرب مباراة في التاريخ! {score} - {home} و {away}",
            f"اللاعبين دول بيلعبوا ولا بيهزروا؟ 😅 {home} vs {away}",
            f"كارثة تحكيمية! مباراة {home} و {away} من الآخر!",
            f"ضحك ولا مصيبة؟ مباراة {home} الكوميدية!",
        ]
        
        return random.sample(titles, min(5, len(titles)))
    
    def generate_description(self, script: str, match_data: Dict) -> str:
        """توليد وصف محسن لـ SEO"""
        home = match_data.get('home_team', '')
        away = match_data.get('away_team', '')
        
        description = f"""
🔥 مباراة {home} ضد {away} - محتوى كوميدي رياضي!

في الفيديو ده هنشوف أغرف المواقف الكوميدية من المباراة!
لا تنسى اللايك 👍 والاشتراك 🔔 عشان يصلك كل جديد!

📱 تابعنا على:
• TikTok: @footballcomedy
• Instagram: @footballcomedy
• Twitter: @footballcomedy

#كورة #كرة_القدم #كوميديا #رياضة #{home.replace(' ', '_')} #{away.replace(' ', '_')}
#Viral #Trending #Football #Comedy #Sports
        """.strip()
        
        return description
    
    def generate_tags(self, match_data: Dict) -> List[str]:
        """توليد Tags مناسبة"""
        base_tags = [
            'كورة', 'كرة القدم', 'كوميديا', 'رياضة', 'مباراة',
            'Viral', 'Trending', 'Football', 'Comedy', 'Sports',
            'أهداف', 'تحكيم', 'كلاسيكو', 'دوري', 'كأس'
        ]
        
        team_tags = [
            match_data.get('home_team', '').replace(' ', ''),
            match_data.get('away_team', '').replace(' ', ''),
        ]
        
        return base_tags + team_tags
    
    def save_script(self, script_data: Dict, filename: str = 'comedy_script.json'):
        """حفظ السيناريو في ملف"""
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(script_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ تم حفظ السيناريو في: {filepath}")
        return filepath


def main():
    print("🤖 Starting Comedy Script Generator...")
    print("=" * 50)
    
    generator = ComedyScriptGenerator()
    
    # تحميل بيانات المباراة
    match_data_path = 'output/match_data.json'
    if not os.path.exists(match_data_path):
        print("❌ ملف بيانات المباراة غير موجود!")
        # إنشاء بيانات تجريبية
        match_data = {
            'home_team': 'ريال مدريد',
            'away_team': 'برشلونة',
            'score': '2-3',
            'comedy_elements': [
                {'type': 'red_card', 'description': '🟥 بطاقة حمراء مثيرة للجدل'}
            ]
        }
    else:
        with open(match_data_path, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
            comedy_moments = all_data.get('comedy_moments', [])
            if comedy_moments:
                match_data = comedy_moments[0]
            else:
                match_data = {
                    'home_team': 'الفريق أ',
                    'away_team': 'الفريق ب',
                    'score': '1-1',
                    'comedy_elements': []
                }
    
    print(f"\n📝 جاري توليد السيناريو لـ: {match_data.get('home_team')} vs {match_data.get('away_team')}")
    
    # توليد السيناريو
    print("\n🧠 باستخدام DeepSeek AI...")
    deepseek_script = generator.generate_deepseek_script(match_data)
    
    print("\n💎 باستخدام Gemini AI...")
    gemini_script = generator.generate_gemini_script(match_data)
    
    # اختيار أفضل سيناريو
    final_script = deepseek_script if len(deepseek_script) > len(gemini_script) else gemini_script
    if not final_script:
        final_script = generator.generate_fallback_script(match_data)
    
    # توليد العناوين
    print("\n🎯 جاري توليد العناوين...")
    titles = generator.generate_title_variations(match_data)
    
    # توليد الوصف
    print("\n📝 جاري توليد الوصف...")
    description = generator.generate_description(final_script, match_data)
    
    # توليد التاجات
    tags = generator.generate_tags(match_data)
    
    # حفظ البيانات
    script_data = {
        'timestamp': datetime.now().isoformat(),
        'match': {
            'home': match_data.get('home_team'),
            'away': match_data.get('away_team'),
            'score': match_data.get('score')
        },
        'script': final_script,
        'titles': titles,
        'selected_title': titles[0],
        'description': description,
        'tags': tags,
        'duration_seconds': 75
    }
    
    generator.save_script(script_data)
    
    # طباعة الملخص
    print("\n" + "=" * 50)
    print("📊 ملخص السيناريو:")
    print(f"   العنوان: {titles[0]}")
    print(f"   المدة: {script_data['duration_seconds']} ثانية")
    print(f"   عدد التاجات: {len(tags)}")
    print(f"\n📝 بداية السيناريو:")
    print(final_script[:200] + "..." if len(final_script) > 200 else final_script)
    
    print("\n✅ اكتمل توليد السيناريو بنجاح!")


if __name__ == '__main__':
    main()
