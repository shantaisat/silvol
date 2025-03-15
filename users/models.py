from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('referral', 'Referral'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    skills = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    languages_spoken = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    def get_user_type_display(self):
        return dict(self.USER_TYPE_CHOICES).get(self.user_type)

    def clean(self):
        # Custom validation to ensure 'skills' and 'availability' are provided for 'volunteer' users
        if self.user_type == 'volunteer':
            if not self.skills:
                raise ValidationError('Skills are required for volunteers.')
            if not self.availability:
                raise ValidationError('Availability is required for volunteers.')
