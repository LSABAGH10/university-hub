# core/urls.py

from django.urls import path
# قم بإضافة guest_login_view هنا
from .views import advertise_view, advertise_success_view, OfferListView, guest_login_view

urlpatterns = [
    path('advertise/', advertise_view, name='advertise'),
    path('advertise/success/', advertise_success_view, name='advertise-success'),
    path('offers/', OfferListView.as_view(), name='offer-list'),
    path('guest-login/', guest_login_view, name='guest-login'), # <-- الرابط الجديد
]