# core/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from .forms import AdvertiseForm
from .models import Advertisement
from django.utils import timezone

def advertise_view(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            contact_email = form.cleaned_data['contact_email']
            offer_details = form.cleaned_data['offer_details']
            
            # تجهيز وإرسال البريد الإلكتروني
            subject = f"طلب إعلان جديد من: {company_name}"
            message = f"من: {contact_email}\n\nتفاصيل العرض:\n{offer_details}"
            
            # استبدل هذا الإيميل بإيميلك الحقيقي الذي ستستقبل عليه الطلبات
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
        # جلب الإعلانات الفعالة والتي لم تنتهِ مدتها فقط
        today = timezone.now().date()
        return Advertisement.objects.filter(is_active=True, start_date__lte=today, end_date__gte=today)

def home_view(request):
    return render(request, 'core/home.html')