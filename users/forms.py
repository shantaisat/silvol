from django import forms
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from django.core.exceptions import ValidationError
from .models import Availability
from .models import UserProfile

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('referral', 'Referral'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="Role")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        if user:    
            print(f"User created: {user}")
            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user)
        else:
            print("User creation failed.")
        return user



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # ✅ Prevents circular import initially
        fields = ['biography', 'skills', 'availability', 'contact_info', 'languages_spoken']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a short biography'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List your skills'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Your contact information'}),
            'languages_spoken': forms.TextInput(attrs={'placeholder': 'Languages you speak'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy Forms setup
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Changes', css_class='btn btn-primary'))


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['start_time', 'end_time', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Availability'))
