from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Appointment

class AppointmentAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Appointment, AppointmentAdmin)
