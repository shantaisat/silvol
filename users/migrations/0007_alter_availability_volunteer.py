# Generated by Django 5.1.7 on 2025-03-19 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_availability', to='users.userprofile'),
        ),
    ]
