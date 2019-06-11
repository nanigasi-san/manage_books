import requests
print(requests.get("http://127.0.0.1:5000/books_data").json())