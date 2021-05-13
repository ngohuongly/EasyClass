
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse

from .models import notif

def index(request):
    notifications=notif.objects.all()
    context={'notifications': notifications}
    return render(request,'notifications/for.html', context)


# Create your views here.
