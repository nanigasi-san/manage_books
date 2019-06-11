import json
import requests
data = {"now": True,
        "title": "Fate/Zero[5]"}
URL="http://127.0.0.1:5000/rental"
res = requests.post(URL,data=json.dumps(data))
print(res.json())