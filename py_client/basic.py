import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/" #localhost

get_response = requests.post(endpoint, json={"title":"Hello world"})
print(get_response.json())
print(get_response.status_code)