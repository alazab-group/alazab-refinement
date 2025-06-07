/**
 * Alazab Refinement - JavaScript Functions
 * تحسينات العزب - الدوال الرئيسية
 */

// تهيئة التطبيق عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', function() {
    initializeAlazabRefinement();
});

/**
 * تهيئة تحسينات العزب
 */
function initializeAlazabRefinement() {
    console.log('🚀 تم تحميل تحسينات العزب بنجاح');
    
    // إضافة تأثيرات التحميل
    addLoadingAnimations();
    
    // تهيئة الإحصائيات المتحركة
    initializeCounters();
    
    // تهيئة معالجات الأحداث
    initializeEventHandlers();
    
    // تهيئة التحديث التلقائي
    initializeAutoRefresh();
}

/**
 * إضافة تأثيرات التحميل
 */
function addLoadingAnimations() {
    const cards = document.querySelectorAll('.alazab-card');
    const statBoxes = document.querySelectorAll('.stat-box');
    
    // إضافة تأثير التلاشي للكروت
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 200);
    });
    
    // إضافة تأثير الانزلاق لصناديق الإحصائيات
    statBoxes.forEach((box, index) => {
        setTimeout(() => {
            box.classList.add('slide-in-right');
        }, index * 150 + 500);
    });
}

/**
 * تهيئة العدادات المتحركة
 */
function initializeCounters() {
    const counters = [
        { element: '.stat-box h4', targets: [300, 50, 99.9, 95] }
    ];
    
    const statBoxes = document.querySelectorAll('.stat-box h4');
    const targets = [300, 50, 99.9, 95];
    
    statBoxes.forEach((counter, index) => {
        animateCounter(counter, targets[index], 2000);
    });
}

/**
 * تحريك العداد من 0 إلى القيمة المستهدفة
 */
function animateCounter(element, target, duration) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        
        // تنسيق الرقم حسب النوع
        if (target === 99.9) {
            element.textContent = current.toFixed(1) + '%';
        } else if (target === 300) {
            element.textContent = Math.floor(current) + '%';
        } else {
            element.textContent = Math.floor(current) + '%';
        }
    }, 16);
}

/**
 * تهيئة معالجات الأحداث
 */
function initializeEventHandlers() {
    // إضافة تأثيرات التفاعل للكروت
    const cards = document.querySelectorAll('.alazab-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', handleCardHover);
        card.addEventListener('mouseleave', handleCardLeave);
        card.addEventListener('click', handleCardClick);
    });
    
    // إضافة معالج للنقر على صناديق الإحصائيات
    const statBoxes = document.querySelectorAll('.stat-box');
    statBoxes.forEach(box => {
        box.addEventListener('click', handleStatBoxClick);
    });
    
    // إضافة معالج لتغيير حجم النافذة
    window.addEventListener('resize', handleWindowResize);
}

/**
 * معالج تحويم الفأرة على الكارت
 */
function handleCardHover(event) {
    const card = event.currentTarget;
    card.style.transform = 'translateY(-10px) scale(1.02)';
    card.style.transition = 'all 0.3s ease';
}

/**
 * معالج مغادرة الفأرة للكارت
 */
function handleCardLeave(event) {
    const card = event.currentTarget;
    card.style.transform = 'translateY(0) scale(1)';
}

/**
 * معالج النقر على الكارت
 */
function handleCardClick(event) {
    const card = event.currentTarget;
    const cardTitle = card.querySelector('.card-header').textContent.trim();
    
    showNotification(`تم النقر على: ${cardTitle}`, 'info');
    
    // إضافة تأثير النبضة
    card.style.animation = 'pulse 0.5s ease-in-out';
    setTimeout(() => {
        card.style.animation = '';
    }, 500);
}

/**
 * معالج النقر على صندوق الإحصائيات
 */
function handleStatBoxClick(event) {
    const statBox = event.currentTarget;
    const statValue = statBox.querySelector('h4').textContent;
    const statLabel = statBox.querySelector('p').textContent;
    
    showDetailedStats(statLabel, statValue);
}

/**
 * معالج تغيير حجم النافذة
 */
function handleWindowResize() {
    // إعادة حساب تخطيط العناصر عند تغيير حجم النافذة
    const isMobile = window.innerWidth < 768;
    const cards = document.querySelectorAll('.alazab-card');
    
    cards.forEach(card => {
        if (isMobile) {
            card.style.marginBottom = '20px';
        } else {
            card.style.marginBottom = '30px';
        }
    });
}

/**
 * عرض إشعار
 */
function showNotification(message, type = 'info') {
    // إنشاء عنصر الإشعار
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        min-width: 300px;
        text-align: center;
    `;
    
    notification.innerHTML = `
        <strong>${message}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // إزالة الإشعار تلقائياً بعد 3 ثواني
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 3000);
}

/**
 * عرض تفاصيل الإحصائيات
 */
function showDetailedStats(label, value) {
    const details = {
        'تحسن في السرعة': 'تم تحقيق تحسن 300% في سرعة معالجة البيانات من خلال تحسين الخوارزميات وضغط البيانات.',
        'توفير في التخزين': 'تم توفير 50% من مساحة التخزين باستخدام تقنيات الضغط المتقدمة وتحسين هيكل قاعدة البيانات.',
        'مستوى الأمان': 'تم الوصول لمستوى أمان 99.9% من خلال تطبيق أحدث معايير التشفير والحماية.',
        'رضا المستخدمين': '95% من المستخدمين أعربوا عن رضاهم الكامل عن التحسينات الجديدة.'
    };
    
    const detail = details[label] || 'تفاصيل إضافية غير متوفرة حالياً.';
    
    // إنشاء نافذة منبثقة مخصصة
    showCustomModal(label, value, detail);
}

/**
 * عرض نافذة منبثقة مخصصة
 */
function showCustomModal(title, value, description) {
    // إنشاء الخلفية المعتمة
    const backdrop = document.createElement('div');
    backdrop.className = 'modal-backdrop fade show';
    backdrop.style.zIndex = '9998';
    
    // إنشاء النافذة المنبثقة
    const modal = document.createElement('div');
    modal.className = 'modal fade show';
    modal.style.cssText = `
        display: block;
        z-index: 9999;
    `;
    
    modal.innerHTML = `
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="border-radius: 15px; overflow: hidden;">
                <div class="modal-header" style="background: linear-gradient(45deg, var(--alazab-primary), #4a90e2); color: white;">
                    <h5 class="modal-title">
                        <i class="fas fa-chart-bar ms-2"></i>
                        ${title}
                    </h5>
                    <button type="button" class="btn-close btn-close-white" onclick="closeCustomModal()"></button>
                </div>
                <div class="modal-body text-center">
                    <div class="mb-4">
                        <h2 style="color: var(--alazab-primary); font-size: 3rem; font-weight: bold;">${value}</h2>
                    </div>
                    <p style="font-size: 1.1rem; line-height: 1.6;">${description}</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" onclick="closeCustomModal()">
                        <i class="fas fa-check ms-1"></i>
                        فهمت
                    </button>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(backdrop);
    document.body.appendChild(modal);
    
    // حفظ مراجع للإزالة لاحقاً
    window.currentModalBackdrop = backdrop;
    window.currentModal = modal;
}

/**
 * إغلاق النافذة المنبثقة المخصصة
 */
function closeCustomModal() {
    if (window.currentModalBackdrop) {
        window.currentModalBackdrop.remove();
    }
    if (window.currentModal) {
        window.currentModal.remove();
    }
}

/**
 * تهيئة التحديث التلقائي
 */
function initializeAutoRefresh() {
    // تحديث الإحصائيات كل 30 ثانية
    setInterval(() => {
        updateStatistics();
    }, 30000);
    
    // تحديث حالة النظام كل دقيقة
    setInterval(() => {
        updateSystemStatus();
    }, 60000);
}

/**
 * تحديث الإحصائيات
 */
function updateStatistics() {
    // محاكاة تحديث الإحصائيات
    const statBoxes = document.querySelectorAll('.stat-box h4');
    
    statBoxes.forEach(statBox => {
        // إضافة تأثير وميض للإشارة للتحديث
        statBox.style.animation = 'pulse 0.5s ease-in-out';
        setTimeout(() => {
            statBox.style.animation = '';
        }, 500);
    });
    
    console.log('تم تحديث الإحصائيات:', new Date().toLocaleString('ar-EG'));
}

/**
 * تحديث حالة النظام
 */
function updateSystemStatus() {
    // فحص حالة اتصال النظام
    fetch('/api/system/status')
        .then(response => response.json())
        .then(data => {
            console.log('حالة النظام:', data);
            // يمكن إضافة مؤشر حالة النظام هنا
        })
        .catch(error => {
            console.log('تعذر الحصول على حالة النظام:', error);
        });
}

/**
 * دوال مساعدة إضافية
 */

// تصدير الإحصائيات
function exportStatistics() {
    const stats = {
        speed_improvement: '300%',
        storage_saving: '50%',
        security_level: '99.9%',
        user_satisfaction: '95%',
        export_date: new Date().toISOString()
    };
    
    const dataStr = JSON.stringify(stats, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    
    const exportFileDefaultName = `alazab-stats-${new Date().toISOString().split('T')[0]}.json`;
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
}

// طباعة التقرير
function printReport() {
    window.print();
}

// مشاركة الإحصائيات
function shareStats() {
    if (navigator.share) {
        navigator.share({
            title: 'تحسينات العزب - الإحصائيات',
            text: 'شاهد إحصائيات تحسينات العزب المذهلة!',
            url: window.location.href
        });
    } else {
        // نسخ الرابط للحافظة
        navigator.clipboard.writeText(window.location.href)
            .then(() => showNotification('تم نسخ الرابط للحافظة', 'success'))
            .catch(() => showNotification('تعذر نسخ الرابط', 'error'));
    }
}

// تفعيل الوضع المظلم
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark);
    showNotification(isDark ? 'تم تفعيل الوضع المظلم' : 'تم تفعيل الوضع العادي', 'info');
}

// تحميل إعدادات الوضع المظلم
document.addEventListener('DOMContentLoaded', function() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
    }
});

/**
 * تصدير الدوال العامة للنافذة العالمية
 */
window.AlazabRefinement = {
    exportStatistics,
    printReport,
    shareStats,
    toggleDarkMode,
    closeCustomModal,
    showNotification
};

console.log('✅ تم تحميل جميع دوال تحسينات العزب بنجاح');
