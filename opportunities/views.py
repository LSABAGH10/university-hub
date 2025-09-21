# opportunities/views.py

from django.views.generic import ListView, DetailView
from .models import Opportunity

class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'opportunities/opportunity_list.html'
    context_object_name = 'opportunities'
    ordering = ['-post_date'] # لعرض الأحدث أولاً

class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'opportunities/opportunity_detail.html'
    context_object_name = 'opportunity'