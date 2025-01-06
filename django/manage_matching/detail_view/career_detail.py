from django.shortcuts import render, get_object_or_404
from manage_matching.models import Career, EnterpriseStudent

# @login_required
def career_detail(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    other = Career.objects.get(id=career_id)
    fields_value = other.field
    other_careers = Career.objects.filter(field=fields_value).exclude(id=career_id)[:5]

    # Kiểm tra xem đã có sinh viên nào được thêm vào thực tập cho Career này chưa
    students_added = EnterpriseStudent.objects.filter(enterprise=career.enterprise).exists()
    
    context = {
        'career': career,
        'other_careers': other_careers,
        'students_added': students_added,
    }
    
    return render(request, 'manage_matching/career_detail.html', context)
