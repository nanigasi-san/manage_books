import json
import requests
data = {"lending": False,
        "title": "プリンキピア"}
URL="http://127.0.0.1:5000/rental"
res = requests.post(URL,data=json.dumps(data))
print(res.json())