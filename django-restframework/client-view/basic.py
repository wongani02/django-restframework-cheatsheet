import requests

endpoint = "http://127.0.0.1:7000/api/products/func/create/"
get_response = requests.post(endpoint, json={'title': 'okay', 'content': 'hello world', 'price':'20.00'})
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())