"""
Alazab Refinement Hooks
تحسينات العزب - ملف الخطافات والتكامل مع Frappe
"""

import frappe
from frappe import _

# معلومات التطبيق الأساسية
app_name = "alazab_refinement"
app_title = "Alazab Refinement"
app_publisher = "Alazab Group"
app_description = "تحسينات متقدمة لنظام ERPNext تشمل الأداء والأمان وتجربة المستخدم"
app_version = "1.0.0"
app_color = "#2c5aa0"
app_email = "admin@alazab.online"
app_license = "MIT"

# التطبيقات المطلوبة
required_apps = ["frappe", "erpnext"]

# إعدادات الموقع
# =================

# إدخال Bootstrap و CSS مخصص
app_include_css = [
    "/assets/alazab_refinement/css/alazab-refinement.css"
]

# إدخال JavaScript مخصص
app_include_js = [
    "/assets/alazab_refinement/js/alazab-refinement.js"
]

# إدخال ملفات للصفحات الخاصة بالتطبيق
web_include_css = [
    "/assets/alazab_refinement/css/alazab-refinement.css"
]

web_include_js = [
    "/assets/alazab_refinement/js/alazab-refinement.js"
]

# الصفحات الرئيسية
website_route_rules = [
    {"from_route": "/alazab-refinement", "to_route": "alazab_refinement"},
    {"from_route": "/refinements", "to_route": "alazab_refinement"},
]

# إعدادات التطبيق
# ================

# Generator فئات المستندات
# doc_events = {}

# خطافات الجلسة
# ===============

# on_login
on_login = [
    "alazab_refinement.utils.session.on_user_login"
]

# on_logout  
on_logout = [
    "alazab_refinement.utils.session.on_user_logout"
]

# خطافات المستندات
# ==================

# خطافات عامة لجميع المستندات
doc_events = {
    "*": {
        "before_save": "alazab_refinement.utils.performance.optimize_before_save",
        "after_save": "alazab_refinement.utils.performance.optimize_after_save",
        "before_delete": "alazab_refinement.utils.security.log_deletion",
        "after_delete": "alazab_refinement.utils.security.cleanup_after_deletion"
    },
    "User": {
        "after_insert": "alazab_refinement.utils.user.setup_user_preferences",
        "on_update": "alazab_refinement.utils.user.update_user_cache"
    },
    "Sales Invoice": {
        "on_submit": "alazab_refinement.utils.sales.optimize_sales_invoice",
        "before_print": "alazab_refinement.utils.print.enhance_invoice_print"
    },
    "Purchase Invoice": {
        "on_submit": "alazab_refinement.utils.purchase.optimize_purchase_invoice"
    },
    "Item": {
        "after_save": "alazab_refinement.utils.inventory.update_item_cache"
    },
    "Customer": {
        "after_save": "alazab_refinement.utils.crm.update_customer_insights"
    }
}

# خطافات مجدولة
# ===============

scheduler_events = {
    # يومياً في منتصف الليل
    "daily": [
        "alazab_refinement.tasks.daily.cleanup_temp_files",
        "alazab_refinement.tasks.daily.update_performance_metrics",
        "alazab_refinement.tasks.daily.backup_critical_data"
    ],
    
    # أسبوعياً يوم الأحد
    "weekly": [
        "alazab_refinement.tasks.weekly.generate_performance_report",
        "alazab_refinement.tasks.weekly.optimize_database_indexes"
    ],
    
    # شهرياً في اليوم الأول
    "monthly": [
        "alazab_refinement.tasks.monthly.archive_old_logs",
        "alazab_refinement.tasks.monthly.update_security_audit"
    ],
    
    # كل 10 دقائق
    "cron": {
        "*/10 * * * *": [
            "alazab_refinement.tasks.monitoring.check_system_health"
        ],
        "0 */6 * * *": [
            "alazab_refinement.tasks.maintenance.optimize_cache"
        ]
    }
}

# خطافات البريد الإلكتروني
# =========================

# تخصيص قوالب البريد الإلكتروني
email_brand_image = "/assets/alazab_refinement/images/email-header.png"
default_mail_footer = """
<div style="text-align: center; margin-top: 30px; padding: 20px; background-color: #f8f9fa;">
    <p style="color: #6c757d; font-size: 12px;">
        تم إرسال هذا البريد بواسطة تحسينات العزب<br>
        © 2025 مجموعة العزب - جميع الحقوق محفوظة
    </p>
</div>
"""

# خطافات التثبيت
# ================

after_install = "alazab_refinement.setup.install.after_install"
after_uninstall = "alazab_refinement.setup.install.after_uninstall"

# خطافات البيانات
# ================

# إنشاء مستندات افتراضية بعد التثبيت
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["name", "in", [
                "User-alazab_refinement_preferences",
                "Company-alazab_performance_settings"
            ]]
        ]
    },
    {
        "doctype": "Property Setter",
        "filters": [
            ["name", "like", "alazab_refinement%"]
        ]
    }
]

# خطافات الإعدادات
# ===================

# إعدادات النظام الافتراضية
default_app_config = {
    "enable_performance_monitoring": 1,
    "enable_security_enhancements": 1,
    "enable_ui_improvements": 1,
    "cache_optimization_level": "medium",
    "security_audit_frequency": "weekly"
}

# خطافات واجهة برمجة التطبيقات
# ===============================

# نقاط نهاية API مخصصة
website_generators = [
    "Alazab Refinement Dashboard"
]

# خطافات التقارير
# =================

# تحسين أداء التقارير
override_whitelisted_methods = {
    "frappe.desk.query_report.run": "alazab_refinement.utils.reports.optimized_run_report"
}

# خطافات البحث
# ==============

# تحسين البحث العام
global_search_doctypes = {
    "Alazab Performance Metric": 1,
    "Alazab Security Log": 1
}

# خطافات الترجمة
# ===============

# ملفات الترجمة
boot_session = "alazab_refinement.utils.boot.boot_session"

# خطافات التخزين المؤقت
# ========================

# إعدادات التخزين المؤقت المحسنة
redis_cache_config = {
    "alazab_refinement_cache": {
        "ttl": 3600,  # ساعة واحدة
        "max_size": 1000
    }
}

# خطافات الأمان
# ==============

# قواعد الصلاحيات المحسنة
permission_query_conditions = {
    "Alazab Performance Metric": "alazab_refinement.utils.permissions.get_performance_metric_permissions",
    "Alazab Security Log": "alazab_refinement.utils.permissions.get_security_log_permissions"
}

# خطافات التصدير
# ===============

# تنسيقات تصدير إضافية
export_formats = ["alazab_enhanced_pdf", "alazab_excel_template"]

# خطافات الطباعة
# ===============

# تحسينات الطباعة
standard_format_template = "alazab_refinement/templates/print_formats/enhanced_standard.html"

# خطافات مخصصة
# ==============

def validate_alazab_settings(doc, method):
    """
    التحقق من صحة إعدادات تحسينات العزب
    """
    pass

def update_alazab_cache(doc, method):
    """
    تحديث التخزين المؤقت لتحسينات العزب
    """
    pass

# دوال مساعدة
# ============

def get_app_version():
    """إرجاع إصدار التطبيق"""
    return app_version

def is_alazab_refinement_enabled():
    """فحص ما إذا كانت تحسينات العزب مفعلة"""
    return frappe.db.get_single_value("System Settings", "enable_alazab_refinement") or False

def get_alazab_config(key, default=None):
    """الحصول على إعداد محدد من تحسينات العزب"""
    try:
        return frappe.db.get_single_value("Alazab Refinement Settings", key) or default
    except:
        return default

# جدولة المهام الديناميكية
def get_dynamic_scheduler_events():
    """
    إرجاع مهام مجدولة ديناميكية حسب الإعدادات
    """
    events = {}
    
    if get_alazab_config("enable_auto_backup"):
        events["daily"] = events.get("daily", []) + [
            "alazab_refinement.tasks.backup.automated_backup"
        ]
    
    if get_alazab_config("enable_performance_monitoring"):
        events["hourly"] = events.get("hourly", []) + [
            "alazab_refinement.tasks.monitoring.performance_check"
        ]
    
    return events

# إضافة المهام الديناميكية للجدولة
try:
    dynamic_events = get_dynamic_scheduler_events()
    for frequency, tasks in dynamic_events.items():
        if frequency in scheduler_events:
            scheduler_events[frequency].extend(tasks)
        else:
            scheduler_events[frequency] = tasks
except:
    pass  # تجاهل الأخطاء أثناء التحميل

# تسجيل تحميل الخطافات
if frappe.get_conf().get("developer_mode", False):
    frappe.logger().info("✅ تم تحميل خطافات تحسينات العزب بنجاح")
