import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import University
from common_service.otp import confirm
from django.utils import timezone  # Để lấy thời gian hiện tại
from django.contrib import messages  # Để thông báo lỗi nếu thiếu trường
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from manage_student.models import Major

def manage_university(request):
    """
    View để quản lý thông tin trường học, thêm thông báo khi cập nhật thành công.
    """
    university = University.get_or_create_university(request.user)

    if request.method == 'POST':
        # Lấy thông tin từ form
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        current_academic_year = request.POST.get('current_academic_year')
        year_of_establishment = request.POST.get('year_of_establishment')
        head_teacher = request.POST.get('head_teacher')
        description = request.POST.get('description')
        motto = request.POST.get('motto')
        slogan = request.POST.get('slogan')
        major_id = request.POST.get('major')
        new_major_name = request.POST.get('new_major')
        print(current_academic_year)
        # Kiểm tra lỗi
        errors = []

        if not name or len(name) < 3:
            errors.append("Tên trường phải có ít nhất 3 ký tự.")
        if not email:
            errors.append("Email không được để trống.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Email không hợp lệ.")
        if not address or len(address) < 10:
            errors.append("Địa chỉ phải có ít nhất 10 ký tự.")
        if not phone or not phone.isdigit() or len(phone) < 10 or len(phone) > 15:
            errors.append("Số điện thoại phải là số hợp lệ từ 10 đến 15 ký tự.")
        if not current_academic_year or not re.match(r'^\d{4}-\d{4}$', current_academic_year):
            errors.append("Năm học hiện tại phải có định dạng 'YYYY-YYYY'.")
        if not year_of_establishment or not year_of_establishment.isdigit() or int(year_of_establishment) > timezone.now().year:
            errors.append("Năm thành lập phải là số và nhỏ hơn hoặc bằng năm hiện tại.")
        if not head_teacher or len(head_teacher) < 3:
            errors.append("Tên hiệu trưởng phải có ít nhất 3 ký tự.")
        if not description or len(description) < 20 or len(description) > 500:
            errors.append("Mô tả phải có từ 20 đến 500 ký tự.")
        if not motto or len(motto) < 5:
            errors.append("Phương châm phải có ít nhất 5 ký tự.")
        if not slogan or len(slogan) < 5:
            errors.append("Khẩu hiệu phải có ít nhất 5 ký tự.")

        # Nếu có lỗi, gửi thông báo và hiển thị lại form
        if errors:
            for error in errors:
                messages.error(request, error)
            # Truyền lại thông tin đã nhập vào context để người dùng không phải nhập lại từ đầu
            context = {
                'university': university,
                'form_data': {
                    'name': name,
                    'email': email,
                    'address': address,
                    'phone': phone,
                    'current_academic_year': current_academic_year,
                    'year_of_establishment': year_of_establishment,
                    'head_teacher': head_teacher,
                    'description': description,
                    'motto': motto,
                    'slogan': slogan,
                },
                'majors': Major.objects.all(),  # Truyền danh sách majors vào context
            }
            return render(request, 'manage_university/university.html', context)

        # Nếu không có lỗi, cập nhật thông tin
        university.name = name
        university.email = email
        university.address = address
        university.phone = phone
        university.current_academic_year = current_academic_year
        university.year_of_establishment = year_of_establishment
        university.head_teacher = head_teacher
        university.description = description
        university.motto = motto
        university.slogan = slogan
        university.save()
        messages.success(request, "Thay đổi thông tin trường học thành công.")
        # Thêm ngành mới nếu có
        if new_major_name:
            Major.objects.get_or_create(name=new_major_name, created_by=request.user, university_id=university.id)
        try:
            # Thêm thông báo vào session
            # update_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
            # if 'notifications' not in request.session:
            #     request.session['notifications'] = []
            # request.session['notifications'].insert(0,  # Thêm lên đầu danh sách
            #     f"University information updated successfully on {update_time}"
            # )
            # request.session.modified = True  

            # try:
            #     # Gửi email thông báo cho người dùng
            #     user_email = request.user.email
            #     title = 'Notification'
            #     content = f'Your university information has been successfully updated on {update_time}!'
            #     confirm(receiver=user_email, title=title, content=content)
            # except Exception as e:
            #     print(f"Error sending email: {e}")
            return redirect('manage_university')  # Sau khi lưu, chuyển hướng lại trang quản lý trường

        except Exception as e:
            # Nếu có lỗi xảy ra khi lưu, thông báo lỗi
            messages.error(request, f"Đã có lỗi xảy ra: {e}")
            return redirect('manage_university')

    else:
        # Nếu không phải là POST, trả về form trống hoặc thông tin trường
        context = {
            'university': university,
            'majors': Major.objects.all(),  # Truyền danh sách majors vào context
        }
        return render(
            request,
            'manage_university/university.html',  # Đảm bảo đây là template chính của bạn
            context
        )