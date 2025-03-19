from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Home view
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

class Availability(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    #slug = models.SlugField(unique=True, blank=True)  # Add a slug field

    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(f"{self.volunteer.username}-{self.start_time.strftime('%Y%m%d%H%M')}")
        #super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.volunteer.username} - {self.start_time} to {self.end_time}"