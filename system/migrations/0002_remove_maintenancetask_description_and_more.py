# Generated by Django 4.2.6 on 2023-10-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancetask',
            name='description',
        ),
        migrations.RemoveField(
            model_name='maintenancetask',
            name='frequency',
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='estimated_duration',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='priority',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maintenancetask',
            name='task_description',
            field=models.TextField(null=True),
        ),
    ]
