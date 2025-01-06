from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Student, Major
from common_service.pagination import create_custom_page_range
from django.http import Http404
from django.utils import timezone
from common_service.otp import confirm
from django.db.models import Q
from django.contrib import messages

def student_list(request):
    # Lấy giá trị từ GET request
    search_query = request.GET.get('search', '').strip()
    selected_academic_years = request.GET.getlist('academic_years')
    selected_majors = request.GET.getlist('majors')
    selected_classes = request.GET.getlist('classes')

    # Lọc học sinh theo các điều kiện
    students = Student.objects.filter(created_by=request.user)

    # Tìm kiếm theo tên nếu có
    if search_query.isdigit():
        students = students.filter(id__icontains=search_query)
    else:
        search_terms = search_query.split()
        for term in search_terms:
            query = Q(name__iregex=rf'(^|\s){term}(\s|$)')
            students = students.filter(query)

    # Lọc theo ngành học (majors)
    if selected_majors:
        students = students.filter(major__id__in=selected_majors)

    # Lọc theo lớp học (classes)
    if selected_classes:
        students = students.filter(lop__in=selected_classes)

    # Lấy danh sách các năm học và xử lý để hiển thị "5+" nếu có năm học lớn hơn 5
    academic_years = Student.objects.values_list('academic_year', flat=True).distinct()
    processed_years = []
    has_5_plus = False  # Biến để kiểm tra nếu có năm lớn hơn 5

    for year in academic_years:
        if int(year) > 5:
            has_5_plus = True  # Đánh dấu rằng có ít nhất một năm lớn hơn 5
        else:
            processed_years.append(year)
    processed_years.sort()
    # Nếu có năm lớn hơn 5, thêm mục "5+" vào danh sách
    if has_5_plus:
        processed_years.append('5+')

    # Lọc danh sách sinh viên theo năm học
    filtered_by_academic_years = Q()
    if '5+' in selected_academic_years:
        filtered_by_academic_years |= Q(academic_year__gt=5)
        selected_academic_years.remove('5+')
    if selected_academic_years:
        filtered_by_academic_years |= Q(academic_year__in=selected_academic_years)
    
    if filtered_by_academic_years:
        students = students.filter(filtered_by_academic_years)

    majors_list = Major.objects.all()
    student_classes_list = Student.objects.values_list('lop', flat=True).distinct()

    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    current_page = students.number
    total_pages = paginator.num_pages
    custom_page_range = create_custom_page_range(current_page, total_pages)

    return render(request, 'manage_student/student_list.html', {
        'search_query': search_query,
        'academic_years': processed_years,
        'selected_academic_years': request.GET.getlist('academic_years'),  # giữ lại các giá trị đã chọn
        'majors': majors_list,
        'selected_majors': selected_majors,
        'student_classes': student_classes_list,
        'selected_classes': selected_classes,
        'students': students,
        'custom_page_range': custom_page_range,
    })

@login_required
def student_delete(request, id):
    student = Student.objects.filter(id=id).first()
    if not student:
        raise Http404("Student not found")
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, 'Student deleted successfully.') 
        if 'notifications' not in request.session:
            request.session['notifications'] = []
        notification_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
        notification = f"The student '{student_name}' has been deleted on {notification_time}"
        request.session['notifications'].insert(0, notification)
        request.session.modified = True
        # try:
        #     user_email = request.user.email
        #     title = 'Notification'
        #     content = f"The student '{student_name}' has been deleted on {notification_time}"
        #     asyncio.create_task(confirm(receiver=user_email, title=title, content=content))
        # except Exception as e:
        #     print(f"Error sending email: {e}")
        return redirect('student_list')
    return redirect('student_list')