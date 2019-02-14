from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import sport


def login(request):
    return render(request,"login.html")


@csrf_exempt
def dbview(request):
    studs = user
    lessons = sport.objects.all()
    str1 = ''.join(str(e) for e in lessons)
    # print(request.POST)
    return HttpResponse(str1)

def dbsports(request):
    return HttpResponse('a')

def dbstudents(request):
    return HttpResponse('a')

def dbcoachs(request):
    return HttpResponse('a')

def dbplaces(request):
    return HttpResponse('a')

def dblessons(request):
    return HttpResponse('a')

def dbmessages(request):
    return HttpResponse('a')

def lessonedit(request):
    return HttpResponse('a')

def lessonmark(request):
    return HttpResponse('a')

def lessonmessages(request):
    return HttpResponse('a')
