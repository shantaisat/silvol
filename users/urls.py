from django.urls import path
from . import views
from .views import profile_view, edit_profile, delete_account

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('profile/', profile_view, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_account, name='delete_account'),
]