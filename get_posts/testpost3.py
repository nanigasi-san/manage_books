import requests
import json
data = {"title":"やさしいC"}
requests.post("http://127.0.0.1:5000/delbook",data=json.dumps(data))