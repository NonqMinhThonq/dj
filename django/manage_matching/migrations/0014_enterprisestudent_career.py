# Generated by Django 5.1.3 on 2024-12-13 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matching', '0013_career_end_career_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisestudent',
            name='career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_matching.career'),
        ),
    ]
