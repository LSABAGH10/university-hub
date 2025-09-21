# opportunities/models.py

from django.db import models
from django.utils import timezone

class Opportunity(models.Model):
    TYPE_CHOICES = (
        ('internship', 'تدريب صيفي'),
        ('full-time', 'وظيفة بدوام كامل'),
        ('workshop', 'ورشة عمل'),
        ('competition', 'مسابقة'),
    )

    title = models.CharField(max_length=200, verbose_name="عنوان الفرصة")
    company_name = models.CharField(max_length=100, verbose_name="اسم الشركة/الجهة")
    location = models.CharField(max_length=100, verbose_name="الموقع")
    description = models.TextField(verbose_name="الوصف والتفاصيل")
    opportunity_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="نوع الفرصة")
    post_date = models.DateTimeField(default=timezone.now, verbose_name="تاريخ النشر")
    end_date = models.DateField(null=True, blank=True, verbose_name="تاريخ انتهاء التقديم")
    link_to_apply = models.URLField(verbose_name="رابط التقديم")

    def __str__(self):
        return self.title