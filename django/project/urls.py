from django.contrib import admin
from django.urls import path, include
from login.detail_view.login_view import login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('login/', include('login.urls')),
    path('home/', include('home.urls')),
    path('manage_university/', include('manage_university.urls')),
    path('student/', include('manage_student.urls')),
    path('workshop/', include('manage_workshop.urls')),
    path('matching/', include('manage_matching.urls')),
    path('major/', include('manage_majors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
