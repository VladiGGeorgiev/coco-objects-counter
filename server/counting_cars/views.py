from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
import json
import requests

from .objects_counter import CarsObjectsCounter

def carsApi(request):
    return JsonResponse('Aloha!', safe=False)

def carsUpload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        json_content = json.load(file)
        
        objects_counter = CarsObjectsCounter()
        number_of_cars = objects_counter.count_cars(json_content)

        return JsonResponse(number_of_cars, safe=False)
    return HttpResponse(status=404)