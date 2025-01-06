from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from manage_matching.models import CareerUniversity
from django.contrib import messages
from django.core.paginator import Paginator
from common_service.pagination import create_custom_page_range

@login_required
def my_applied_careers(request):
    try:
        university = request.user.universities.first()  # Lấy trường của người dùng
    except AttributeError:
        messages.error(request, 'Bạn chưa thuộc trường đại học nào.')
        return redirect('career_list')

    applied_careers = CareerUniversity.objects.filter(university_id=university.id, is_deleted=False).select_related('career')

    paginator = Paginator(applied_careers, 10)
    page_number = request.GET.get('page')
    applied_careers = paginator.get_page(page_number)

    current_page = applied_careers.number
    total_pages = paginator.num_pages
    custom_page_range = create_custom_page_range(current_page, total_pages)


    return render(request, 'manage_matching/my_applied_careers.html', {
        'applied_careers': applied_careers,
        'custom_page_range':custom_page_range
    })