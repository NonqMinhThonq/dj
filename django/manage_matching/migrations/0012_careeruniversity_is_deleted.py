# Generated by Django 5.1.3 on 2024-12-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matching', '0011_remove_career_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='careeruniversity',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
