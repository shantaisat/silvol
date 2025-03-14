from django.db import models
from django.contrib.auth.models import User
from datetime import date


# 1. Define the Skill model for volunteer skills
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # 2. Define the Appointment model for scheduled appointments
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]




class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # 3. Adding custom validation to prevent setting a past date with "pending" status
    def save(self, *args, **kwargs):
        if self.date < date.today() and self.status != 'completed':
            raise ValueError("Cannot set a past date with status 'pending'.")
        super(Appointment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status}"

