from django.contrib import admin
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.urls import path
from .models import Career, Enterprise, CareerUniversity, EnterpriseStudent
from .forms import CareerForm

class CareerAdmin(admin.ModelAdmin):
    form = CareerForm  # Đảm bảo sử dụng form đã chỉnh sửa

    class Media:
        js = ('admin/js/update_field.js',)  # Thêm file JavaScript vào Admin

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_fields/<int:enterprise_id>/', self.get_available_fields, name='get_available_fields'),
        ]
        return custom_urls + urls

    def get_available_fields(self, request, enterprise_id):
        try:
            enterprise = Enterprise.objects.get(id=enterprise_id)
            fields = enterprise.get_available_fields()  # Lấy các field từ enterprise
            return JsonResponse({'fields': fields})
        except Enterprise.DoesNotExist:
            return JsonResponse({'fields': []})
    list_display = ['id', 'enterprise', 'name']
admin.site.register(Career, CareerAdmin)

class CareerUniverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CareerUniversity._meta.fields]
admin.site.register(CareerUniversity, CareerUniverAdmin)

class Enterprise_Student(admin.ModelAdmin):
    list_display = [field.name for field in EnterpriseStudent._meta.fields]
admin.site.register(EnterpriseStudent, Enterprise_Student)