# courses/urls.py

from django.urls import path
from .views import CourseListView, CourseDetailView, enroll_course_view
from qa.views import ask_question_view # <-- استيراد الـ view من تطبيق qa

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('<int:pk>/enroll/', enroll_course_view, name='enroll-course'),
    path('<int:pk>/ask/', ask_question_view, name='ask-question'), # <-- الرابط الجديد
]