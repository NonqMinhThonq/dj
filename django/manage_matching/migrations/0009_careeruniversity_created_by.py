# Generated by Django 5.1.3 on 2024-12-10 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matching', '0008_career_requirement'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='careeruniversity',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CareerUniversity', to=settings.AUTH_USER_MODEL),
        ),
    ]
