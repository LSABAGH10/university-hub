# courses/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Course
from django.contrib.auth.decorators import login_required

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses' # اسم المتغير الذي سنستخدمه في القالب

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
@login_required
def enroll_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)

    # التحقق إذا كان الطالب ملتحقاً بالفعل أم لا
    is_enrolled = course.enrolled_students.filter(pk=request.user.pk).exists()

    if is_enrolled:
        # إذا كان ملتحقاً، قم بإزالته (Unenroll)
        course.enrolled_students.remove(request.user)
    else:
        # إذا لم يكن ملتحقاً، قم بإضافته (Enroll)
        course.enrolled_students.add(request.user)

    # أعد توجيه المستخدم إلى نفس صفحة تفاصيل المقرر
    return redirect('course-detail', pk=course.pk)