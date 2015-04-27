from django.db import models

# Create your models here.


class Patient_inquiry(models.Model): 
    patient_id = models.AutoField(primary_key=True, max_length = 6) 
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    ssn = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=30)
    birthdate = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    patient_type =  models.CharField(max_length=30)
    room_no = models.CharField(max_length=30)
    room_type = models.CharField(max_length=30)
    Insurance = models.CharField(max_length=30)
  
    def __unicode__(self):
       return self.firstname





    
