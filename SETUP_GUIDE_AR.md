# 🚀 دليل الإعداد الكامل - Football Comedy AI

<div align="center">

**دليل خطوة بخطوة لإعداد نظام أتمتة المحتوى الرياضي الكوميدي**

⏱️ الوقت المتوقع: 15-20 دقيقة

</div>

---

## 📋 المتطلبات المسبقة

قبل البدء، تأكد من وجود:

- ✅ حساب GitHub
- ✅ قناة يوتيوب
- ✅ بريد إلكتروني للتسجيل في الخدمات
- ✅ 15-20 دقيقة من الوقت

---

## 🔑 المرحلة 1: إعداد APIs

### 1️⃣ YouTube Data API v3

**الخطوات:**

1. اذهب إلى [Google Cloud Console](https://console.cloud.google.com/)

2. أنشئ مشروع جديد:
   ```
   اسم المشروع: Football Comedy AI
   ```

3. فعل YouTube Data API v3:
   - اذهب إلى "APIs & Services" → "Library"
   - ابحث عن "YouTube Data API v3"
   - اضغط "Enable"

4. أنشئ OAuth 2.0 Credentials:
   - اذهب إلى "APIs & Services" → "Credentials"
   - اضغط "Create Credentials" → "OAuth client ID"
   - اختر "Web application"
   - أضف Redirect URI: `http://localhost`
   - احفظ Client ID و Client Secret

5. احصل على Refresh Token:
   ```bash
   # استخدم هذا الرابط (استبدل YOUR_CLIENT_ID)
   https://accounts.google.com/o/oauth2/auth?
   client_id=YOUR_CLIENT_ID&
   redirect_uri=http://localhost&
   scope=https://www.googleapis.com/auth/youtube.upload&
   response_type=code&
   access_type=offline
   ```
   
   - بعد الموافقة، انسخ الـ code من URL
   - استخدمه للحصول على Refresh Token

---

### 2️⃣ DeepSeek API

**الخطوات:**

1. اذهب إلى [DeepSeek Platform](https://platform.deepseek.com/)

2. سجل حساب جديد

3. اذهب إلى "API Keys"

4. أنشئ API Key جديد

5. انسخ المفتاح واحفظه في مكان آمن

**التكلفة:**
- الخطة المجانية: 1M tokens شهرياً
- كافية لـ ~500 سيناريو شهرياً

---

### 3️⃣ Gemini API (Google AI Studio)

**الخطوات:**

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/)

2. سجل الدخول بحساب Google

3. اضغط "Get API Key"

4. أنشئ مفتاح جديد

5. انسخ المفتاح

**التكلفة:**
- مجاني حتى 60 طلب/دقيقة
- كافٍ للاستخدام الشخصي

---

### 4️⃣ API-Football (RapidAPI)

**الخطوات:**

1. اذهب إلى [API-Football على RapidAPI](https://rapidapi.com/api-sports/api/api-football/)

2. سجل حساب RapidAPI (مجاني)

3. اشترك في الخطة المجانية:
   - 100 طلب/يوم
   - كافٍ لـ 10-15 تحديث يومياً

4. انسخ API Key من صفحة الـ Subscription

---

## 🔧 المرحلة 2: إعداد GitHub Repository

### 1️⃣ إنشاء Repository

```bash
# على GitHub.com
1. اضغط "+" → "New repository"
2. الاسم: football-comedy-ai
3. الوصف: Automated Football Comedy Content System
4. Public أو Private (يفضل Private للمفاتيح)
5. اضغط "Create repository"
```

### 2️⃣ رفع الملفات

```bash
# في جهازك المحلي
git clone https://github.com/YOUR_USERNAME/football-comedy-ai.git
cd football-comedy-ai

# انسخ جميع الملفات إلى المجلد
# (.github, scripts, index.html, README.md, etc.)

git add .
git commit -m "Initial commit - Football Comedy AI System"
git push origin main
```

### 3️⃣ إعداد GitHub Secrets

1. اذهب إلى Repository → Settings

2. اضغط "Secrets and variables" → "Actions"

3. اضغط "New repository secret"

4. أضف المفاتيح التالية واحداً تلو الآخر:

| الاسم | القيمة |
|-------|--------|
| `YOUTUBE_CLIENT_ID` | Client ID من Google Cloud |
| `YOUTUBE_CLIENT_SECRET` | Client Secret من Google Cloud |
| `YOUTUBE_REFRESH_TOKEN` | Refresh Token من OAuth |
| `DEEPSEEK_KEY` | مفتاح DeepSeek API |
| `GEMINI_KEY` | مفتاح Gemini API |
| `API_FOOTBALL_KEY` | مفتاح API-Football |

**اختياري - للإشعارات:**

| الاسم | القيمة |
|-------|--------|
| `DISCORD_WEBHOOK` | Webhook من Discord Server |
| `TELEGRAM_BOT_TOKEN` | Token من BotFather |
| `TELEGRAM_CHAT_ID` | ID من Telegram Chat |

---

## ⚙️ المرحلة 3: تفعيل GitHub Actions

### 1️⃣ تفعيل Actions

1. اذهب إلى Repository → Actions

2. إذا ظهر تحذير، اضغط "I understand my workflows, go ahead and enable them"

### 2️⃣ التشغيل الأول

1. اضغط على workflow "🎬 Football Comedy Auto-Upload"

2. اضغط "Run workflow" → "Run workflow"

3. انتظر 2-5 دقائق لاكتمال التشغيل

### 3️⃣ مراقبة التنفيذ

1. اضغط على الـ run الجارى

2. راقب كل خطوة:
   - ✅ Checkout repository
   - ✅ Setup Python
   - ✅ Install dependencies
   - ✅ Fetch Match Data
   - ✅ Generate Comedy Script
   - ✅ Generate Thumbnail
   - ✅ Create Video
   - ✅ Upload to YouTube
   - ✅ Update Statistics

---

## 🎯 المرحلة 4: التخصيص

### تعديل جدول النشر

افتح `.github/workflows/main.yml` وعدل:

```yaml
on:
  schedule:
    # كل 6 ساعات (الافتراضي)
    - cron: '0 */6 * * *'
    
    # يومياً عند منتصف الليل
    # - cron: '0 0 * * *'
    
    # كل 3 ساعات
    # - cron: '0 */3 * * *'
    
    # كل ساعة
    # - cron: '0 * * * *'
```

### تخصيص المحتوى

افتح `scripts/generate_script.py` وعدل:

```python
# قوالب كوميدية إضافية
self.comedy_templates = [
    "يا ساتر! {event} ده كان حاجة تانية خالص!",
    # أضف قوالبك الخاصة هنا
]

# نكات مخصصة
self.football_jokes = [
    "الحكم كان شايف الحاجة وهو مش شايفها",
    # أضف نكاتك الخاصة هنا
]
```

---

## 📊 المرحلة 5: المتابعة والتحسين

### متابعة الأداء

1. **YouTube Studio:**
   - راقب المشاهدات
   - تابع معدل الاحتفاظ بالمشاهدين
   - حلل التعليقات

2. **GitHub Actions:**
   - راقب سجلات التنفيذ
   - تحقق من الأخطاء
   - حسّن الأداء

3. **لوحة التحكم:**
   - افتح `index.html` في المتصفح
   - راقب الإحصائيات
   - تتبع التقدم

### تحسين المحتوى

بناءً على الأداء:

- ✅ فيديوهات ناجحة: كرر النمط
- ❌ فيديوهات ضعيفة: غيّر الأسلوب
- 📈 جرب عناوين مختلفة
- 🎭 جرّب أنواع كوميديا مختلفة

---

## 🐛 حل المشاكل الشائعة

### ❌ فشل المصادقة مع يوتيوب

**الحل:**
```bash
1. تأكد من تفعيل YouTube Data API v3
2. تحقق من Client ID و Secret
3. جدد Refresh Token
4. تأكد من صلاحيات OAuth
```

### ❌ خطأ في جلب بيانات المباريات

**الحل:**
```bash
1. تحقق من API-Football Key
2. تأكد من عدم تجاوز الحد اليومي (100)
3. انتظر 24 ساعة للReset
```

### ❌ فشل توليد السيناريو

**الحل:**
```bash
1. تحقق من مفاتيح AI
2. تأكد من وجود رصيد
3. راجع سجلات GitHub Actions
```

### ❌ الفيديو لم يُرفع

**الحل:**
```bash
1. تحقق من حجم الفيديو (< 128MB للحسابات الجديدة)
2. تأكد من تنسيق MP4
3. راجع سجلات الرفع
```

---

## 📈 نصائح للنجاح

### 1️⃣ الاستمرارية
- انشر يومياً في نفس الوقت
- حافظ على جودة ثابتة
- استمر حتى مع قلة المشاهدات في البداية

### 2️⃣ الجودة
- راجع المحتوى قبل النشر
- تأكد من دقة المعلومات
- استخدم صور مصغرة جذابة

### 3️⃣ التفاعل
- رد على التعليقات
- اسأل المشاهدين عن آرائهم
- نفّذ اقتراحاتهم

### 4️⃣ التحسين
- جرّب أشكال مختلفة
- حلل البيانات بانتظام
- طوّر بناءً على الملاحظات

---

## 🎉 النتيجة المتوقعة

بعد 30 يوماً من التشغيل المستمر:

| المقياس | الهدف |
|---------|-------|
| فيديوهات منشورة | 30+ |
| إجمالي المشاهدات | 100K+ |
| المشتركين الجدد | 1K+ |
| معدل التفاعل | 8%+ |

بعد 90 يوماً:

| المقياس | الهدف |
|---------|-------|
| فيديوهات منشورة | 90+ |
| إجمالي المشاهدات | 1M+ |
| المشتركين الجدد | 10K+ |
| معدل التفاعل | 10%+ |

---

## 📞 الدعم

إذا واجهت مشكلة:

1. **راجع السجلات:** GitHub Actions → Workflow Run → Logs
2. **ابحث في Issues:** قد يكون الآخرون واجهوا نفس المشكلة
3. **اطرح سؤالاً:** أنشئ Issue جديد مع التفاصيل
4. **تواصل:** استخدم قنوات الدعم المتاحة

---

## ⚠️ تحذيرات مهمة

### 🔒 الأمان
- ❌ لا تشارك مفاتيح API أبداً
- ❌ لا ترفع ملفات credentials إلى GitHub
- ✅ استخدم GitHub Secrets دائماً
- ✅ فعّل 2FA على جميع الحسابات

### 📜 الامتثال
- التزم بشروط استخدام YouTube
- احترم حقوق النشر
- لا تستخدم محتوى غير مرخص
- اتبع إرشادات المجتمع

---

<div align="center">

**🚀 جاهز للبدء؟**

اتبع الخطوات above وابدأ رحلة إنشاء المحتوى الكوميدي الرياضي!

⚽ Football Comedy AI © 2026

</div>
