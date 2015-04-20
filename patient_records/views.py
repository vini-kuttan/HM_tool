# Create your views here.

from django.http import HttpResponse
from models import Patient_inquiry

def record_inquiry(request):
    obj = Patient_inquiry()
    import pdb;pdb.set_trace() 
    obj.firstname = request.REQUEST['firstname'] 
    obj.lastname = request.REQUEST['lastname']
    obj.ssn = request.REQUEST['ssn']
    obj.phone = request.REQUEST['phone']
    obj.street = request.REQUEST['street'] 
    obj.city = request.REQUEST['city'] 
    obj.country = request.REQUEST['country'] 
    obj.gender = request.REQUEST['gender'] 
    obj.marital_status = request.REQUEST['marital_status']
    obj.birthdate = request.REQUEST['date']+'/'+request.REQUEST['month']+'/'+request.REQUEST['year'] 
    obj.nationality = request.REQUEST['nationality'] 
    obj.patient_type = request.REQUEST['patient_type']  
    obj.room_no = request.REQUEST['room_no'] 
    obj.room_type = request.REQUEST['room_type'] 
    obj.Insurance = request.REQUEST['Insurance']
    obj.save()
    return HttpResponse("successfully loaded")

  
