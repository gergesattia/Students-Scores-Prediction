# 📚 Exam Score Predictor - README

## 🎯 نظرة عامة

تطبيق تنبؤ ذكي لدرجات امتحانات الطلاب باستخدام تعلم الآلة (XGBoost)

---

## 🚀 البدء السريع

### خيار 1: Flask (الأفضل)
```bash
python app_flask.py
```
ثم انتقل إلى: **http://localhost:5000**

### خيار 2: Streamlit
```bash
streamlit run app_streamlit_fixed.py
```
ثم انتقل إلى: **http://localhost:8501**

---

## 📊 المميزات

✅ **Single Prediction** - التنبؤ بدرجة طالب واحد
✅ **Batch Prediction** - التنبؤ لعدة طلاب من ملف CSV
✅ **Dark Theme** - واجهة حديثة وسهلة الاستخدام
✅ **Real-time Results** - النتائج فوراً

---

## 📁 الملفات المهمة

### تطبيقات الويب:
- `app_flask.py` - Flask (تطبيق الويب الرئيسي)
- `app_streamlit_fixed.py` - Streamlit (نسخة محسّنة)
- `app_web.py` - Streamlit (تصميم جميل)

### Static Files (Flask):
- `templates/index.html` - صفحة HTML
- `static/styles.css` - الأنماط
- `static/script.js` - المنطق

### نماذج معدة مسبقاً:
- `xgboost_model.pkl` - نموذج XGBoost المدرب
- `preprocessor.pkl` - معالج البيانات

---

## 🔧 المتطلبات (Requirements)

```
flask
streamlit
pandas
numpy
scikit-learn
xgboost
```

### التثبيت:
```bash
pip install flask streamlit pandas numpy scikit-learn xgboost
```

---

## 📊 المدخلات (Features)

يتقبل التطبيق 11 feature:

| Feature | الوصف | نوع البيانات |
|---------|--------|------------|
| Age | عمر الطالب | رقم (15-65) |
| Gender | النوع | male/female/other |
| Course Type | نوع الدورة | ba/diploma/b.tech |
| Study Hours | ساعات الدراسة أسبوعياً | رقم (0-24) |
| Class Attendance | نسبة الحضور | نسبة (0-100%) |
| Internet Access | توفر الإنترنت | yes/no |
| Sleep Hours | ساعات النوم يومياً | رقم (0-12) |
| Sleep Quality | جودة النوم | poor/average/good |
| Study Method | طريقة الدراسة | group study/coaching/mixed/self study |
| Facility Rating | تقييم المرافق | low/medium/high |
| Exam Difficulty | صعوبة الامتحان | easy/moderate/hard |

---

## 📤 صيغة CSV (للتنبوء الجماعي)

```csv
age,gender,course,study_hours,class_attendance,internet_access,sleep_hours,sleep_quality,study_method,facility_rating,exam_difficulty
20,male,ba,6.0,75.0,yes,7.0,good,group study,medium,moderate
22,female,b.tech,7.5,85.0,yes,6.5,average,self study,high,easy
19,male,diploma,5.0,65.0,no,8.0,good,coaching,low,hard
```

---

## 🎯 النتائج

### المخرجات:
- **Predicted Score** - الدرجة المتنبأ بها (0-100)
- **Grade** - التقدير (A/B/C/D)
- **Status** - الحالة (Excellent/Good/Average/Poor)

### إحصائيات (للتنبؤ الجماعي):
- Average Score
- Max Score
- Min Score
- Standard Deviation

---

## 💡 نصائح للحصول على تنبؤات أفضل

✓ زيادة ساعات الدراسة (6+ ساعات)
✓ المحافظة على حضور عالي (80%+)
✓ الحصول على 7-8 ساعات نوم جيد
✓ استخدام طرق دراسة فعالة (group study)
✓ التأكد من توفر المرافق الجيدة

---

## 🔍 فهم النموذج

### معمارية النموذج:
```
Raw Data
    ↓
Preprocessing (Category Encoding + Standard Scaling)
    ↓
XGBoost Regressor (trained on 12 features)
    ↓
Predicted Score (0-100)
```

### الدقة:
- الدقة تعتمد على جودة بيانات التدريب
- النموذج متدرب على بيانات طلاب حقيقية

---


## 📈 تحسين النموذج (المستقبل)

لتحسين النموذج، يمكنك:
1. إضافة بيانات تدريب أكثر
2. تعديل معاملات XGBoost
3. إضافة features جديدة
4. استخدام cross-validation

--

