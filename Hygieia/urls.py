from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path("doctor/",include("doctor.urls")),
    path('register/',include('register_login.urls')),
    path('patient/',include('patient.urls')),
]
