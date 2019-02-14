from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sportApp.models import sport

@csrf_exempt
def dbview(request):
    studs = user
    lessons = sport.objects.all()
    str1 = ''.join(str(e) for e in lessons)
    # print(request.POST)
    return HttpResponse(str1)

def login(request):
    return render(request,"login.html")
