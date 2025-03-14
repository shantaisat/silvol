from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import UserProfile
from .forms import EditProfileForm


def home(request):
    return render(request, 'index.html')  # Render your index.html template

# User Profile View
@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, "users/profile.html", {"profile": profile})

# Edit Profile
@login_required
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)  # Get the user's profile
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)  # Use EditProfileForm
        if form.is_valid():
            form.save()
            return redirect("profile")  # Redirect to the profile view after saving
    else:
        form = EditProfileForm(instance=profile)  # Pre-fill form with the current profile data

    return render(request, "users/edit_profile.html", {"form": form})

# Delete Account
@login_required
def delete_account(request):
    user = request.user
    user.delete()  # Delete the user account
    logout(request)  # Log out after deleting the account
    return redirect("home")  # Redirect to the homepage after deletion


