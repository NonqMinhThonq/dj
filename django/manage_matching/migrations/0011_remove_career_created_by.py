# Generated by Django 5.1.3 on 2024-12-12 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matching', '0010_career_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='created_by',
        ),
    ]
