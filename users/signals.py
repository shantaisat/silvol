from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# Handle both creation and saving in one signal handler
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Check if the user already has a UserProfile
    if created:
        # Only create a UserProfile if one doesn't exist
        if not hasattr(instance, 'userprofile'):
            UserProfile.objects.create(user=instance)
    else:
        # If the user already exists, ensure the profile is saved
        instance.userprofile.save()
