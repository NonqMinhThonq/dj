from django.db import models
from django.contrib.auth.models import User

class Career(models.Model):
    enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='career_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirement = models.TextField(blank=True, null=True)
    number_of_recruitment = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class CareerUniversity(models.Model):
    
    career = models.ForeignKey('Career', on_delete=models.SET_NULL, null=True)
    university_id = models.IntegerField()
    number_of_recruitment = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='CareerUniversity', null=True)

    def save(self, *args, **kwargs):
        if not self.created_by:  # Nếu chưa có giá trị cho created_by
            self.created_by = self._get_current_user()
        super().save(*args, **kwargs)

    def _get_current_user(self):
        # Giả sử bạn có thể truy xuất user qua request trong context (sử dụng trong view)
        return self.request.user if hasattr(self, 'request') else None
    
    def __str__(self):
        return f"Career {self.career.name} - University {self.university_id}"


class CareerMajor(models.Model):
    career = models.ForeignKey('Career', on_delete=models.SET_NULL, null=True)
    major_id = models.IntegerField()

    def __str__(self):
        return f"Career {self.career.name} - Major {self.major_id}"


class Enterprise(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    def get_available_fields(self):
        if self.field:
            return self.field.split(',')  # Trả về danh sách các field
        return []


class EnterpriseStudent(models.Model):
    enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)
    career = models.ForeignKey('Career', on_delete=models.SET_NULL,null=True)
    student_id = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    status_student = models.CharField(max_length=255, blank=True, null=True, default='Đang thực tập',choices=[('Trượt', 'Trượt'),('Đang thực tập', 'Đang thực tập'),('Hoàn thành', 'Hoàn thành')])

    def __str__(self):
        return f"Enterprise {self.enterprise.name} - Student {self.student_id}"



