from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'enterprise', 'created_by']
    list_filter = ['topic'] 

admin.site.register(Workshop, WorkshopAdmin)
