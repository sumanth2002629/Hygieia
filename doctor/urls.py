from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doctor-home'),
    path('doc_free_slots/',views.add_slots,name="add_slots"),

]
