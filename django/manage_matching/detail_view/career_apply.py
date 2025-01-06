from django.shortcuts import render, redirect, get_object_or_404
from ..models import Career, CareerUniversity
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from manage_university.models import University

@login_required
def apply_career(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    print('ddsaf')
    try:
        university = request.user.universities.first()  # Lấy trường của người dùng (giả sử mỗi người dùng chỉ quản lý một trường)

        if not university:
            messages.error(request, 'Bạn chưa thuộc trường đại học nào để apply công việc này.')
            return redirect('career_detail', career_id=career.id)

    except AttributeError:
        messages.error(request, 'Bạn chưa thuộc trường đại học nào để apply công việc này.')
        return redirect('career_detail', career_id=career.id)

    career_university, created = CareerUniversity.objects.get_or_create(
        career=career,
        university_id=university.id,
        defaults={'number_of_recruitment': career.number_of_recruitment}
    )

    if not created:
        if career_university.is_deleted:
            career_university.is_deleted = False
            career_university.save()
            messages.success(request, 'Bạn đã apply lại thành công vào công việc này!')
        else:
            messages.info(request, 'Bạn đã apply công việc này rồi.')
    else:
        messages.success(request, 'Bạn đã apply thành công vào công việc này!')

    return redirect('career_detail', career_id=career.id)

