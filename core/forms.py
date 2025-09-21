# core/forms.py

from django import forms

class AdvertiseForm(forms.Form):
    company_name = forms.CharField(label="اسم الشركة/المعلن", max_length=100)
    contact_email = forms.EmailField(label="البريد الإلكتروني للتواصل")
    offer_details = forms.CharField(label="تفاصيل العرض المقترح", widget=forms.Textarea)