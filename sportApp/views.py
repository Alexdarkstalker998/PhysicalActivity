from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import sport
from django.http import JsonResponse

@csrf_exempt
def getSports(request):
    # lessonns = sport.objects.all()
    # lessonns.delete()
    # #
    # lesson = sport.objects.create(idk=str("request."), name=str("request.POST['sport[name]']"), photo='', desc=str("request.POST['sport[desc]']"))
    # # # lesson = sport.objects.create(idKey=str(request.POST['sport[id]']), name=request.POST['sport[name]'], photo='', Desc=request.POST['sport[desc]'])
    # lesson.save()
    # lessons = sport.objects.all()
    # str1 = ''.join(str(e) for e in lessons)
    # # print(request.POST)
    # return HttpResponse(str1)
    req = request.POST.dict().keys()
    print(req.get)
    response = JsonResponse(req[0])
    return response
