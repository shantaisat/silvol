from django.urls import path
from .views import home, profile_view, edit_profile, delete_account

urlpatterns = [
    path("", home, name="home"),  # Homepage or main user dashboard
    path("profile/", profile_view, name="profile"),  # View user profile
    path("profile/edit/", edit_profile, name="edit_profile"),  # Edit profile
    path("profile/delete/", delete_account, name="delete_account"),  # Delete account
]
# Compare this snippet from appointments/urls.py: