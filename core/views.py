# core/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from .forms import AdvertiseForm
from .models import Advertisement, Testimonial
from django.utils import timezone
from news.models import Article # <-- استيراد نموذج الأخبار
from courses.models import Material

def home_view(request):
    # استخدام أرقام ثابتة للإحصائيات
    student_count = 457
    course_count = 38
    material_count = 280
    
    # جلب التقييمات المميزة
    manual_testimonials = [
        {
            'quote': 'وفّر عليا وقت كبير بدل ما أدور في جروبات الواتساب.',
            'student_name': 'أحمد علي',
            'student_details': 'الفرقة الثالثة، هندسة'
        },
        {
            'quote': 'أفضل مكان ألاقي فيه ملخصات منظمة ومحدثة باستمرار.',
            'student_name': 'سارة محمود',
            'student_details': 'الفرقة الثانية، طب'
        }
    ]
    
    # جلب آخر 3 أخبار منشورة
    latest_articles = Article.objects.filter(is_published=True)[:3]
    
    context = {
        'student_count': student_count,
        'course_count': course_count,
        'material_count': material_count,
        'testimonials': manual_testimonials,
        'articles': latest_articles, # <-- إضافة الأخبار للسياق
    }
    return render(request, 'core/home.html', context)

def advertise_view(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            contact_email = form.cleaned_data['contact_email']
            offer_details = form.cleaned_data['offer_details']
            
            subject = f"طلب إعلان جديد من: {company_name}"
            message = f"من: {contact_email}\n\nتفاصيل العرض:\n{offer_details}"
            
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['your_admin_email@example.com'])
            
            return redirect('advertise-success')
    else:
        form = AdvertiseForm()
        
    return render(request, 'core/advertise.html', {'form': form})

def advertise_success_view(request):
    return render(request, 'core/advertise_success.html')

class OfferListView(ListView):
    model = Advertisement
    template_name = 'core/offer_list.html'
    context_object_name = 'offers'

    def get_queryset(self):
        today = timezone.now().date()
        return Advertisement.objects.filter(is_active=True, start_date__lte=today, end_date__gte=today)

def guest_login_view(request):
    request.session['is_guest'] = True
    return redirect('course-list')