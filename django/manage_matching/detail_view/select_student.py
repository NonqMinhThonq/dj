from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from manage_matching.models import Career, EnterpriseStudent, CareerUniversity
from manage_student.models import Student
from common_service.pagination import create_custom_page_range
from django.core.paginator import Paginator

@login_required
def select_students_for_internship(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    university = request.user.universities.first()
    
    # Lọc ra những sinh viên chưa được cử đi thực tập ở công việc khác
    students = Student.objects.filter(major__name=career.field).exclude(id__in=EnterpriseStudent.objects.values_list('student_id', flat=True)).distinct()
    if request.method == "POST":
        student_ids = request.POST.getlist('student_ids')
        start_date = career.start
        end_date = career.end
        error_messages = []

        for student_id in student_ids:
            # Kiểm tra xem sinh viên đã được cử đi công việc nào khác chưa
            if EnterpriseStudent.objects.filter(student_id=student_id).exists():
                student = Student.objects.get(id=student_id)
                error_messages.append(f"Sinh viên {student.name} đã được cử đi công việc khác.")
                continue  # Bỏ qua sinh viên này và tiếp tục với sinh viên tiếp theo

            EnterpriseStudent.objects.create(
                enterprise=career.enterprise,
                career=career,
                student_id=student_id,
                start=start_date,
                end=end_date
            )

        # Lưu thông tin apply vào bảng CareerUniversity
        career_university, created = CareerUniversity.objects.get_or_create(
            career=career,
            university_id=university.id,
            defaults={'number_of_recruitment': career.number_of_recruitment}
        )

        if not created and career_university.is_deleted:
            career_university.is_deleted = False
            career_university.save()

        if error_messages:
            messages.error(request, "Có lỗi xảy ra:\n" + "\n".join(error_messages))
        else:
            messages.success(request, 'Bạn đã chọn sinh viên thành công!')

        return redirect('select_students_for_internship', career_id=career.id)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    current_page = students.number
    total_pages = paginator.num_pages
    custom_page_range = create_custom_page_range(current_page, total_pages)

    context = {
        'career': career,
        'students': students,
        'number_of_recruitment': career.number_of_recruitment,
        'start_date': career.start,
        'end_date': career.end,
        'custom_page_range': custom_page_range,
    }
    
    return render(request, 'manage_matching/select_students_for_internship.html', context)
