# Generated by Django 5.1.3 on 2024-11-21 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birthadate',
            new_name='birthDate',
        ),
    ]
