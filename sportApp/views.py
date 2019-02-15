from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import lesson, user, type1, type2, place, lesson, messages, sport
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
    if loguser['login']=="admin" and loguser['password'] == 'admin':
        return {'aut':'admin'}
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
    except Exception as e:
        print(e)
        return JsonResponse({'aut':'error'})
    try:
        us.type2
    except Exception as e:
        return JsonResponse({'aut':'coach'})
    return JsonResponse({'aut':"user"})

@csrf_exempt
def schedule(request):
    logjson = get_from_request(request)
    print(logjson)
    loguser = logjson.get("user")
    try:
        print("0")
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        type = us.type2
        print("1")
        courses = list(lesson.objects.filter(stud = type))
        an = list()
        print("2")
        for el in courses:
            dic = dict()
            dic.update({'sport':model_to_dict(el.sport)['name']})
            co = model_to_dict(el.coach)
            co.update(model_to_dict(el.coach.user))
            co.pop('user')
            dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
            dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place)})
            an.append(dic)
        print(an)
        return JsonResponse({'sch':an})
    except Exception as e:
        print(e)
        return JsonResponse({'schedule':'error'})


def test(request):
    p1, created = user.objects.get_or_create(tabnum = "111111", password = '1488', name = "Alex", surname = 'Nefedov')
    p3, created = user.objects.get_or_create(tabnum = "333333", password = '3222', name = "Alesx", surname = 'Refedov')
    t3, created = type2.objects.get_or_create(email = "asdfg@mail.ru", group = 'k3215', goal = "0", user = p3)
    t1, created = type2.objects.get_or_create(email = "asd@mail.ru", group = 'k3215', goal = "0", user = p1)
    s, created = sport.objects.get_or_create(name = 'Борьба',desc='Это борьба, там борятся.')
    p,created= place.objects.get_or_create(name = "Ломо")
    p2, created = user.objects.get_or_create(tabnum = "222222", password = '1337', name = "Anton", surname = 'Evteev')
    t2, created = type1.objects.get_or_create(contacts = '911838284', desc = 'Хороший учитель', user = p2)
    l, created = lesson.objects.get_or_create(sport = s, coach = t2, lvl="1",wday="Пtонедельник",tday="11:40",place =p, countmax = '50',countnow='49')
    l.stud.add(t1)
    l.stud.add(t3)
    us = user.objects.get(tabnum = '111111',password='1488')
    type = us.type2
    # l2 = lesson.objects.create(sport = s, coach = t2, lvl="1",wday="Понедельник",tday="11:40",place =p, countmax = '50',countnow='49')
    # l2.stud.add(t1)


    courses = list(lesson.objects.filter(stud = type))
    an = list()
    for el in courses:
        dic = dict()
        dic.update({'sport':model_to_dict(el.sport)['name']})
        co = model_to_dict(el.coach)
        co.update(model_to_dict(el.coach.user))
        co.pop('user')
        dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
        dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place)})
        an.append(dic)

    response = {'aut':an}
    print(response)
    return JsonResponse(model_to_dict(p1))
