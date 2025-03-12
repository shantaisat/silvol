from django import forms
from .models import UserProfile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'skills', 'availability', 'contact_info', 'languages_spoken']
