from django.urls import path
from .detail_view.workshop_list import workshop_list
from .detail_view.workshop_detail import workshop_detail
urlpatterns =[
    path('list/', workshop_list, name='workshop_list'),
    path('detail/<int:pk>/', workshop_detail, name='workshop_detail'),
]