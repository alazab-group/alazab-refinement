"""
Configuration for documentation
تكوين الوثائق والمساعدة
"""

source_link = "https://github.com/alazab-group/alazab-refinement"
docs_base_url = "https://docs.alazab.online"
headline = "تحسينات العزب - نظام التطوير والتحسين المتقدم"
sub_heading = "حلول متطورة لتحسين أداء وكفاءة نظام إدارة الموارد"

def get_context(context):
    """
    إضافة متغيرات إضافية لسياق الوثائق
    """
    context.brand_name = "Alazab Refinement"
    context.brand_html = '<img src="/assets/alazab_refinement/images/logo.png" alt="Alazab Logo" style="height: 30px;">'
    context.top_bar_items = [
        {
            "label": "الدعم الفني",
            "url": "https://support.alazab.online",
            "right": 1
        },
        {
            "label": "الوثائق",
            "url": "https://docs.alazab.online",
            "right": 1
        },
        {
            "label": "المجتمع",
            "url": "https://community.alazab.online",
            "right": 1
        }
    ]
    
    return context

# Documentation categories
doc_categories = {
    "user_manual": {
        "title": "دليل المستخدم",
        "description": "شرح مفصل لاستخدام تحسينات العزب",
        "icon": "fa-user",
        "color": "#2c5aa0"
    },
    "developer_guide": {
        "title": "دليل المطور",
        "description": "وثائق تقنية للمطورين والمبرمجين",
        "icon": "fa-code",
        "color": "#28a745"
    },
    "api_reference": {
        "title": "مرجع واجهة برمجة التطبيقات",
        "description": "توثيق شامل لجميع واجهات برمجة التطبيقات",
        "icon": "fa-cogs",
        "color": "#ffc107"
    },
    "tutorials": {
        "title": "الدروس التطبيقية",
        "description": "دروس خطوة بخطوة للبدء السريع",
        "icon": "fa-graduation-cap",
        "color": "#dc3545"
    },
    "troubleshooting": {
        "title": "حل المشاكل",
        "description": "حلول للمشاكل الشائعة وطرق استكشاف الأخطاء",
        "icon": "fa-wrench",
        "color": "#6f42c1"
    }
}

# Help documentation structure
help_sections = [
    {
        "title": "البدء السريع",
        "description": "تعلم أساسيات استخدام تحسينات العزب",
        "topics": [
            "تثبيت النظام",
            "الإعداد الأولي",
            "أول استخدام",
            "الواجهة الرئيسية"
        ]
    },
    {
        "title": "الميزات المتقدمة",
        "description": "استكشف الإمكانيات المتطورة للنظام",
        "topics": [
            "تحسين الأداء",
            "إدارة الأمان",
            "التخصيص والإعدادات",
            "التكامل مع الأنظمة الأخرى"
        ]
    },
    {
        "title": "الإدارة والصيانة",
        "description": "كيفية إدارة وصيانة النظام",
        "topics": [
            "النسخ الاحتياطي",
            "مراقبة الأداء",
            "إدارة المستخدمين",
            "التحديثات والترقيات"
        ]
    }
]

# FAQ - الأسئلة الشائعة
faq = [
    {
        "question": "كيف يمكنني تثبيت تحسينات العزب؟",
        "answer": "يمكن تثبيت تحسينات العزب من خلال مدير التطبيقات في نظام Frappe. انتقل إلى قائمة التطبيقات واختر 'تثبيت تطبيق جديد' ثم ابحث عن 'Alazab Refinement'."
    },
    {
        "question": "هل تحسينات العزب متوافقة مع جميع إصدارات ERPNext؟",
        "answer": "تحسينات العزب متوافقة مع ERPNext الإصدار 15 وما بعده. للإصدارات الأقدم، يرجى الاتصال بفريق الدعم للحصول على إصدار متوافق."
    },
    {
        "question": "كم من الوقت يستغرق تطبيق التحسينات؟",
        "answer": "عادة ما تظهر التحسينات فوراً بعد التثبيت. بعض التحسينات قد تحتاج إعادة تشغيل النظام لتكون فعالة بالكامل."
    },
    {
        "question": "هل يمكنني تخصيص التحسينات حسب احتياجاتي؟",
        "answer": "نعم، يمكن تخصيص معظم التحسينات من خلال لوحة الإعدادات. كما يمكن للمطورين إضافة تحسينات مخصصة باستخدام واجهات برمجة التطبيقات المتاحة."
    },
    {
        "question": "ماذا لو واجهت مشكلة بعد تطبيق التحسينات؟",
        "answer": "يمكنك الرجوع إلى الإعدادات الافتراضية في أي وقت من خلال لوحة التحكم. كما يتوفر فريق دعم فني متخصص للمساعدة في حل أي مشاكل."
    }
]

# Release notes template
release_notes_template = """
# تحسينات العزب - ملاحظات الإصدار

## الإصدار {version} - {date}

### ✨ الميزات الجديدة
{new_features}

### 🚀 التحسينات
{improvements}

### 🐛 إصلاح الأخطاء
{bug_fixes}

### ⚠️ التغييرات المهمة
{breaking_changes}

### 📚 تحديثات الوثائق
{documentation_updates}

---
للمزيد من المعلومات، راجع [الوثائق الكاملة]({docs_url})
"""

# API documentation template
api_doc_template = """
# API Reference - مرجع واجهات برمجة التطبيقات

## {endpoint_name}

**URL:** `{method} {endpoint}`

### الوصف
{description}

### المعاملات
{parameters}

### مثال على الطلب
```{request_language}
{request_example}
