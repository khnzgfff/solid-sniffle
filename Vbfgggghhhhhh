#!/usr/bin/env python3
"""
⚽ Football Match Data Fetcher
يجلب بيانات المباريات من API-Football
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional

class FootballDataFetcher:
    def __init__(self):
        self.api_key = os.getenv('API_FOOTBALL_KEY')
        self.rapidapi_host = os.getenv('RAPIDAPI_HOST', 'api-football-v1.p.rapidapi.com')
        self.base_url = 'https://api-football-v1.p.rapidapi.com/v3'
        self.headers = {
            'X-RapidAPI-Key': self.api_key,
            'X-RapidAPI-Host': self.rapidapi_host
        }
    
    def get_live_matches(self) -> List[Dict]:
        """جلب المباريات المباشرة الحالية"""
        try:
            response = requests.get(
                f'{self.base_url}/fixtures?live=all',
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data.get('response', [])
        except Exception as e:
            print(f"❌ خطأ في جلب المباريات المباشرة: {e}")
            return []
    
    def get_today_matches(self, league_id: Optional[int] = None) -> List[Dict]:
        """جلب مباريات اليوم"""
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            url = f'{self.base_url}/fixtures?date={today}'
            if league_id:
                url += f'&league={league_id}'
            
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get('response', [])
        except Exception as e:
            print(f"❌ خطأ في جلب مباريات اليوم: {e}")
            return []
    
    def get_match_events(self, fixture_id: int) -> Dict:
        """جلب أحداث مباراة محددة (أهداف، بطاقات، إلخ)"""
        try:
            response = requests.get(
                f'{self.base_url}/fixtures/events?fixture={fixture_id}',
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data.get('response', [])
        except Exception as e:
            print(f"❌ خطأ في جلب أحداث المباراة: {e}")
            return []
    
    def get_match_statistics(self, fixture_id: int) -> Dict:
        """جلب إحصائيات مباراة محددة"""
        try:
            response = requests.get(
                f'{self.base_url}/fixtures/statistics?fixture={fixture_id}',
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data.get('response', [])
        except Exception as e:
            print(f"❌ خطأ في جلب إحصائيات المباراة: {e}")
            return []
    
    def get_top_leagues(self) -> List[Dict]:
        """جلب قائمة أهم الدوريات"""
        top_leagues = [
            {'id': 39, 'name': 'Premier League', 'country': 'England'},
            {'id': 140, 'name': 'La Liga', 'country': 'Spain'},
            {'id': 78, 'name': 'Bundesliga', 'country': 'Germany'},
            {'id': 135, 'name': 'Serie A', 'country': 'Italy'},
            {'id': 61, 'name': 'Ligue 1', 'country': 'France'},
            {'id': 2, 'name': 'Champions League', 'country': 'World'},
        ]
        return top_leagues
    
    def analyze_for_comedy(self, matches: List[Dict]) -> List[Dict]:
        """
        تحليل المباريات للبحث عن لحظات كوميدية محتملة
        """
        comedy_moments = []
        
        for match in matches:
            fixture = match.get('fixture', {})
            teams = match.get('teams', {})
            goals = match.get('goals', {})
            events = self.get_match_events(fixture.get('id'))
            
            # تحليل الأحداث للكوميدية
            comedy_potential = {
                'fixture_id': fixture.get('id'),
                'home_team': teams.get('home', {}).get('name'),
                'away_team': teams.get('away', {}).get('name'),
                'score': f"{goals.get('home')} - {goals.get('away')}",
                'status': fixture.get('status', {}).get('long'),
                'comedy_elements': []
            }
            
            # عد البطاقات الحمراء والصفراء
            red_cards = [e for e in events if e.get('type') == 'Card' and e.get('detail') == 'Red Card']
            yellow_cards = [e for e in events if e.get('type') == 'Card' and e.get('detail') == 'Yellow Card']
            
            if len(red_cards) >= 1:
                comedy_potential['comedy_elements'].append({
                    'type': 'red_card',
                    'count': len(red_cards),
                    'description': f'🟥 {len(red_cards)} بطاقات حمراء - دراما!'
                })
            
            if len(yellow_cards) >= 5:
                comedy_potential['comedy_elements'].append({
                    'type': 'many_yellow_cards',
                    'count': len(yellow_cards),
                    'description': f'🟨 {len(yellow_cards)} بطاقات صفراء - الحكم عصبي!'
                })
            
            # أهداف في الوقت الضائع
            late_goals = [e for e in events if e.get('type') == 'Goal' and e.get('time', {}).get('elapsed', 0) >= 90]
            if late_goals:
                comedy_potential['comedy_elements'].append({
                    'type': 'late_goals',
                    'count': len(late_goals),
                    'description': f'⚽ {len(late_goals)} أهداف في الوقت الضائع!'
                })
            
            # أخطاءOwn Goals
            own_goals = [e for e in events if e.get('type') == 'Goal' and 'Own' in str(e.get('detail', ''))]
            if own_goals:
                comedy_potential['comedy_elements'].append({
                    'type': 'own_goal',
                    'count': len(own_goals),
                    'description': f'😅 {len(own_goals)} أهداف عكسية!'
                })
            
            # نتيجة غير متوقعة
            home_strength = teams.get('home', {}).get('winner')
            away_strength = teams.get('away', {}).get('winner')
            if home_strength is None and away_strength is None and goals.get('home') != goals.get('away'):
                comedy_potential['comedy_elements'].append({
                    'type': 'draw_surprise',
                    'description': '🤝 تعادل مثير!'
                })
            
            # إضافة فقط إذا وجدت عناصر كوميدية
            if comedy_potential['comedy_elements']:
                comedy_moments.append(comedy_potential)
        
        return comedy_moments
    
    def save_match_data(self, data: Dict, filename: str = 'match_data.json'):
        """حفظ بيانات المباريات في ملف JSON"""
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ تم حفظ البيانات في: {filepath}")
        return filepath


def main():
    print("🚀 starting Football Data Fetcher...")
    print("=" * 50)
    
    fetcher = FootballDataFetcher()
    
    # جلب المباريات المباشرة
    print("\n📺 جاري جلب المباريات المباشرة...")
    live_matches = fetcher.get_live_matches()
    print(f"✅ تم العثور على {len(live_matches)} مباراة مباشرة")
    
    # جلب مباريات اليوم
    print("\n📅 جاري جلب مباريات اليوم...")
    today_matches = fetcher.get_today_matches()
    print(f"✅ تم العثور على {len(today_matches)} مباراة اليوم")
    
    # تحليل للكوميدية
    print("\n🎭 جاري تحليل اللحظات الكوميدية...")
    all_matches = live_matches + today_matches
    comedy_moments = fetcher.analyze_for_comedy(all_matches)
    print(f"✅ تم العثور على {len(comedy_moments)} لحظة كوميدية محتملة")
    
    # حفظ البيانات
    match_data = {
        'timestamp': datetime.now().isoformat(),
        'live_matches': live_matches,
        'today_matches': today_matches,
        'comedy_moments': comedy_moments,
        'total_matches': len(all_matches)
    }
    
    fetcher.save_match_data(match_data)
    
    # طباعة ملخص
    print("\n" + "=" * 50)
    print("📊 ملخص البيانات:")
    print(f"   مباريات مباشرة: {len(live_matches)}")
    print(f"   مباريات اليوم: {len(today_matches)}")
    print(f"   لحظات كوميدية: {len(comedy_moments)}")
    
    if comedy_moments:
        print("\n🎭 أبرز اللحظات الكوميدية:")
        for moment in comedy_moments[:3]:
            print(f"   • {moment['home_team']} vs {moment['away_team']}")
            for element in moment['comedy_elements']:
                print(f"     - {element['description']}")
    
    print("\n✅ اكتمل جلب البيانات بنجاح!")


if __name__ == '__main__':
    main()
