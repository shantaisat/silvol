from django.urls import path
from .views import appointment_list, appointment_detail, create_appointment, complete_appointment, delete_appointment

urlpatterns = [
    path('', appointment_list, name='appointment_list'),
    path('<int:pk>/', appointment_detail, name='appointment_detail'),
    path('create/', create_appointment, name='create_appointment'),
    path('<int:pk>/complete/', complete_appointment, name='complete_appointment'),
    path('<int:pk>/delete/', delete_appointment, name='delete_appointment'),
]
# Compare this snippet from appointments/forms.py: