# Generated by Django 4.0 on 2023-02-19 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_rename_project_title_project_overview_title'),
        ('meta', '0013_rename_meta_title_overview_title'),
        ('dashboard', '0005_alter_payment_payed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.overview'),
        ),
        migrations.AlterField(
            model_name='project_order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectApp.project_overview'),
        ),
    ]
