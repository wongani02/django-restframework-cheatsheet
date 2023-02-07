import requests

endpoint = "http://127.0.0.1:7000/api/products/1/update/"
data = {
    'title': 'same same',
    'price': 12.99,
}

get_response = requests.put(endpoint, json=data)
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())