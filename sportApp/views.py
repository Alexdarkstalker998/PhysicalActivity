from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import lesson, user
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict


def get_from_request(request):
    return json.loads(list(request.POST.dict().keys())[0])

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
    slov = json.loads(list(request.POST.dict().keys())[0])
    print(slov)
    response = JsonResponse(slov)
    return response
    
@csrf_exempt
def login(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        user.objects.get(name = loguser['name'],password=loguser['password'])
        return JsonResponse({'aut':"accept"})
    except Exception as e:
        print(e)
        return JsonResponse({'aut':'error'})




def test(request):
    p1, created = user.objects.get_or_create(tabnum = "111111", password = '1488', name = "Alex", surname = 'Nefedov')
    print(model_to_dict(p1))
    return JsonResponse(model_to_dict(p1))
