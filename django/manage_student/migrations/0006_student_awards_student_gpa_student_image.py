# Generated by Django 5.1.3 on 2024-12-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_student', '0005_alter_student_year_of_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Awards',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=3),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_image/'),
        ),
    ]
