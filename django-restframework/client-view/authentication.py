import requests

password = input('enter password: ')
auth_endpoint = "http://127.0.0.1:7000/api/auth/"
auth_response = requests.post(auth_endpoint, json={'username': 'pablo', 'password': password})

print(auth_response.status_code)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpoint = "http://127.0.0.1:7000/api/products/list-create/"
    get_response = requests.get(endpoint, headers=headers)

    # print(get_response.status_code)
    print(get_response.json())