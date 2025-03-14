from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'skills', 'availability', 'contact_info', 'languages_spoken']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Changes'))
# {% for appointment in appointments %}
