## **2. ملف alazab_refinement/__init__.py:**

```python
"""
Alazab Refinement - تحسينات العزب
نظام التحسينات والتطويرات المتقدمة لـ ERPNext

Author: Alazab Group
Version: 1.0.0
License: MIT
"""

__version__ = '1.0.0'
__title__ = 'Alazab Refinement'
__author__ = 'Alazab Group'
__email__ = 'admin@alazab.online'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025 Alazab Group'

# Application metadata
app_name = "alazab_refinement"
app_title = "Alazab Refinement"
app_publisher = "Alazab Group"
app_description = "تحسينات متقدمة لنظام ERPNext تشمل تحسين الأداء والأمان وتجربة المستخدم"
app_version = __version__
app_color = "#2c5aa0"
app_email = __email__
app_license = __license__

# Import main modules
try:
    import frappe
    from .hooks import *
    
    # تسجيل تحميل التطبيق
    if frappe.get_conf().get("developer_mode"):
        frappe.logger().info(f"✅ تم تحميل {app_title} بنجاح - الإصدار {app_version}")
        
except ImportError as e:
    # في حالة عدم توفر Frappe (أثناء التطوير مثلاً)
    print(f"تحذير: لم يتم العثور على Frappe - {e}")

# تصدير المتغيرات المهمة
__all__ = [
    '__version__',
    '__title__',
    '__author__',
    '__email__',
    '__license__',
    'app_name',
    'app_title',
    'app_publisher',
    'app_description',
    'app_version',
    'app_color',
    'app_email',
    'app_license'
]

def get_app_info():
    """
    إرجاع معلومات التطبيق
    """
    return {
        'name': app_name,
        'title': app_title,
        'version': app_version,
        'publisher': app_publisher,
        'description': app_description,
        'color': app_color,
        'email': app_email,
        'license': app_license,
        'copyright': __copyright__
    }

def check_dependencies():
    """
    فحص التبعيات المطلوبة
    """
    try:
        import frappe
        frappe_version = frappe.__version__
        
        # فحص إصدار Frappe
        if frappe_version < "15.0.0":
            return {
                'status': 'error',
                'message': f'تحسينات العزب تتطلب Frappe الإصدار 15.0.0 أو أحدث. الإصدار الحالي: {frappe_version}'
            }
        
        # فحص تطبيق ERPNext
        try:
            import erpnext
            erpnext_version = erpnext.__version__
            
            if erpnext_version < "15.0.0":
                return {
                    'status': 'warning',
                    'message': f'يُنصح باستخدام ERPNext الإصدار 15.0.0 أو أحدث. الإصدار الحالي: {erpnext_version}'
                }
                
        except ImportError:
            return {
                'status': 'warning',
                'message': 'لم يتم العثور على تطبيق ERPNext. بعض الميزات قد لا تعمل بشكل كامل.'
            }
        
        return {
            'status': 'success',
            'message': 'جميع التبعيات متوفرة ومتوافقة'
        }
        
    except ImportError:
        return {
            'status': 'error',
            'message': 'لم يتم العثور على Frappe. تأكد من تثبيت Frappe أولاً.'
        }

def initialize_app():
    """
    تهيئة التطبيق
    """
    try:
        import frappe
        
        # فحص التبعيات
        deps_check = check_dependencies()
        if deps_check['status'] == 'error':
            frappe.throw(deps_check['message'])
        elif deps_check['status'] == 'warning':
            frappe.msgprint(deps_check['message'], alert=True)
        
        # تسجيل تحميل التطبيق
        frappe.logger().info(f"🚀 تم تهيئة {app_title} بنجاح")
        
        return True
        
    except Exception as e:
        print(f"خطأ في تهيئة التطبيق: {e}")
        return False

# تشغيل التهيئة عند استيراد الموديول
if __name__ != "__main__":
    try:
        initialize_app()
    except:
        pass  # تجاهل الأخطاء أثناء الاستيراد
