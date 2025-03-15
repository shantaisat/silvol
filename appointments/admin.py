from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Appointment, Skill

class AppointmentAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

# Check if models are already registered before registering
if not admin.site.is_registered(Appointment):
    admin.site.register(Appointment, AppointmentAdmin)

if not admin.site.is_registered(Skill):
    admin.site.register(Skill)