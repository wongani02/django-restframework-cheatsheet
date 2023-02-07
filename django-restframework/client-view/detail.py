import requests

endpoint = "http://127.0.0.1:7000/api/products/list-create/"
get_response = requests.get(endpoint)
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())