import os, sys
import logging
import xml.etree.cElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import Config
from Config import hm_config

class utils(object):
    def __init__(self):
        self.log_levels  = hm_config.levels
        self.login_type  = hm_config.default_xml 
        self.format = "%(asctime)s %(method)s %(message)s"


    def auth_response(self,request):
        if request.REQUEST['username'] in hm_config.authenticated_user:
            username = request.REQUEST['username']
            if request.REQUEST['password'] in hm_config.authenticated_user[username]:
                return True
        return False

    def xml_build(self,request):
        try:
            login_type = request.REQUEST['Login_type'] 
            xml_name = self.login_type[login_type].keys()[0]
            xml_name = request.REQUEST[xml_name] or xml
            NotOnOrAfter = request.REQUEST['NotOnOrAfter'] or hm_config.NotOnOrAfter
            tree = ET.ElementTree(file = xml)
            root = tree.getroot()

            for items in root.iterator():
                if items.attrib == 'Recipient':
                    items.attrib.set('Recipient',request.REQUEST['Target'])
                elif items.attrib == 'SPNameQualifier':
                    items.attrib.set('SPNameQualifier',request.REQUEST['Target'])                
                elif items.attrib == 'NotOnOrAfter':
                    items.attrib.set('NotOnOrAfter',NotOnOrAfter)
                elif items.attrib == 'SessionNotOnOrAfter':
                    items.attrib.set('SessionNotOnOrAfter',NotOnOrAfter)
            
            if login_type  == 'member':
                field  = self.login_type[login_type]['member_default']
                value  = request.REQUEST[field]
            
            elif login_type == 'nurse':
                field = self.login_type[login_type]['nurse_default']
                value = request.REQUEST[field]   
          
            elif login_type == 'provider':
                field = self.login_type[login_type]['nurse_default']
                value = request.REQUEST[field]
        except Exception, e:
           raise "error in xml build"                        
         
    def debug_logger(self, method, msg):
        log = self.log_levels.get('debug')
        logging.basicConfig(level=log[0], filename=log[1]+'.log', format= self.format)
        logging.debug(method+' : '+msg)         

    def info_logger(self, msg): 
        log = self.log_levels.get('info')
        logging.basicConfig(level=log[0], filename=log[1]+'.log', format= self.format)
        logging.info(msg)
    
    def error_logger(self, method, msg):
        log = self.log_levels.get('error')
        logging.basicConfig(level=log[0], filename=log[1]+'.log', format= self.format)
        logging.error(method+' :\n '+msg)
        


