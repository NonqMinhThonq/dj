from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from manage_matching.models import Career, CareerUniversity, EnterpriseStudent

@login_required
def delete_application(request, career_id):
    """
    Hủy ứng tuyển của trường đại học cho công việc và xóa sinh viên liên quan.
    """
    print('vaoday')
    career = get_object_or_404(Career, id=career_id)
    university = request.user.universities.first()

    if not university:
        messages.error(request, "Bạn không thuộc trường đại học nào! Vui lòng kiểm tra lại thông tin tài khoản.")
        return redirect('career_detail', career_id=career.id)

    application = CareerUniversity.objects.filter(career=career, university_id=university.id, is_deleted=False).first()

    if application:
        application.is_deleted = True  # Đánh dấu xóa mềm
        application.save()

        # Xóa tất cả các sinh viên liên quan trong bảng EnterpriseStudent
        related_students = EnterpriseStudent.objects.filter(career=career, enterprise=career.enterprise)
        related_students.delete()  # Xóa tất cả các bản ghi liên quan

        # Kiểm tra và xác nhận đã xóa
        if not related_students.exists():
            messages.success(request, "Đã hủy ứng tuyển công việc và xóa sinh viên liên quan thành công.")
        else:
            messages.error(request, "Có lỗi xảy ra khi xóa sinh viên liên quan.")
    else:
        messages.warning(request, "Không tìm thấy ứng tuyển để hủy.")

    return redirect('my_applied_careers')
