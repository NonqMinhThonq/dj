from itertools import count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from manage_student.models import Major, Student
from manage_workshop.models import Workshop
from manage_matching.models import CareerUniversity, Career
from manage_university.models import University
from django.db.models import Count
# Create your views here.
def home_view(request):
        # Truy vấn dữ liệu từ bảng Career
    career_data = Career.objects.values('field').annotate(count=Count('field')).order_by('-count')
    
    # Chuẩn bị dữ liệu cho biểu đồ
    labels = [item['field'] for item in career_data]
    data = [item['count'] for item in career_data]
    colors = ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#858796', '#5a5c69']
    # Lấy tất cả CareerUniversity của người dùng hiện tại
    university_ids = University.objects.filter(created_by=request.user).values_list('id', flat=True)
    user_career_universities = CareerUniversity.objects.filter(university_id__in=university_ids, is_deleted=False)

    # Đếm số lượng các đối tượng khác
    total_majors = Major.objects.filter(created_by=request.user).count()
    print(f"Total majors: {total_majors}") 
    total_student = Student.objects.filter(created_by=request.user).count()
    total_workshop = Workshop.objects.filter(created_by=request.user).count()

    #     # Lấy tất cả CareerUniversity của người dùng hiện tại
    # university_ids = University.objects.filter(created_by=request.user).values_list('id', flat=True)
    # user_career_universities = CareerUniversity.objects.filter(university_id__in=university_ids, is_deleted=False)

    # Đếm số lượng CareerUniversity đã tạo bởi người dùng hiện tại
    total_applied = user_career_universities.count()
    print(f"Total total_applied: {total_applied}") 
    # Truy vấn dữ liệu từ bảng Student cho biểu đồ Area Chart
    # QuerySet của Student được tạo bởi người dùng hiện tại
    academic_year_data = Student.objects.filter(created_by=request.user).values('academic_year').annotate(count=Count('academic_year')).order_by('academic_year')
    area_labels = [item['academic_year'] for item in academic_year_data]
    area_data = [item['count'] for item in academic_year_data]
    
    print(f"area_labels: {area_labels}")

    # Chuyển tất cả dữ liệu vào context và trả về view
    context = {
        'total_majors': total_majors,
        'total_student': total_student,
        'total_workshop': total_workshop,
        'total_applied': total_applied,
        'labels': labels,
        'data': data,
        'colors': colors[:len(labels)],
        'area_labels': area_labels,
        'area_data': area_data,
    }


    
    return render(request, 'home/home.html', context)


from django.urls import reverse

def logout_view(request):
    logout(request)
    return redirect(reverse('login')) 


def show_all_notifications(request):
    notifications = request.session.get('notifications', [])
    return render(request, 'frame/all_notifications.html', {'notifications': notifications})
