# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from manage_student.models import Student
# from manage_matching.models import EnterpriseStudent, Enterprise  # Sửa lại đường dẫn import theo app của bạn
# from .models import Career

# # @login_required
# # def student_enterprise(request, student_id):
# #     student = get_object_or_404(Student, id=student_id)
# #     enterprise_students = EnterpriseStudent.objects.filter(student_id=student_id)
# #     enterprises = [enterprise_student.enterprise for enterprise_student in enterprise_students]

# #     return render(request, 'manage_matching/student_enterprise.html', {'student': student, 'enterprises': enterprises})

# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.contrib.auth.decorators import login_required
# # from django.contrib import messages
# # from manage_student.models import Student
# # from manage_matching.models import EnterpriseStudent, Enterprise  # Adjust the import paths according to your app structure
# # from .models import Career

# # @login_required
# # def add_internship(request, career_id):

# #     career = get_object_or_404(Career, id=career_id)
# #     other_careers = Career.objects.exclude(id=career_id)
# #     # Lọc sinh viên dựa trên lĩnh vực
# #     students = Student.objects.filter(major__name=career.field)
# #     print('vao day2')

# #     if request.method == 'POST':
# #         if 'student_ids' in request.POST:
# #             start_date = request.POST.get('start_date')
# #             end_date = request.POST.get('end_date')
            
# #             selected_students = request.POST.getlist('student_ids')  # Lấy danh sách sinh viên đã chọn
# #             for student_id in selected_students:
# #                 student = get_object_or_404(Student, id=student_id)
# #                 # Thêm vào bảng EnterpriseStudent
# #                 EnterpriseStudent.objects.create(
# #                     enterprise=career.enterprise,
# #                     student_id=student.id,
# #                     start=start_date,
# #                     end=end_date
# #                 )
# #             messages.success(request, 'Đã thêm sinh viên vào kỳ thực tập.')
# #         elif 'delete_application' in request.POST:
# #             # Logic xóa ứng dụng
# #             career.students.clear()  # Loại bỏ tất cả sinh viên khỏi career
# #             EnterpriseStudent.objects.filter(enterprise=career.enterprise).delete()
# #             messages.success(request, 'Đã hủy ứng dụng.')

# #         return redirect('add_internship', career_id=career_id)

# #     return render(request, 'manage_matching/add_student.html', {
# #         'career': career,
# #         'other_careers': other_careers,
# #         'students': students,
# #     })



# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.contrib import messages
# # from django.contrib.auth.decorators import login_required
# # from manage_matching.models import Career, EnterpriseStudent
# # from manage_student.models import Student

# # @login_required
# # def select_students_for_internship(request, career_id):
# #     career = get_object_or_404(Career, id=career_id)
# #     students = Student.objects.filter(major__name=career.field).distinct()

# #     if request.method == "POST":
# #         student_ids = request.POST.getlist('student_ids')
# #         start_date = career.start
# #         end_date = career.end

# #         if len(student_ids) > career.number_of_recruitment:
# #             messages.error(request, f"Bạn chỉ có thể chọn tối đa {career.number_of_recruitment} sinh viên.")
# #             return render(request, 'manage_matching/select_students_for_internship.html', {
# #                 'career': career,
# #                 'students': students,
# #                 'number_of_recruitment': career.number_of_recruitment,
# #                 'start_date': career.start,
# #                 'end_date': career.end,
# #             })

# #         for student_id in student_ids:
# #             EnterpriseStudent.objects.create(
# #                 enterprise=career.enterprise,
# #                 student_id=student_id,
# #                 start=start_date,
# #                 end=end_date
# #             )
# #         return redirect('career_detail', career_id=career.id)

# #     context = {
# #         'career': career,
# #         'students': students,
# #         'number_of_recruitment': career.number_of_recruitment,
# #         'start_date': career.start,
# #         'end_date': career.end,
# #     }
    
# #     return render(request, 'manage_matching/select_students_for_internship.html', context)

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from manage_matching.models import Career, EnterpriseStudent, CareerUniversity
# from manage_student.models import Student

# @login_required
# def select_students_for_internship(request, career_id):
#     career = get_object_or_404(Career, id=career_id)
#     university = request.user.universities.first()
#     students = Student.objects.filter(major__name=career.field).distinct()

#     if request.method == "POST":
#         student_ids = request.POST.getlist('student_ids')
#         start_date = career.start
#         end_date = career.end

#         for student_id in student_ids:
#             EnterpriseStudent.objects.create(
#                 enterprise=career.enterprise,
#                 career=career,
#                 student_id=student_id,
#                 start=start_date,
#                 end=end_date
#             )

#         # Lưu thông tin apply vào bảng CareerUniversity
#         CareerUniversity.objects.get_or_create(
#             career=career,
#             university_id=university.id,
#             defaults={'number_of_recruitment': career.number_of_recruitment}
#         )

#         messages.success(request, 'Bạn đã chọn sinh viên thành công!')
#         return redirect('my_applied_careers')

#     context = {
#         'career': career,
#         'students': students,
#         'number_of_recruitment': career.number_of_recruitment,
#         'start_date': career.start,
#         'end_date': career.end,
#     }
    
#     return render(request, 'manage_matching/select_students_for_internship.html', context)


# from django.shortcuts import render
# from manage_matching.models import CareerUniversity

# @login_required
# def applied_careers_list(request):
#     university = request.user.universities.first()
#     if not university:
#         messages.error(request, "Bạn không thuộc trường đại học nào! Vui lòng kiểm tra lại thông tin tài khoản.")
#         return redirect('career_list')  # Chuyển hướng đến trang danh sách công việc nếu không thuộc trường đại học nào

#     applied_careers = CareerUniversity.objects.filter(university_id=university.id, is_deleted=False)

#     context = {
#         'applied_careers': applied_careers,
#     }

#     return render(request, 'manage_matching/applied_careers_list.html', context)


# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from manage_matching.models import CareerUniversity
# from manage_student.models import Student

# @login_required
# def my_applied_careers(request):
#     try:
#         university = request.user.universities.first()  # Lấy trường của người dùng
#     except AttributeError:
#         messages.error(request, 'Bạn chưa thuộc trường đại học nào.')
#         return redirect('career_list')

#     applied_careers = CareerUniversity.objects.filter(university_id=university.id, is_deleted=False).select_related('career')
#     return render(request, 'manage_matching/my_applied_careers.html', {
#         'applied_careers': applied_careers,
#     })


# @login_required
# def applied_career_detail(request, career_id):
#     """
#     Hiển thị chi tiết công việc đã apply và danh sách sinh viên đã được gửi đi.
#     """
#     career = get_object_or_404(Career, id=career_id)
    
#     # Lấy danh sách sinh viên thông qua bảng EnterpriseStudent
#     enterprise_students = EnterpriseStudent.objects.filter(enterprise=career.enterprise, career=career)
#     student_ids = enterprise_students.values_list('student_id', flat=True)
#     students = Student.objects.filter(id__in=student_ids)

#     context = {
#         'career': career,
#         'students': students,
#     }
#     return render(request, 'manage_matching/applied_career_detail.html', context)
