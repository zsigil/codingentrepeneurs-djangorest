import requests


endpoint = "http://127.0.0.1:8000/api/products/1/update/" 

data = {
    "title": "double Updated title",
    "price": 100
}

get_response = requests.put(endpoint,data=data)
print(get_response.json())
print(get_response.status_code)