# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # هنا نحدد الحقول التي ستظهر في استمارة التسجيل
        fields = ('email', 'username', 'gender', 'college', 'academic_year', 'id_photo')