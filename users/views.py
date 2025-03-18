from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile, Availability
from .forms import AvailabilityForm, EditProfileForm

# Home view
def home(request):
    return render(request, 'index.html')

# Profile View
@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    availabilities = Availability.objects.filter(volunteer=request.user)

    return render(request, "users/profile.html", {
        "profile": profile,
        "availabilities": availabilities
    })

# Edit Profile
@login_required
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")  
    else:
        form = EditProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})

# Delete Account
@login_required
def delete_account(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    profile.delete()  # Delete the user's profile
    user.delete()  # Delete the user account
    logout(request)  # Log out after deleting the account
    return HttpResponseRedirect(reverse("goodbye"))  # Redirect to goodbye page

# Set Availability
@login_required
def set_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.volunteer = request.user  # Associate the logged-in user
            availability.save()
            return redirect('profile')  # Redirect after successful submission
    else:
        form = AvailabilityForm()

    return render(request, 'users/set_availability.html', {'form': form})

# View Availability
@login_required
def view_availability(request):
    availabilities = Availability.objects.filter(volunteer=request.user)
   
    return render(request, 'users/view_availability.html', {'availabilities': availabilities})

@login_required
def edit_availability(request, availability_id):
    availability = get_object_or_404(Availability, id=availability_id, volunteer=request.user)
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after editing
    else:
        form = AvailabilityForm(instance=availability)

    return render(request, 'users/edit_availability.html', {'form': form})
