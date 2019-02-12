from django.shortcuts import render
from django.http import HttpResponse
import requests

def getSports(request):
    return HttpResponse(request.POST)
