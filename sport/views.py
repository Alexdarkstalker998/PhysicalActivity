from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getSports(request):
    print(request.POST)
    return HttpResponse(request.POST['id'])
