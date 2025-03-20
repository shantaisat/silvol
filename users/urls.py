from django.urls import path, include
from . import views
from .views import (
    home,
    profile_view,
    edit_profile,
    delete_account,
    set_availability,
    view_availability,
    edit_availability,  
    delete_availability, 
    volunteer_list,
    volunteer_detail,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("", home, name="home"),  # Homepage or main user dashboard
    path("profile/", profile_view, name="profile"),  # View user profile
    path("profile/edit/", edit_profile, name="edit_profile"),  # Edit profile
    path("profile/set_availability/", set_availability, name="set_availability"),  # Set availability
    path('accounts/', include('allauth.urls')),  # Django-allauth URLs
    path("profile/view_availability/", view_availability, name="view_availability"),  # View availability
    path('profile/edit_availability/<int:availability_id>/', edit_availability, name='edit_availability'),
    path('profile/delete_availability/<int:availability_id>/', delete_availability, name='delete_availability'),
    path("goodbye/", TemplateView.as_view(template_name="goodbye.html"), name="goodbye"),  # Goodbye page

    path('volunteers/', volunteer_list, name='volunteer_list'),  # Volunteer list
    path('volunteer/<int:id>/', volunteer_detail, name='volunteer_detail'),  # Volunteer detail
]



