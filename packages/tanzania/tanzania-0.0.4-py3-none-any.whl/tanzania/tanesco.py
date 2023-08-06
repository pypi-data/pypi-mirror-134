import requests
import json

host = 'http://app.gepg.go.tz:8006/api/customer-info'

def load_owner(meternumber):
    header = {
            'Host' : 'app.gepg.go.tz:8006',
            'Content-Type' : 'application/json', 
            'Accept' : 'application/json',
            'Connection' : 'keep-alive'
        }
    info = requests.post(
        host, headers=header,
        data=json.dumps(
            {
                "meterNumber" : meternumber
                }
            )
        )
    if info.status_code == 200:
        return info.json()
    else:
        return json.dumps({"error":"Connection Error"})
