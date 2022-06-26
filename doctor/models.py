from django.db import models

# Create your models here.


class Free_Slots(models.Model):

    doc_username=models.CharField(max_length=1000)
    time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    patient_name = models.CharField(max_length=100,default='')
    room_id = models.CharField(max_length=6,default="")
