# courses/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Course
from django.contrib.auth.decorators import login_required

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # إذا كان المستخدم ضيفاً، اعرض له المقررات التجريبية فقط
        if self.request.session.get('is_guest', False):
            return Course.objects.filter(is_demo=True)
        
        # إذا كان المستخدم مسجلاً دخوله، اعرض له كل المقررات
        # ملاحظة: إذا أردت عرض المقررات للمستخدمين المسجلين فقط، يمكنك إضافة تحقق هنا
        return Course.objects.all()

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        # هذه الدالة تضيف بيانات إضافية ليتم استخدامها في القالب
        context = super().get_context_data(**kwargs)
        # نضيف متغير is_guest ليتمكن القالب من التحقق منه
        context['is_guest'] = self.request.session.get('is_guest', False)
        return context

@login_required
def enroll_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    is_enrolled = course.enrolled_students.filter(pk=request.user.pk).exists()

    if is_enrolled:
        course.enrolled_students.remove(request.user)
    else:
        course.enrolled_students.add(request.user)
        
    return redirect('course-detail', pk=course.pk)