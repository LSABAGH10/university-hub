# courses/models.py

from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقرر")
    course_code = models.CharField(max_length=20, verbose_name="كود المقرر", unique=True)
    academic_year = models.IntegerField(verbose_name="الفرقة الدراسية")
    description = models.TextField(blank=True, verbose_name="وصف المقرر")
    # --- السطر الجديد ---
    # هذا الحقل سيربط المقرر بقائمة من المستخدمين (الطلاب الملتحقين)
    enrolled_students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='enrolled_courses', blank=True)

    def __str__(self):
        return self.title

class Material(models.Model):
    MATERIAL_TYPE_CHOICES = (
        ('pdf', 'ملف PDF'),
        ('video', 'فيديو'),
        ('summary', 'ملخص'),
        ('exam', 'امتحان سابق'),
    )

    title = models.CharField(max_length=200, verbose_name="عنوان المادة")
    # ربط كل مادة تعليمية بمقرر دراسي معين
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials', verbose_name="المقرر التابع له")
    # ربط كل مادة بالمستخدم الذي قام برفعها
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="رافع المادة")

    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE_CHOICES, verbose_name="نوع المادة")
    file = models.FileField(upload_to='course_materials/', verbose_name="الملف")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الرفع")

    def __str__(self):
        return self.title