# core/models.py

from django.db import models
from django.utils import timezone

class Advertisement(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="اسم الشركة")
    offer_title = models.CharField(max_length=200, verbose_name="عنوان العرض")
    offer_details = models.TextField(verbose_name="تفاصيل العرض")
    promo_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="البروموكود")
    logo = models.ImageField(upload_to='logos/', verbose_name="شعار الشركة")
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء")
    is_active = models.BooleanField(default=True, verbose_name="هل العرض فعال؟")

    def is_currently_active(self):
        today = timezone.now().date()
        return self.is_active and self.start_date <= today <= self.end_date

    def __str__(self):
        return self.offer_title

class Testimonial(models.Model):
    student_name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    student_details = models.CharField(max_length=100, verbose_name="تفاصيل الطالب (مثال: سنة 3)")
    quote = models.TextField(verbose_name="نص التقييم")
    is_featured = models.BooleanField(default=False, verbose_name="هل يظهر في الصفحة الرئيسية؟")

    def __str__(self):
        return self.student_name