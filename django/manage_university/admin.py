from django.contrib import admin
from .models import University
# Register your models here.
class universityAdmin(admin.ModelAdmin):
    # Hiển thị tất cả các trường của model Workshop trong danh sách admin
    list_display = [field.name for field in University._meta.fields]

admin.site.register(University, universityAdmin)