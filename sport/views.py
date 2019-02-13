from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models

@csrf_exempt
def getSports(request):
    lesson = sport.objects.create(idKey=request.POST['sport[id]'], name=request.POST['sport[name]'], photo='', Desc=request.POST['sport[desc]'])
    lesson.save()
    lessons = sport.objects.all()
    str1 = ''.join(str(e) for e in lessons)
    print(request.POST)
    return HttpResponse(str1)
