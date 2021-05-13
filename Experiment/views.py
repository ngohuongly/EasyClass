from django.shortcuts import render
from django.http import HttpResponse

def Welcome(request):
    return HttpResponse("I want to add some fun experiments that our children can easily do at home. Just be creative and enjoy!"   )

from .models import Experiments

def index(request):
    experiments=Experiments.objects.all()
    context={'experiments': experiments}
    return render(request,'experiment/for.html', context)
