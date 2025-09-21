# qa/urls.py

from django.urls import path
from .views import ask_question_view, question_detail_view # <-- أضف الدالة الجديدة

urlpatterns = [
    path('question/<int:pk>/', question_detail_view, name='question-detail'), # <-- الرابط الجديد
]