# qa/models.py

from django.db import models
from django.conf import settings
from courses.models import Course # سنستورد نموذج المقرر من تطبيق courses

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions', verbose_name="المقرر")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="السائل")
    title = models.CharField(max_length=255, verbose_name="عنوان السؤال")
    body = models.TextField(verbose_name="نص السؤال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name="السؤال التابع له")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="المجيب")
    body = models.TextField(verbose_name="نص الإجابة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return f"إجابة على: {self.question.title}"