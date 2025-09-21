# courses/admin.py

from django.contrib import admin
from .models import Course, Material

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1 # لعرض حقل إضافي واحد لإضافة مادة تعليمية جديدة مباشرة من صفحة المقرر

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_code', 'academic_year')
    search_fields = ('title', 'course_code')
    inlines = [MaterialInline]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'material_type', 'uploader', 'uploaded_at')
    list_filter = ('course', 'material_type', 'uploader')
    search_fields = ('title',)