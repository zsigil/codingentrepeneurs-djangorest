import requests


endpoint = "http://127.0.0.1:8000/api/products/" 

data = {
    "title": "This field is title",
    "price": 12.99
}

get_response = requests.post(endpoint, data=data)
print(get_response.json())
print(get_response.status_code)