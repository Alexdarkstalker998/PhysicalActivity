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
        return JsonResponse({'aut':'admin'})
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
    except Exception as e:
        print(e)
        return JsonResponse({'aut':'error'})
    try:
        us.type2
    except Exception as e:
        return JsonResponse({'aut':['coach', {'name':us.name,'surname':us.surname}]})
    return JsonResponse({'aut':["user", {'name':us.name,'surname':us.surname}]})

@csrf_exempt
def schedule(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        type = us.type2
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
        return JsonResponse({'sch':an})
    except Exception as e:
        print(e)
        return JsonResponse({'schedule':'error'})

@csrf_exempt
def coschedule(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        type = us.type1
        courses = list(lesson.objects.filter(coach = type))
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
        return JsonResponse({'sch':an})
    except Exception as e:
        print(e)
        return JsonResponse({'schedule':'error'})

@csrf_exempt
def colesson(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    loglesson = logjson.get('lesson')
    el = lesson.objects.get(id = int(loglesson['id']))
    dic = dict()
    dic.update({'sport':model_to_dict(el.sport)['name']})
    co = model_to_dict(el.coach)
    co.update(model_to_dict(el.coach.user))
    co.pop('user')
    dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
    dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place),'countmax':el.countmax,'countnow':el.countnow})
    slst =list()
    for student in list(el.stud.all()):
        studdic= dict()
        studdic.update({'group':student.group,'id':student.user.id,'tabnum':student.user.tabnum,'name':student.user.name,'surname':student.user.surname})
        slst.append(studdic)
    dic.update({"stud":slst})
    return JsonResponse({"clsn":dic})

@csrf_exempt
def copoints(request):

    return a


@csrf_exempt
def getlesson(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
    except Exception as e:
        print(e)
        return JsonResponse({'gtlsn':'user_error'})
    courses = list(lesson.objects.all())
    an = list()
    for el in courses:
        dic = dict()
        dic.update({'sport':model_to_dict(el.sport)['name']})
        co = model_to_dict(el.coach)
        co.update(model_to_dict(el.coach.user))
        co.pop('user')
        dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
        dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place),'countmax':el.countmax,'countnow':el.countnow})
        co = el.stud.all()
        if len(co)!=0:
            for u in co:
                if u.user.id == us.id:
                    dic.update({'member':True})
                    break
                else: dic.update({'member':False})
        else: dic.update({'member':False})
        an.append(dic)
    return JsonResponse({'gtlsn':an})

@csrf_exempt
def dolesson(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    try:
        us = user.objects.get(tabnum = loguser['login'],password=loguser['password'])
        t = us.type2
    except Exception as e:
        print(e)
        return JsonResponse({'dlsn':'user_error'})
    loglesson = logjson.get('lesson')
    print(loglesson)
    if loglesson['do'] == "join":
        try:
            print("check")
            if len(list(lesson.objects.filter(stud = t)))>=3:
                return JsonResponse({'dlsn':'maxlessons'})
            l = lesson.objects.get(id = int(loglesson['id']))
            l.stud.add(t)
            l.countnow = str(int(l.countnow) - 1)
            l.save()
        except Exception as e:
            print(e)
            return JsonResponse({'dlsn':'join_error'})

        return JsonResponse({'dlsn':'success'})
    elif loglesson['do']== 'del':
        print('good')
        try:
            l = lesson.objects.get(id = int(loglesson['id']))
            l.stud.remove(t)
            l.countnow = str(int(l.countnow) + 1)
            l.save()
        except Exception as e:
            print(e)
            return JsonResponse({'dlsn':'del_error'})
        return JsonResponse({'dlsn':'del_success'})
    else: return JsonResponse({'dlsn':'key_error'})

def test(request):
    p1, created = user.objects.get_or_create(tabnum = "111111", password = '1488', name = "Alex", surname = 'Nefedov')
    p3, created = user.objects.get_or_create(tabnum = "333333", password = '3222', name = "Alesx", surname = 'Refedov')
    t3, created = type2.objects.get_or_create(email = "asdfg@mail.ru", group = 'k3215', goal = "0", user = p3)
    t1, created = type2.objects.get_or_create(email = "asd@mail.ru", group = 'k3215', goal = "0", user = p1)
    s, created = sport.objects.get_or_create(name = 'Борьба',desc='Это борьба, там борятся.')
    s1, created = sport.objects.get_or_create(name = 'Флорбол',desc='Это флорбол, там игрют в флорбол.')
    s2, created = sport.objects.get_or_create(name = 'Бокс',desc='Это бокс, там дерутся.')
    s3, created = sport.objects.get_or_create(name = 'Гребля',desc='Это гребля, там гребут.')
    p,created= place.objects.get_or_create(name = "ул. Ломоносова, д. 9")
    p1p,created= place.objects.get_or_create(name = "Вяземский переулок, д. 5/7")
    p2p,created= place.objects.get_or_create(name = "Альпийский переулок, д. 15, к. 2, лит. А")
    p3p,created= place.objects.get_or_create(name = "Другие спортивные объекты")
    p2, created = user.objects.get_or_create(tabnum = "222222", password = '1337', name = "Anton", surname = 'Evteev')
    t2, created = type1.objects.get_or_create(contacts = '911838284', desc = 'Хороший учитель', user = p2)
    # l1, created = lesson.objects.get_or_create(sport = s1, coach = t2, lvl="2",wday="Вторник",tday="11:40",place =p1p, countmax = '50',countnow='50')
    # l2, created = lesson.objects.get_or_create(sport = s2, coach = t2, lvl="3",wday="Среда",tday="13:30",place =p2p, countmax = '50',countnow='50')
    # l3, created = lesson.objects.get_or_create(sport = s3, coach = t2, lvl="3",wday="Четверг",tday="08:20",place =p3p, countmax = '25',countnow='25')
    # l4, created = lesson.objects.get_or_create(sport = s2, coach = t2, lvl="2",wday="Пятница",tday="15:00",place =p1p, countmax = '30',countnow='30')
    # l5, created = lesson.objects.get_or_create(sport = s, coach = t2, lvl="1",wday="Суббота",tday="16:50",place =p2p, countmax = '40',countnow='40')
    # l6, created = lesson.objects.update_or_create(countnow = "0", defaults = {'countmax':'25', 'countnow':'17'} )

    us = user.objects.get(tabnum = '111111',password='1488')
    type = us.type2
    # l2 = lesson.objects.create(sport = s, coach = t2, lvl="1",wday="Понедельник",tday="11:40",place =p, countmax = '50',countnow='49')
    # l2.stud.add(t1)

    # !! Уроки студента
    # courses = list(lesson.objects.filter(stud = type))
    # an = list()
    # for el in courses:
    #     dic = dict()
    #     dic.update({'sport':model_to_dict(el.sport)['name']})
    #     co = model_to_dict(el.coach)
    #     co.update(model_to_dict(el.coach.user))
    #     co.pop('user')
    #     dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
    #     dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place)})
    #     an.append(dic)
    # response = {'aut':an}
    #
    # # !!Уроки преподователя
    # type = p2.type1
    # courses = list(lesson.objects.filter(coach = type))
    # an = list()
    # for el in courses:
    #     dic = dict()
    #     dic.update({'sport':model_to_dict(el.sport)['name']})
    #     co = model_to_dict(el.coach)
    #     co.update(model_to_dict(el.coach.user))
    #     co.pop('user')
    #     dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
    #     dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place)})
    #     an.append(dic)
    # response = {'aut':an}
    #
    # # !!Урок преподователя
    # el = l1
    # dic = dict()
    # dic.update({'sport':model_to_dict(el.sport)['name']})
    # co = model_to_dict(el.coach)
    # co.update(model_to_dict(el.coach.user))
    # co.pop('user')
    # dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
    # dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place),'countmax':el.countmax,'countnow':el.countnow})
    # slst =list()
    # for student in list(el.stud.all()):
    #     studdic= dict()
    #     studdic.update({'group':student.group,'id':student.user.id,'tabnum':student.user.tabnum,'name':student.user.name,'surname':student.user.surname})
    #     slst.append(studdic)
    # dic.update({"stud":slst})
    #
    # # !!Выставление баллов
    #
    #
    # # !!Все уроки
    # courses = list(lesson.objects.all())
    # for el in courses:
    #     dic = dict()
    #     dic.update({'sport':model_to_dict(el.sport)['name']})
    #     co = model_to_dict(el.coach)
    #     co.update(model_to_dict(el.coach.user))
    #     co.pop('user')
    #     dic.update({'coach':{'name':co["name"],'surname':co["surname"],'id':co['id']}})
    #     dic.update({'lvl':el.lvl,'wday':el.wday,"id":el.id,'tday':el.tday,"place":model_to_dict(el.place),'countmax':el.countmax,'countnow':el.countnow})
    #     co = el.stud.all()
    #     if len(co)!=0:
    #         for u in co:
    #             if u.user.id == us.id:
    #                 dic.update({'member':True})
    #                 break
    #             else: dic.update({'member':False})
    #     else: dic.update({'member':False})
    #     an.append(dic)

    return JsonResponse(model_to_dict(p1))

def testtest(request):
    return JsonResponse({})

@csrf_exempt
def admin(request):
    logjson = get_from_request(request)
    loguser = logjson.get("user")
    if loguser['login']!="admin" and loguser['password'] != 'admin':
        return JsonResponse({'admin':'user_error'})
    lognewuser = logjson.get("newuser")
    try:
        a = user.objects.get(tabnum=lognewuser['tabnum'])
        return JsonResponse({'admin':'create_err'})
    except Exception as e:
        pass
    p1, created = user.objects.get_or_create(tabnum = lognewuser['tabnum'], password = lognewuser['password'], name = lognewuser['name'], surname = lognewuser['surname'])
    t1, created = type2.objects.get_or_create(email = lognewuser['email'], group = lognewuser['group'], goal = "0", user = p1)
    return JsonResponse({'admin':'created'})
