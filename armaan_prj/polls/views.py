from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    response = {"Message": "Hello World!"}
    return JsonResponse(response)







# Create your views here.
