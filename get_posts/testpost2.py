import requests
import json
data = {"title":"testbook",
        "author":"俺",
        "genre":"哲学"}
requests.post("http://127.0.0.1:5000/newbook",data=json.dumps(data))