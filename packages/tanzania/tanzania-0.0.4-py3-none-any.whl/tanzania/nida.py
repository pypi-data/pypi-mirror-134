import requests
import json
def load_citizen(nin):
    user_link = "https://ors.brela.go.tz/um/load/load_nida/{}".format(nin)
    link_headers = {
        "Content-Type":"application/json",
    }
    info = requests.post(
        url = user_link,
        headers= link_headers
        )
    if info.status_code == 200:
        return info.json()
    else:
        return json.dumps({"error":"Connection Error"})