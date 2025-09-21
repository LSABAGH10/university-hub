# qa/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

@login_required
def ask_question_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.course = course
            question.author = request.user
            question.save()
            # بعد طرح السؤال، أعد توجيهه إلى صفحة المقرر الرئيسية
            return redirect('course-detail', pk=course.pk)
    else:
        form = QuestionForm()
        
    return render(request, 'qa/ask_question.html', {'form': form, 'course': course})

@login_required
def question_detail_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all().order_by('created_at')
    answer_form = AnswerForm()

    if request.method == 'POST':
        # إذا كان الطلب لإضافة إجابة جديدة
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question-detail', pk=question.pk) # أعد تحميل نفس الصفحة

    context = {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
    }
    return render(request, 'qa/question_detail.html', context)