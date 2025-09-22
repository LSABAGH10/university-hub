# news/models.py
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    content = models.TextField(verbose_name="محتوى الخبر")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="تاريخ النشر")
    is_published = models.BooleanField(default=True, verbose_name="هل الخبر منشور؟")

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title