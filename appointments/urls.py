from django.urls import path
from .views import AppointmentListView, AppointmentDetailView, create_appointment, complete_appointment, delete_appointment

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),  # CBV for listing appointments
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),  # CBV for appointment details
    path('appointments/create/', create_appointment, name='create_appointment'),  # FBV for creating appointments
    path('appointments/<int:pk>/complete/', complete_appointment, name='complete_appointment'),  # FBV for completing appointments
    path('appointments/<int:pk>/delete/', delete_appointment, name='delete_appointment'),  # FBV for deleting appointments
]