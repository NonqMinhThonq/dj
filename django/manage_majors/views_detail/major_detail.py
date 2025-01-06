from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from manage_student.models import Student, Major 
from manage_workshop.models import Workshop
from manage_matching.models import EnterpriseStudent
from django.core.paginator import Paginator
from common_service.pagination import create_custom_page_range

@login_required
def major_detail(request, major_id):
    try:
        major = get_object_or_404(Major, id=major_id)
        students = Student.objects.filter(major=major)
        # Thống kê số lượng sinh viên trong khoa
        total_majors = students.count()

        # Thống kê số lượng sinh viên đang thực tập (có trong bảng EnterpriseStudent)
        total_students_interning = EnterpriseStudent.objects.filter(student_id__in=students.values_list('id', flat=True)).count()

        # Đếm số lượng workshop theo điều kiện major_id = id tren url
        total_workshop = Workshop.objects.filter(major_id=major_id).count()

        # thogn ke so lop co trong khoa
        total_classes = students.values('lop').distinct().count()


        paginator = Paginator(students, 10)
        page_number = request.GET.get('page')
        students = paginator.get_page(page_number)

        current_page = students.number
        total_pages = paginator.num_pages
        custom_page_range = create_custom_page_range(current_page, total_pages)

        context = {
            'major': major,
            'students': students,
            'total_majors': total_majors,
            'total_students_interning': total_students_interning,
            'total_workshop': total_workshop,
            'classes': total_classes,
            'custom_page_range':custom_page_range
        }
        return render(request, 'manage_majors/major_detail.html', context)
    except Major.DoesNotExist:
        return render(request, 'manage_majors/major_detail.html', {
            'error': 'Major not found.',
        })
    except Exception as e:
        print(f"Error fetching students for major {major_id}: {e}")
        return render(request, 'manage_majors/major_detail.html', {
            'error': 'An error occurred. Please try again later.',
        })
