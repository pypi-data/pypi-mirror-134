import json
from urllib import response
import requests
import urllib3

from moconf.appliance import appliance

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class infra(appliance):
    def __init__(self,appliance):
        self.url = appliance.url
        self.access_token = appliance.access_token
        
    def getGroups(self, name: str=None, id: int = None):
        type = "group"
        headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (self.access_token)}
        endpoint = str("%s/api/%ss" % (self.url,type)) if self.url.startswith("https://") else str("https://%s/api/%ss" % (self.url, type))
        if name:
            url = str("%s?%s" % (endpoint,name))
        elif id:
            url = str("%s/%s" % (endpoint,id))
        else:
            url = endpoint
        
        try:
            response = requests.get(url, headers=headers, verify=False)
            data = response.json()
            return data
        except:
            data = response.json()
            return data

        # def newGroup(url: str, access_token: str, name: str, code: str = "", location: str = ""):
        #     type = "group"
        #     url = str("%s/api/%ss" % (url,type)) if url.startswith("https://") else str("https://%s/api/%ss" % (url, type))
            
        #     headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (access_token)}
        #     body = {type:{"name": name,"code": code,"location": location}}
        #     b = json.dumps(body)
        #     try:
        #         response = requests.post(url, headers=headers, data=b, verify=False)
        #         data = response.json()
        #         return data[type]
        #     except:
        #         data = response.json()
        #         return data
