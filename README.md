# ⚽ Football Comedy AI - نظام أتمتة المحتوى الرياضي الكوميدي

<div align="center">

![Football Comedy AI](https://img.shields.io/badge/Football-Comedy-green?style=for-the-badge)
![YouTube Automation](https://img.shields.io/badge/YouTube-Automation-red?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge&logo=github)

**نظام متكامل لإنشاء ونشر محتوى كرة قدم كوميدي تلقائياً**

[الرئيسية](#-about) • [المميزات](#-features) • [التركيب](#-installation) • [الاستخدام](#-usage) • [APIs](#-apis)

</div>

---

## 🎯 About

نظام أتمتة متقدم يستخدم الذكاء الاصطناعي لإنشاء محتوى كرة قدم كوميدي Viral ونشره تلقائياً على يوتيوب عبر GitHub Actions.

### 🚀 كيف يعمل؟

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  API-Football   │ -> │  DeepSeek AI    │ -> │  Gemini AI      │
│  جلب البيانات   │    │  السيناريو      │    │  التحسين        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                                ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Video Creator  │ <- │  Thumbnail      │ <- │  YouTube API    │
│  إنتاج الفيديو  │    │  الصورة المصغرة │    │  الرفع          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## ✨ Features

### 🤖 أتمتة كاملة
- ✅ تشغيل تلقائي كل 6 ساعات عبر GitHub Actions
- ✅ تشغيل يدوي عند الحاجة
- ✅ معالجة الأخطاء تلقائياً

### 🎭 محتوى كوميدي ذكي
- ✅ تحليل المباريات للبحث عن لحظات كوميدية
- ✅ توليد سيناريوهات باللهجة المصرية
- ✅ عناوين Viral جذابة

### 📹 إنتاج احترافي
- ✅ إنشاء صور مصغرة جذابة
- ✅ تحسين SEO للفيديوهات
- ✅ Tags ووصف محسن

### 📊 إحصائيات ومتابعة
- ✅ تقارير أداء مفصلة
- ✅ إشعارات Discord و Telegram
- ✅ تتبع المشاهدات والمشتركين

---

## 📋 Requirements

### الأساسية
- Python 3.11+
- GitHub Account
- YouTube Channel

### APIs المطلوبة
| API | الغرض | الحالة |
|-----|-------|--------|
| YouTube Data API v3 | رفع الفيديوهات | ✅ مطلوب |
| DeepSeek API | توليد السيناريوهات | ✅ مطلوب |
| Gemini API | تحسين المحتوى | ⭕ اختياري |
| API-Football | بيانات المباريات | ✅ مطلوب |

---

## 🔧 Installation

### 1️⃣ استنساخ المشروع

```bash
git clone https://github.com/YOUR_USERNAME/football-comedy-ai.git
cd football-comedy-ai
```

### 2️⃣ تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 3️⃣ إعداد GitHub Secrets

اذهب إلى: **Settings → Secrets and variables → Actions**

وأضف المفاتيح التالية:

```bash
# YouTube API
YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret
YOUTUBE_REFRESH_TOKEN=your_refresh_token

# AI APIs
DEEPSEEK_KEY=your_deepseek_api_key
GEMINI_KEY=your_gemini_api_key

# Football Data
API_FOOTBALL_KEY=your_api_football_key

# Notifications (اختياري)
DISCORD_WEBHOOK=your_discord_webhook
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

### 4️⃣ تفعيل GitHub Actions

```bash
# اذهب إلى Actions في repository الخاص بك
# فعل الـ workflow
```

---

## 🚀 Usage

### التشغيل التلقائي

النظام يعمل تلقائياً كل 6 ساعات حسب الإعداد في `.github/workflows/main.yml`

### التشغيل اليدوي

1. اذهب إلى **Actions** في GitHub
2. اختر **🎬 Football Comedy Auto-Upload**
3. اضغط على **Run workflow**

### تعديل الجدول الزمني

عدل الملف `.github/workflows/main.yml`:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # كل 6 ساعات
    # أمثلة أخرى:
    # - cron: '0 0 * * *'  # يومياً عند منتصف الليل
    # - cron: '0 */3 * * *'  # كل 3 ساعات
```

---

## 📁 Project Structure

```
football-comedy-ai/
├── .github/
│   └── workflows/
│       └── main.yml          # GitHub Actions workflow
├── scripts/
│   ├── fetch_matches.py      # جلب بيانات المباريات
│   ├── generate_script.py    # توليد السيناريو الكوميدي
│   ├── generate_thumbnail.py # إنشاء الصورة المصغرة
│   ├── create_video.py       # إنتاج الفيديو
│   ├── upload_youtube.py     # رفع الفيديو ليوتيوب
│   ├── send_notification.py  # إرسال الإشعارات
│   └── update_stats.py       # تحديث الإحصائيات
├── output/
│   ├── match_data.json       # بيانات المباريات
│   ├── comedy_script.json    # السيناريو المولد
│   ├── thumbnail.jpg         # الصورة المصغرة
│   ├── video.mp4             # الفيديو النهائي
│   └── upload_result.json    # نتيجة الرفع
├── requirements.txt          # المتطلبات
├── README.md                 # هذا الملف
└── index.html                # لوحة التحكم
```

---

## 🔌 APIs

### YouTube Data API v3

**الغرض:** رفع الفيديوهات وإدارة القناة

**الإعداد:**
1. اذهب إلى [Google Cloud Console](https://console.cloud.google.com/)
2. أنشئ مشروع جديد
3. فعل YouTube Data API v3
4. أنشئ OAuth 2.0 Credentials
5. احصل على Refresh Token

### DeepSeek API

**الغرض:** توليد السيناريوهات الكوميدية

**الإعداد:**
1. سجل في [DeepSeek Platform](https://platform.deepseek.com/)
2. أنشئ API Key
3. أضفه إلى GitHub Secrets

### API-Football

**الغرض:** جلب بيانات المباريات

**الإعداد:**
1. سجل في [RapidAPI - API-Football](https://rapidapi.com/api-sports/api/api-football/)
2. اشترك في الخطة المجانية
3. احصل على API Key

---

## ⚠️ Security

### 🔒 حماية المفاتيح

**لا تضع المفاتيح أبداً في الكود!**

✅ افعل:
- استخدم GitHub Secrets
- فعّل 2FA
- حدّث المفاتيح كل 90 يوم

❌ لا تفعل:
- تضع المفاتيح في الكود
- تشارك المفاتيح مع أحد
- تستخدم نفس المفتاح في مشاريع متعددة

### 🛡️ أفضل الممارسات

```bash
# تحقق من أن المفاتيح غير موجودة في الكود
git grep -i "api_key\|secret\|token" -- "*.py"

# تأكد من أن .gitignore يتضمن الملفات الحساسة
echo "*.env" >> .gitignore
echo "credentials.json" >> .gitignore
```

---

## 📊 Performance

### مؤشرات الأداء المستهدفة

| المقياس | الهدف | الحالي |
|---------|-------|--------|
| المشاهدات/شهر | 10M+ | - |
| المشتركين الجدد | 50K/شهر | - |
| معدل التفاعل | 10%+ | - |
| فيديوهات/أسبوع | 7+ | - |

---

## 🐛 Troubleshooting

###常见问题

**❌ فشل المصادقة مع يوتيوب**
```bash
# تأكد من:
1. تفعيل YouTube Data API v3
2. صحة Client ID و Secret
3. وجود Refresh Token صالح
```

**❌ خطأ في جلب بيانات المباريات**
```bash
# تأكد من:
1. صحة API-Football Key
2. عدم تجاوز حد الـ Requests
3. اتصال الإنترنت
```

**❌ فشل توليد السيناريو**
```bash
# تأكد من:
1. صحة مفاتيح AI
2. وجود رصيد في الحساب
3. اتصال APIs
```

---

## 📝 License

هذا المشروع مفتوح المصدر تحت رخصة MIT

---

## 🤝 Contributing

المساهمات مرحب بها! يرجى:

1. Fork المشروع
2. إنشاء Feature Branch
3. Commit التغييرات
4. Push إلى Branch
5. فتح Pull Request

---

## 📞 Support

لللدعم والاستفسارات:
- 📧 Email: support@footballcomedy.ai
- 💬 Discord: [Join Server](#)
- 🐦 Twitter: [@FootballComedyAI](#)

---

## ⭐ Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/football-comedy-ai&type=Date)](https://star-history.com/)

</div>

---

<div align="center">

**صنع بـ ❤️ للمحتوى العربي**

⚽ Football Comedy AI © 2026

</div>
