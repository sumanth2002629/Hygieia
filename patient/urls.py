from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='patient-home'),
    path('book_appoinment/',views.book_appoinment,name="book_appoinment"),
    # path('view_slots/',views.view_slots,name="view_slots"),

]
