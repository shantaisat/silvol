from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('referral', 'Referral'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to Django's built-in User model
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Either Volunteer or Referral
    skills = models.TextField(blank=True, null=True)  # For Volunteers
    availability = models.TextField(blank=True, null=True)  # For Volunteers
    biography = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
