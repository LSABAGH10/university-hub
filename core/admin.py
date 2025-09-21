# core/admin.py

from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('offer_title', 'company_name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'company_name')
    search_fields = ('offer_title', 'company_name')