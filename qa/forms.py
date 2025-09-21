# qa/forms.py

from django import forms
from .models import Question, Answer # قم بإضافة Answer هنا

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        labels = {
            'title': 'عنوان السؤال',
            'body': 'اشرح سؤالك بالتفصيل',
        }

# --- الاستمارة الجديدة ---
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
        labels = {
            'body': 'أضف إجابتك',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}), # لجعل حقل الإدخال أكبر
        }