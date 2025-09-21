# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'ولد'),
        ('female', 'بنت'),
    )
    VERIFICATION_STATUS_CHOICES = (
        ('pending', 'قيد المراجعة'),
        ('verified', 'موثق'),
        ('rejected', 'مرفوض'),
    )

    email = models.EmailField(unique=True)

    # --- بداية التعديل ---
    # جعلنا هذه الحقول اختيارية للسماح بإنشاء حساب المدير
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='الجنس', null=True, blank=True)
    college = models.CharField(max_length=100, verbose_name='الكلية', null=True, blank=True)
    academic_year = models.IntegerField(verbose_name='الفرقة الدراسية', null=True, blank=True)
    
    verification_status = models.CharField(
        max_length=10, 
        choices=VERIFICATION_STATUS_CHOICES, 
        default='pending', 
        verbose_name='حالة التحقق'
    )
    
    id_photo = models.FileField(upload_to='id_photos/', verbose_name='صورة إثبات الهوية', null=True, blank=True)
    # --- نهاية التعديل ---

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email