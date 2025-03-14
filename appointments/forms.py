from django import forms
from .models import Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['title', 'description', 'date', 'time', 'location']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Appointment'))
# Compare this snippet from appointments/models.py:
# from django.db import models
# from django.contrib.auth.models import User
#
# class Appointment
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField() # 24-hour format    location = models.CharField(max_length=100)
#     volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
#     completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
# Compare this snippet from users/models.py:
# from django.db import models
# from django.contrib.auth.models import User
#
# class UserProfile
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     biography = models.TextField(blank=True)
#     skills = models.CharField(max_length=100, blank=True)
#     availability = models.CharField(max_length=100, blank=True)
#     contact_info = models.CharField(max_length=100, blank=True)
#     languages_spoken = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return self.user.username
# Compare this snippet from appointments/templates/appointments/appointment_list.html:
# {% extends "base.html" %}
# {% block content %}   <h1>Appointments</h1>               
