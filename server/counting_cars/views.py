from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
import json
import requests

def carsApi(request):
    return JsonResponse('Aloha!', safe=False)

def carsUpload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        json_content = json.load(file)
        number_of_cars = count_cars(json_content)
        return JsonResponse(number_of_cars, safe=False)
    return HttpResponse(status=404)

def count_cars(json_content):
    CAR_CATEGORY_ID = 3
    car_annotations = list(filter(lambda c: c['category_id'] == CAR_CATEGORY_ID, json_content['annotations']))

    # TODO: Count only cars located in the center area of the images
    center_images_count = len(car_annotations)
    return center_images_count
