from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from django.core.exceptions import ValidationError

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['biography', 'skills', 'availability', 'contact_info', 'languages_spoken']
        # You can add widgets here to customize form field input styles if needed
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a short biography'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List your skills, separated by commas'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Your contact information (email, phone)'}),
            'languages_spoken': forms.TextInput(attrs={'placeholder': 'Languages you speak'}),
            'availability': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your availability details'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Changes', css_class='btn btn-primary'))

        # Additional customizations
        self.helper.form_class = 'form-horizontal'  # You can adjust form class for styling
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'

        # Ensure some fields are required based on your needs
        self.fields['biography'].required = True
        self.fields['skills'].required = True
        self.fields['availability'].required = True

    # Optional: You can add additional clean methods to validate fields.
    def clean_contact_info(self):
        contact_info = self.cleaned_data.get('contact_info')
        if not contact_info:
            raise ValidationError("Please provide your contact information.")
        return contact_info

    def clean_languages_spoken(self):
        languages_spoken = self.cleaned_data.get('languages_spoken')
        if languages_spoken and len(languages_spoken.split(',')) > 5:
            raise ValidationError("Please limit the number of languages to 5.")
        return languages_spoken

    