from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import UserProfile, Availability#  Make sure these are properly defined in models.py
from .models import ReferralProfile
from .forms import ReferralProfileForm
from users.forms import AvailabilityForm, EditProfileForm
from django.db.models import Q # Import Q for complex queries

# Home view
def home(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'profile': request.user.userprofile})



@login_required
# Use a view to render the volunteers_list page
def volunteer_list(request):
    volunteers = UserProfile.objects.filter(user_type='volunteer')
    return render(request, 'volunteers_list.html', {'volunteers': volunteers})

# Profile View
@login_required
def profile_view(request):
    # Fetch the UserProfile for the logged-in user
    profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch availabilities associated with the UserProfile
    availabilities = Availability.objects.filter(volunteer=profile)

    return render(request, "users/profile.html", {
        "profile": profile,
        "availabilities": availabilities
    })

@login_required
def referral_profile_view(request):
    # Check if the user already has a referral profile
    referral_profile, created = ReferralProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ReferralProfileForm(request.POST, instance=referral_profile)
        if form.is_valid():
            form.save()
            return redirect('referral_profile')  # Redirect to the same page or another page
    else:
        form = ReferralProfileForm(instance=referral_profile)

    return render(request, 'users/referral_profile.html', {'form': form})
 



# List of Volunteers
@login_required
def volunteer_list(request):
    query = request.GET.get('q', '')  # Get search query from GET parameters

    if query:
        # If there's a search query, filter volunteers based on username and user_type
        volunteers = UserProfile.objects.filter(
            user__username__icontains=query,
            user_type='volunteer'  # Only include volunteers
        )
    else:
        # If there's no search query, return all volunteers
        volunteers = UserProfile.objects.filter(user_type='volunteer')  # Only volunteers

    return render(request, "users/volunteers_list.html", {"volunteers": volunteers, "query": query})

# Volunteer Detail
@login_required
def volunteer_detail(request, id):
    volunteer = get_object_or_404(UserProfile, id=id)
    return render(request, "users/volunteer_detail.html", {"volunteer": volunteer})



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
            # Fetch the UserProfile for the logged-in user
            availability.volunteer = request.user.userprofile  # Use the UserProfile instance
            availability.save()
            return redirect('profile')  # Redirect after successful submission
    else:
        form = AvailabilityForm()

    return render(request, 'users/set_availability.html', {'form': form})

# View Availability
@login_required
def view_availability(request):
    # Fetch the UserProfile for the logged-in user
    user_profile = request.user.userprofile

    # Fetch availabilities associated with the UserProfile
    availabilities = Availability.objects.filter(volunteer=user_profile)

    return render(request, 'users/view_availability.html', {'availabilities': availabilities})    # View Availability
    @login_required
    def view_availability(request):
        # Fetch the UserProfile for the logged-in user
        user_profile = request.user.userprofile
    
        # Fetch availabilities associated with the UserProfile
        availabilities = Availability.objects.filter(volunteer=user_profile)
    
        return render(request, 'users/view_availability.html', {'availabilities': availabilities})

# Edit Availability
@login_required
def edit_availability(request, availability_id):
    # Fetch the availability or return a 404 if not found or if it doesn't belong to the user's UserProfile
    availability = get_object_or_404(Availability, id=availability_id, volunteer=request.user.userprofile)

    if request.method == "POST":
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            return redirect('view_availability')  # Redirect to view after saving
    else:
        form = AvailabilityForm(instance=availability)

    return render(request, 'users/edit_availability.html', {'form': form, 'availability': availability})
 
# Delete Availability
@login_required
def delete_availability(request, availability_id):
    # Fetch the availability or return a 404 if not found or if it doesn't belong to the user's UserProfile
    availability = get_object_or_404(Availability, id=availability_id, volunteer=request.user.userprofile)
    availability.delete()
    messages.success(request, "Availability deleted successfully.")
    return redirect('view_availability')  # Redirect to the availability list after deletion
