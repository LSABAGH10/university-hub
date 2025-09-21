# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # هنا نحدد الحقول التي ستظهر في لوحة التحكم
    # يمكنك تعديلها لاحقاً كما تشاء
    model = CustomUser
    list_display = ['email', 'username', 'verification_status', 'is_staff']
    
    # هذه لتخصيص صفحة التعديل داخل لوحة التحكم
    fieldsets = UserAdmin.fieldsets + (
            ('الحقول الإضافية', {'fields': ('gender', 'college', 'academic_year', 'id_photo', 'verification_status')}),
    )

# الآن نقوم بتسجيل النموذج الخاص بنا مع الفئة المخصصة له
admin.site.register(CustomUser, CustomUserAdmin)