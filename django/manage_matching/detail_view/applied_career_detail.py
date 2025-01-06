
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from manage_matching.models import Career, CareerUniversity, EnterpriseStudent
from django.db.models import OuterRef, Subquery
from manage_student.models import Student

@login_required
def applied_career_detail(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    university = request.user.universities.first()
    
    # Lấy danh sách sinh viên đã được gửi đi
    
    enterprise_students = EnterpriseStudent.objects.filter(enterprise=career.enterprise, career=career)
    # student_ids = enterprise_students.values_list('student_id', flat=True)
    # students = Student.objects.filter(id__in=student_ids)
    students = Student.objects.filter(id__in=enterprise_students.values_list('student_id', flat=True)).annotate(status_student=Subquery( enterprise_students.filter(student_id=OuterRef('id')).values('status_student')[:1])
)
    

    # Xử lý hủy ứng tuyển
    if request.method == "POST" and 'delete_application' in request.POST:
        application = get_object_or_404(CareerUniversity, career=career, university_id=university.id, is_deleted=False)
        application.is_deleted = True
        application.save()
        messages.success(request, "Bạn đã hủy ứng tuyển thành công.")
        return redirect('my_applied_careers')

    context = {
        'career': career,
        'students': students,
    }
    return render(request, 'manage_matching/applied_career_detail.html', context)
