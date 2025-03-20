from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.

@login_required
def availability_calendar(request):
    # Check if user is in the Referral group
    if request.user.groups.filter(name="Referral").exists():
        availabilities = Availability.objects.all()
        return render(request, "appointments/availability.html", {"availabilities": availabilities})
    else:
        return render(request, "users/permission_denied.html")



# List all appointments (CBV)
class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointments/appointment_list.html"  # Template for appointment list
    context_object_name = "appointments"  # The context name for the list of appointments

# View details of a specific appointment (CBV)
class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = "appointments/appointment_detail.html"  # Template for individual appointment details

# Create an appointment (FBV)
@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.volunteer = request.user  # Assign logged-in user as the volunteer
            appointment.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "appointments/create_appointment.html", {"form": form})

# Mark appointment as completed (FBV)
@login_required
def complete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.user == appointment.volunteer:  # Ensure only the assigned volunteer can complete it
        appointment.completed = True
        appointment.save()
    return redirect("appointment_list")

# Delete an appointment (FBV)
@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.user == appointment.volunteer:
        appointment.delete()
    return redirect("appointment_list")
