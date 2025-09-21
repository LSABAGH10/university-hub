# core/urls.py

from django.urls import path
from .views import advertise_view, advertise_success_view, OfferListView # <-- أضف الجديد

urlpatterns = [
    path('advertise/', advertise_view, name='advertise'),
    path('advertise/success/', advertise_success_view, name='advertise-success'),
    path('offers/', OfferListView.as_view(), name='offer-list'), # <-- الرابط الجديد
]