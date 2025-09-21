# opportunities/admin.py

from django.contrib import admin
from .models import Opportunity

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'opportunity_type', 'post_date', 'end_date')
    list_filter = ('opportunity_type', 'company_name')
    search_fields = ('title', 'description')