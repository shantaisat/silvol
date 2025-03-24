# Generated by Django 5.1.7 on 2025-03-24 23:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_referralprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dv76xhqok/image/upload/v1742855774/default-profile_bbotot.png', max_length=255, verbose_name='image'),
        ),
    ]
