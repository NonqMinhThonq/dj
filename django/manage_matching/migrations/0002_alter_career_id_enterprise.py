# Generated by Django 5.1.3 on 2024-12-09 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_matching', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='id_enterprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_matching.enterprise'),
        ),
    ]
