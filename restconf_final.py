import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept" : "application/yang-data+json", 
    "Content-type" : "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface" : {
            "name" : "Loopback65070721", 
            "description" : "create loopback", 
            "type": "iana-if-type:softwareLoopback",
            "enabled" : True, 
            "ietf-ip:ipv4" : {
                "address" : [
                    {
                        "ip" : "172.30.127.1", 
                        "netmask" : "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6" : {}
        }
    }

    resp = requests.put(
        api_url+"/data/ietf-interfaces:interfaces/interface=Loopback65070721",  
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070721 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url+"/data/ietf-interfaces:interfaces/interface=Loopback65070721",  
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070721 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070721",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        }
    }


    resp = requests.patch(
        api_url+"/data/ietf-interfaces:interfaces/interface=Loopback65070721", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070721 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))



def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070721",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        }
    }

    resp = requests.patch(
        api_url+"/data/ietf-interfaces:interfaces/interface=Loopback65070721", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070721 is disabled"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070721"


    resp = requests.get(
        api_url_status,
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback65070721 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback65070721 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 65070721"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
