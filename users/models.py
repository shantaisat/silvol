from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('referral', 'Referral'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    skills = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    def clean(self):
        if self.user_type == 'volunteer':
            if not self.skills:
                raise ValidationError('Skills are required for volunteers.')
            if not self.availability:
                raise ValidationError('Availability is required for volunteers.')
        elif self.user_type == 'referral':
            if hasattr(self.user, 'referral_profile'):
                raise ValidationError('A referral profile already exists for this user.')
            
class ReferralProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="referral_profile")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Referral"



class Availability(models.Model):
    volunteer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="volunteer_availability")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.volunteer.user.username} - {self.start_time.strftime('%d %b %Y, %I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"

