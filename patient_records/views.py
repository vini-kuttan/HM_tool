# Create your views here.

from django.http import HttpResponse
from models import Patient_inquiry
from django.core import serializers

import json


def record_inquiry(request):
    obj = Patient_inquiry()
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

def search_data(request):
    search = Patient_inquiry()
    import pdb;pdb.set_trace()
    fname = request.REQUEST['search_fname']
    lname = request.REQUEST['search_lname']
    room_type = request.REQUEST['search_room_type']
    patient_type = request.REQUEST['search_patient_type']
    try:
        data = search.objects.filter(firstname = fname, 
                                      lastname = lname, 
                                      room_type = room_type, 
                                      patient_type = patient_type)
        formated_data = serializers.serialize("json", data)
        result  = json.loads(formated_data)
        return result

    except:
       return HttpResponse("No data with requested details")
     

  
