from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from ..models import Student, University, Major
from common_service.otp import confirm
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        lop = request.POST.get('lop')
        date_of_birth = request.POST.get('date_of_birth')
        year_of_admission = request.POST.get('year_of_admission')
        academic_year = request.POST.get('academic_year')
        
        major_id = request.POST.get('major')
        quote = request.POST.get('quote', '')
        available = request.POST.get('available') == 'on'
        status = request.POST.get('status') == 'on'
        print('lop', lop)
        try:
            print('vao day')
            
            major = Major.objects.get(id=major_id) if major_id else None
            # Cập nhật thông tin sinh viên
            student.name = name
            student.email = email
            student.address = address
            student.phone = phone
            student.lop = lop
            print('vao day', student.lop) 
            student.date_of_birth = date_of_birth
            student.year_of_admission = year_of_admission
            student.academic_year = academic_year
            student.major = major
            student.quote = quote
            student.available = available
            student.status = status
            student.save()

            messages.success(request, 'Student information updated successfully.')

            if 'notifications' not in request.session:
                request.session['notifications'] = []
            notification_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
            notification = f"The student '{name}' đã được cập nhật thông tin lúc {notification_time}"
            request.session['notifications'].insert(0, notification) 
            request.session.modified = True
            # try:
            #     user_email = request.user.email
            #     title = 'Notification'
            #     content = f"The student '{name}' đã được cập nhật thông tin lúc {notification_time}"
            #     confirm(receiver=user_email, title=title, content=content)
            # except Exception as e:
            #     print(f"Error sending email: {e}")
        except Exception as e:
            print(e)

    universities = University.objects.all()
    majors = Major.objects.all()

    return render(request, 'manage_student/student_edit.html', {
        'student': student,
        'universities': universities,
        'majors': majors
    })
