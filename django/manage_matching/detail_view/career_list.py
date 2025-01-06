from django.shortcuts import render
from common_service.pagination import create_custom_page_range
from ..models import Career, Enterprise
from django.core.paginator import Paginator

def career_list(request):
    career = Career.objects.all().order_by('-id')
    fields = set(Enterprise.objects.values_list('field', flat=True))

    # Lọc theo field nếu có
    selected_field = request.GET.get('field', '').strip()  # Loại bỏ khoảng trắng thừa
    if selected_field:
        career = career.filter(field__iexact=selected_field) 

    paginator = Paginator(career, 10)
    page_number = request.GET.get('page')
    careers = paginator.get_page(page_number)

    current_page = careers.number
    total_pages = paginator.num_pages
    custom_page_range = create_custom_page_range(current_page, total_pages)

    return render(request, 'manage_matching/career_list.html', {
        # 'Career': career,
        'fields': fields,
        'custom_page_range': custom_page_range,
        'careers':careers
    })


