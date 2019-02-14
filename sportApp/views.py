from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import lesson, user, type1, type2, place, lesson, messages
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
        user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        return JsonResponse({'aut':"accept"})
    except Exception as e:
        print(e)
        return JsonResponse({'aut':'error'})

def schedule(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        type = us.type2 
        courses = type.lesson.all()
        return JsonResponse({'aut':"accept"})
    except Exception as e:
        print(e)
        return JsonResponse({'aut':'error'})
    return HttpResponse('a')


def test(request):
    p1, created = user.objects.get_or_create(tabnum = "111111", password = '1488', name = "Alex", surname = 'Nefedov')
    t1, created = type2.objects.get_or_create(email = "asd@mail.ru", group = 'k3215', goal = "0", user = p1)
    s, created = sport.objects.get_or_create(name = 'Борьба',desc='Это борьба, там борятся.')
    p,created= place.objects.get_or_create(name = "Ломо")
    p2, created = user.objects.get_or_create(tabnum = "222222", password = '1337', name = "Anton", surname = 'Evteev')
    t2, created = type1.objects.get_or_create(contacts = '911838284', desc = 'Хороший учитель', user = p2)
    lesson, created = lesson.objects.get_or_create(sport = s, coach = t2, lvl="1",wday="Понедельник",tday="11:40",place =p, countmax = '50',countnow='49')
    lesson.stud__set.add(t1)
    print(model_to_dict(p1))
    return JsonResponse(model_to_dict(p1))
