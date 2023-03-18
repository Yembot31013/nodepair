# Generated by Django 4.0 on 2022-11-04 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_alter_project_pricing_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_overview',
            name='progress',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project_search_keyword',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keyword', to='projectApp.project_overview'),
        ),
    ]
