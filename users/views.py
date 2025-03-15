from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import UserProfile

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
    from .forms import EditProfileForm  # ✅ Move import inside function to avoid circular import
    
    profile = get_object_or_404(UserProfile, user=request.user)  
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()
            return redirect("profile")  
    else:
        form = EditProfileForm(instance=profile)  

    return render(request, "users/edit_profile.html", {"form": form})

@login_required
def delete_account(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    profile.delete()  # Delete the user's profile
    user.delete()  # Delete the user account
    logout(request)  # Log out after deleting the account
    return redirect("home")  # Redirect to homepage after deletion

