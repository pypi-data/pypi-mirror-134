import json
import requests
import urllib3
import getpass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class appliance(object):
    def __init__(self, url="", user_name="", password="", access_token="", appliance_name="", account_name="", email="", first_name="", license_key=""):
        url = input("Morpheus Appliance URL: ") if not url else url
        if url.startswith('https://'):
            url = url.replace('https://', '')

        self.url = url
        self.appliance_name = appliance_name
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email
        self.first_name = first_name
        self.access_token = access_token
        self.licence_key = license_key
    
    def applianceSetup(self):
        url = str("https://%s" % (self.url))
        setup_url = str("https://%s/api/setup/init" % (self.url))
        headers={'Content-Type': 'application/json',"Accept":"application/json"}
        body={ "applianceName": self.appliance_name, "applianceUrl": url, "accountName": self.account_name, "username": self.user_name, "password": self.password, "email": self.email, "firstName": self.first_name }
        b = json.dumps(body)
        response = requests.post(setup_url, headers=headers, data=b, verify=False)
        data = response.json()
        print(data)   
    
    def getApiToken(self):
        if not self.access_token and not self.user_name:
            self.user_name = input("Please enter user name: ")
            self.password = getpass.getpass("Please enter password: ")

        url = str("https://%s/oauth/token?grant_type=password&scope=write&client_id=morph-api" % (self.url))
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {"username": self.user_name, "password": self.password}
        try:
            response = requests.post(url, headers=headers, data=body, verify=False)
            data = response.json()
            self.access_token = data['access_token']
            self.password = ""
            return "Access token retrieved and accessible via the .access_token attribute"
        except:
            data = response.json()
            self.user_name = ""
            self.password = ""
            return data
            
    def applyLicense(self):
        url = str("https://%s/api/license" % (self.url))
        headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (self.access_token)}
        body = {"license": self.licence_key}
        b = json.dumps(body)
        response = requests.post(url, headers=headers, data=b, verify=False)
        data = response.json()
        
    def checkAppliancePing(self):
        reply = ""
        url = str("https://%s/ping" % (self.url))
        headers={'Content-Type': 'application/json',"Accept":"application/json"}
        try:
            response = requests.get(url, headers=headers, verify=False)
            reply = response.text
        except:
            pass
        return reply
    
    def checkApplianceSetupStatus(self):
        url = str("https://%s/api/ping" % (self.url))
        headers={'Content-Type': 'application/json',"Accept":"application/json"}
        response = requests.get(url, headers=headers, verify=False)
        data = response.json()
        return data["setupNeeded"]