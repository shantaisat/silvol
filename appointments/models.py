from django.db import models
from django.contrib.auth.models import User



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

    def __str__(self):
        return f"{self.title} - {self.status}"

