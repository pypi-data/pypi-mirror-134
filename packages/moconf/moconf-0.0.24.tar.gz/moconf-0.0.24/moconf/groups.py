import json
import requests
import urllib3

from moconf.appliance import morpheusAppliance

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### GROUPS ###
class infraGroup(morpheusAppliance):
    def __init__(self, name=None, id=None) -> None:
        self.name = name
        self.id = id
        
    def new(self, location=None, code=None):
        type = "group"
        url = str("https://%s/api/%ss" % (self.url, type))
        body = {type:{"name": name,"code": code,"location": location}}
        b = json.dumps(body)
        post = requests.post(url, headers=headers, data=b, verify=False)
        data = post.json()
        return data[type]
        
        
        
# def newGroup(url: str, access_token: str, name: str, code: str = "", location: str = ""):
#     type = "group"
#     url = str("%s/api/%ss" % (url,type)) if url.startswith("https://") else str("https://%s/api/%ss" % (url, type))
#     # access_token = str(access_token)
#     # name = str(name)
#     # code = str(code)
#     # location = str(location)
    
#     headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (access_token)}
#     body = {type:{"name": name,"code": code,"location": location}}
#     b = json.dumps(body)
#     post = requests.post(url, headers=headers, data=b, verify=False)
#     data = post.json()
#     return data[type]

# def getGroups(url: str, access_token: str, name: str, id: int = ""):
#     type = "group"
#     url = str("%s/api/%ss" % (url,type)) if url.startswith("https://") else str("https://%s/api/%ss" % (url, type))
#     access_token = str(access_token)