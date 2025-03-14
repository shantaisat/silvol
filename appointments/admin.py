from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Appointment, Skill

class AppointmentAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Appointment, AppointmentAdmin)

# Register Skill model to manage skills through the admin
admin.site.register(Skill)
