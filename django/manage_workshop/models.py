from django.db import models
from manage_university.models import University
from manage_student.models import Major
from manage_matching.models import Enterprise
from django.contrib.auth.models import User
# Create your models here.

    
class Workshop(models.Model):
    topic = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='workshop_image/', blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.SET_NULL, related_name='workshop', null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, related_name='workshop', null=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, related_name='workshop', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workshop')

    def __str__(self):
        return self.name
    


