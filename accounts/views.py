# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# --- دالة تسجيل حساب جديد ---
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# --- دالة تسجيل الدخول ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# --- دالة تسجيل الخروج ---
def logout_view(request):
    logout(request)
    return redirect('login')

# --- دالة لوحة التحكم (تم تعديلها) ---
@login_required
def dashboard_view(request):
    # جلب المقررات التي التحق بها المستخدم الحالي فقط
    enrolled_courses = request.user.enrolled_courses.all()
    context = {
        'courses': enrolled_courses
    }
    return render(request, 'accounts/dashboard.html', context)