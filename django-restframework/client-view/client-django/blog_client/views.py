from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    endpoint = "http://127.0.0.1:7000/api/products/list/"
    get_response = requests.get(endpoint)
    data = get_response.json()
    print(data)
    
    context = {
        'data': data,
    }
    return render(request, 'blog_client/home.html', context)
