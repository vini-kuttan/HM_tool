#! Author = Vineesh Kumar

#import modules
import os, sys
import Utils

from django.http import HttpResponse
from django.template import loader, Context
from Utils.hm_util import utils 

base_path = os.path.join(os.path.dirname(__file__)).replace('\\','/')
template_path =  os.path.join(os.path.dirname(__file__), 'Templates').replace('\\','/')


class exception(object):
    def __init__(self):
        pass
   
    def error(self, msg):
        t = loader.get_template(template_path+'/error.html')
        c = Context({error_msg:msg})
        return HttpResponse(t.render(c)) 


class Controller(utils, exception):

    def __init__(self):
        pass

    def index(self, request):
        if 'authenticated' in request.session and request.session['authenticated'] == True:
            t = loader.get_template(template_path+'/index.html')
            c = Context({})
            return HttpResponse(t.render(c))
        else:
            return self.login_form(request)

    def login_form(self,request):
       t = loader.get_template(template_path+'/login_form.html')
       c = Context({})
       return HttpResponse(t.render(c))

    def search_criteria(self,request):
       t = loader.get_template(template_path+'/search_index.html')
       c = Context({})
       return HttpResponse(t.render(c))

    def authentication(self,request):

       try:
           valid = self.auth_response(request)
           if valid:
               request.session['authenticated'] = True
               return self.index(request)
           else:
               return self.login_form(request)
       except Exception,e:
           msg = "No Login Found"
           print authentication.__name__
           self.error_logger(authentication.__name__, str(e))
           return self.error(msg)

    def _form_saml(self,request = ''):
        try:
            if request:
                saml = self.xml_build(request)
                t = loader.get_template(template_path+'/reconfirm.html')
                c = Context({SAML:saml})
                return HttpResponse(t.render(c)) 
            else:
                msg = 'Request is not communicated to Controller '
                raise ValueError(msg)
        except Exception,e:
            if not (locals().has_key('msg')):
                msg = "Given input has trouble in building saml"
            self.error_logger(upload_xml.__name__, str(e))
            return self.error(msg)             

    def upload_saml(self, request):
        t = loader.get_template(template_path+'/upload_saml.html')
        c = Context({})
        return HttpResponse(t.render(c))

    def upload_xml(self, request):
        try:
            xml_filename = str(request.GET['xmlname'])
            xml = str(request.GET['xml'])
            with open(base_path+'/SAML/'+xml_filename+'.xml','w') as xml_file:
                xml_file.write(xml)
            return HttpResponse ('xml has been uploaded succesfully')
        except Exception,e:
            msg = 'xml is not uploaded successfully, please check with the website administrator'
            self.error_logger(upload_xml.__name__, str(e))
            return self.error(msg)

    def modify_saml(self, request):
        t = loader.get_template(template_path+'/modify_saml.html')
        c = Context({})
        return HttpResponse(t.render(c))

    def modify_xml(self, request):
        try:
            xml_filename = str(request.GET['xmlname'])
            xml_file = open(base_path+'/SAML/'+xml_filename+'.xml','r')
            content = xml_file.readlines()
            t = loader.get_template(template_path+'/modify_saml.html')
            c = Context({xmlname:xml_filename,xml:content})
            return HttpResponse(t.render(c))
        except:
            msg = 'There is no such xml file, please give proper xml name or check with the website administrator'
            self.error_logger(modify_xml.__name__, str(e))
            return self.error(msg)


