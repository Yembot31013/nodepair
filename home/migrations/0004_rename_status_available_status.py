# Generated by Django 4.0 on 2023-01-14 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0003_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='Available_Status',
        ),
    ]
