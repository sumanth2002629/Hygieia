from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/doctor', views.signup_doctor, name='signup-doctor'),
    path('signup/patient', views.signup_patient, name='signup-patient'),
    path('login/', auth_views.LoginView.as_view(template_name='register_login/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='register_login/logout.html'), name="logout"),
    path('profile/', views.profile, name='profile')
]
