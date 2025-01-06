from django.shortcuts import render
from manage_student.models import Major
from manage_university.models import University

# def major_list(request):
#     majors = []
#     try:
#         if request.user.is_authenticated:
#             try:
#                 university = University.objects.get(created_by=request.user)
#                 majors = Major.objects.filter(university=university)
#             except University.DoesNotExist:
#                 print("University not found for the user:", request.user)
#             except Exception as e:
#                 print("Error fetching majors for the university:", e)
#         else:
#             print("User is not authenticated.")
#     except Exception as e:
#         print("Error in context processor major_list:", e)

#     return {'majors': majors}



def major_list(request):
    majors = []
    try:
        if request.user.is_authenticated:
            try:
                university = University.objects.get(created_by=request.user)
                majors = Major.objects.filter(university=university)
            except University.DoesNotExist:
                print("University not found for the user:", request.user)
            except Exception as e:
                print("Error fetching majors for the university:", e)
        else:
            print("User is not authenticated.")
    except Exception as e:
        print("Error in context processor major_list:", e)
    return {'majors': majors}
    # return render(request, 'manage_majors/major_list.html', {'majors': majors})
