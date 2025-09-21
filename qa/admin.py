# qa/admin.py

from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1 # لعرض حقل إضافي لإضافة إجابة

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'author', 'created_at')
    list_filter = ('course', 'author')
    search_fields = ('title', 'body')
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'created_at')
    list_filter = ('author',)
    search_fields = ('body',)