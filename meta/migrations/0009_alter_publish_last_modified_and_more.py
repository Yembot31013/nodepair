# Generated by Django 4.1.1 on 2022-10-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0008_alter_publish_last_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
