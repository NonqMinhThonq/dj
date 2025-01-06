from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from ..models import Student, University, Major
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

def student_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        lop = request.POST.get('class')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        year_of_admission = request.POST.get('year_of_admission')
        academic_year = request.POST.get('academic_year')
        major_id = request.POST.get('major')
        gpa = request.POST.get('gpa')
        Awards = request.POST.get('Awards')
        status = request.POST.get('status') == 'true'
        university = University.objects.get(created_by=request.user)
        print(gpa)

        # Validation logic


        # 2. Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Email không hợp lệ.")
            return redirect('student_add')

        # 3. Check if email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email này đã tồn tại trong hệ thống.")
            return redirect('student_add')

        # 4. Validate phone number (example: numeric and length between 10-15)
        if not phone.isdigit() or not (10 <= len(phone) <= 15):
            messages.error(request, "Số điện thoại không hợp lệ. Vui lòng nhập số từ 10 đến 15 chữ số.")
            return redirect('student_add')

        # # 5. Validate academic year (example: must be numeric or in YYYY format)
        # if not academic_year.isdigit() or len(academic_year) != 4:
        #     messages.error(request, "Năm học không hợp lệ. Vui lòng nhập năm ở định dạng YYYY.")
        #     return redirect('student_add')

        # # 6. Check if major_id exists
        # if not Major.objects.filter(id=major_id).exists():
        #     messages.error(request, "Ngành học không tồn tại.")
        #     return redirect('student_add')
        try:
            major = Major.objects.get(id=major_id) if major_id else None
            new_student = Student(
                name=name,
                gender=gender,
                lop=lop,
                date_of_birth=date_of_birth,
                email=email,
                address=address,
                phone=phone,
                academic_year=academic_year,
                year_of_admission=year_of_admission,
                university=university,
                major=major,
                Awards=Awards,
                gpa=gpa,
                status=status,
                created_by=request.user
            )
            new_student.save()

            messages.success(request, 'Student information updated successfully.')
            print(new_student)
            if 'notifications' not in request.session:
                request.session['notifications'] = []
            notification_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
            notification = f"The student '{name}' dc tao luc {notification_time}"
            request.session['notifications'].insert(0, notification)
            request.session.modified = True
        except University.DoesNotExist:
            messages.error(request, "Selected university does not exist.")
        except Major.DoesNotExist:
            messages.error(request, "Selected major does not exist.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
        return redirect('student_add')

    universities = University.objects.all()
    majors = Major.objects.all()

    return render(request, 'manage_student/student_add.html', {
        'universities': universities,
        'majors': majors
    })
