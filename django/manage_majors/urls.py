from django.urls import path
from .views_detail.major_detail import major_detail
from .views_detail.context_processors import major_list

urlpatterns = [
    path('majors/', major_list, name='major_list'),
    path('detail/<int:major_id>/', major_detail, name='major_detail'),
]
