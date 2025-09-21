# main_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_view # <-- قم باستيراد الـ view الجديد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # <-- هذا هو الرابط الجديد للصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('qa/', include('qa.urls')),
    path('opportunities/', include('opportunities.urls')),
    path('', include('core.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)