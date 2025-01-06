from django.contrib import admin
from .models import Major, Student
# Register your models here.

class Majoradmin(admin.ModelAdmin):
    list_display = [field.name for field in Major._meta.fields]

    list_filter = ['name']
admin.site.register(Major, Majoradmin)

class Studentadmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
    search_fields = ['major', 'name', 'address', 'id']
admin.site.register(Student, Studentadmin)