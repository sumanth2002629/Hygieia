from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doctor-home'),
    path('free_slots/',views.add_slots,name="add_slots"),
    path('view_slots/',views.view_slots,name="view_slots"),

]
