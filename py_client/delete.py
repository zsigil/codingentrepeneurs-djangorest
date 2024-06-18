import requests


endpoint = "http://127.0.0.1:8000/api/products/12/delete/" 

get_response = requests.delete(endpoint)
# print(get_response.json())
print(get_response.status_code)