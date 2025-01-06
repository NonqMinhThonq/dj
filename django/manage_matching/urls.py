from django.urls import path
from .detail_view.career_list import career_list
from .detail_view.career_detail import career_detail
from .detail_view.career_apply import apply_career  
from .detail_view.select_student import select_students_for_internship
from .detail_view.applied_careers import my_applied_careers
from .detail_view.applied_career_detail import  applied_career_detail
from .detail_view.delete_apply import delete_application

urlpatterns =[
    path('list/', career_list, name='career_list'),
    path('detail/<int:career_id>/', career_detail, name='career_detail'),
    path('career/apply/<int:career_id>/', apply_career, name='apply_career'),
    path('internship-select/<int:career_id>/', select_students_for_internship, name='select_students_for_internship'),
    path('applied-careers/', my_applied_careers, name='my_applied_careers'), 
    path('applied-career-detail/<int:career_id>/', applied_career_detail, name='applied_career_detail'),
    path('delete-career/<int:career_id>/', delete_application, name='delete_application'),
]