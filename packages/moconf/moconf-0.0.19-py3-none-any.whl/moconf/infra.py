import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### GROUPS ###
def newGroup(url: str, bearer_token: str, name: str, code: str = "", location: str = ""):
    type = "group"
    url = str("%s/api/%ss" % (url,type)) if url.startswith("https://") else str("https://%s/api/%ss" % (url, type))
    bearer_token = str(bearer_token)
    name = str(name)
    code = str(code)
    location = str(location)
    
    headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (bearer_token)}
    body = {type:{"name": name,"code": code,"location": location}}
    b = json.dumps(body)
    post = requests.post(url, headers=headers, data=b, verify=False)
    data = post.json()
    return data[type]

def getGroups(url: str, bearer_token: str, name: str, id: int = ""):
    type = "group"
    url = str("%s/api/%ss" % (url,type)) if url.startswith("https://") else str("https://%s/api/%ss" % (url, type))
    bearer_token = str(bearer_token)