# Generated by Django 4.1.1 on 2022-10-16 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0005_alter_publish_last_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2022, 10, 16, 14, 27, 2, 387256, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
