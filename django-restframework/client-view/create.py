import requests

endpoint = "http://127.0.0.1:7000/api/products/"
get_response = requests.post(endpoint, json={'title': 'okay create', 'content': 'okay good'})
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())