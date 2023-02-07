from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer, BlogSerializer
from rest_framework import generics
from .models import Blog

# Create your views here.

# def api_home(request, *args, **kwargs):
#     body = request.body # byte string of JSON data
#     print(body)
#     print(request.GET) #url query params
#     data = {}
#     try:
#         data = json.loads(body) #string of json data --> python dict
#     except:
#         pass

#     print(data)
#     data['headers'] = dict(request.headers)
#     print(request.headers)
#     data['content_type'] = request.content_type

#     return JsonResponse({"message": "hello world"})

''' using raw django to send data'''

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()
#     data = {

#     }
#     '''
#     model instace (model_data)
#     turn it into a python dict 
#     return JSON to client
#     '''
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price

#         data = model_to_dict(model_data, fields = ['id', 'title', 'price'])

#     return JsonResponse(data)   

'''same api_home view now using django rest framework'''

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()

#     data = {

#     }
#     if model_data:
#         data = model_to_dict(model_data, fields = ['id', 'title', 'price', 'sale_price'])#using raw django we cant get the 'sale price'

#     return Response(data)

"""
using serializers to make send data
"""

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by('?').first()

#     if instance:
#         data = ProductSerializer(instance).data
#         #using raw django we cant get the 'sale price'

#     return Response(data)

'''
using serializers to ingest data
'''

@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=500)


''' blog api'''
class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    