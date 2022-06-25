from django.db import models

# Create your models here.


class Free_Slots(models.Model):

    doc_username=models.CharField(max_length=1000)
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    patient_name = models.CharField(max_length=100,default='')
