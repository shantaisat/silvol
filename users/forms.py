from allauth.account.forms import SignupForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import Group
from .models import UserProfile, Availability
from .models import UserProfile


class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('referral', 'Referral'),
    ]
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=True, label="Role")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        # Create the UserProfile for the user
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.user_type = self.cleaned_data["user_type"]
        profile.save()

        # Assign user to the correct group
        group_name = "Volunteer" if profile.user_type == "volunteer" else "Referral"
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return user


class EditProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=True, label="Role", disabled=True)

    class Meta:
        model = UserProfile
        fields = ['user_type', 'biography', 'skills', 'availability', 'contact_info', 'languages_spoken']
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a short biography'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List your skills'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Your contact information'}),
            'languages_spoken': forms.TextInput(attrs={'placeholder': 'Languages you speak'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Changes', css_class='btn btn-primary'))

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['start_time', 'end_time', 'description']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
