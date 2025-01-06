from django.shortcuts import render
from ..models import Workshop
from django.core.paginator import Paginator
from common_service.pagination import create_custom_page_range

def workshop_list(request):
    workshops = Workshop.objects.filter(created_by=request.user).order_by('-id')
    print('vao day')

    paginator = Paginator(workshops, 5)
    page_number = request.GET.get('page')
    workshops_page = paginator.get_page(page_number)

    current_page = workshops_page.number
    total_pages = paginator.num_pages
    custom_page_range = create_custom_page_range(current_page, total_pages)

    return render(request, 'manage_workshop/workshop_list.html',{
        'workshops': workshops,
        'custom_page_range': custom_page_range,
        'workshops_page':workshops_page
    })

