from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'skills', 'availability', 'contact_info', 'languages_spoken']
