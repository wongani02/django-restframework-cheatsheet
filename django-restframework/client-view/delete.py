import requests

product_id = input('what product id would you like to delete')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(product_id +'is not valid')

if product_id:
    endpoint = f"http://127.0.0.1:7000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code)
    # print(get_response.json())
