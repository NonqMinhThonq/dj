# student/models.py
from django.db import models
from manage_university.models import University  # Tham chiếu mô hình University từ app 'university'
from django.contrib.auth.models import User

class Major(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='major', null=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null = True)
    lop = models.CharField(max_length=50, null = True)
    email = models.EmailField(max_length=255, unique=True)  # Đảm bảo email duy nhất
    address = models.TextField()
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    year_of_admission = models.DateField(null=True, blank=True)
    academic_year = models.CharField(max_length=10)
    university = models.ForeignKey(University, on_delete=models.CASCADE)  # Liên kết với University
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)  # Liên kết với Major
    image = models.ImageField(upload_to='student_image/', blank=True, null=True)
    gpa = models.FloatField(default=3)
    Awards = models.TextField(default='', blank=True)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students') # Liên kết với User model

    def save(self, *args, **kwargs):
        # Tính toán year_of_admission nếu nó chưa được cung cấp
        if not self.year_of_admission and self.date_of_birth:
            year_of_admission = self.date_of_birth.year + 18
            self.year_of_admission = str(year_of_admission)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
