from django.http import HttpResponse

def Welcome(request):
    return HttpResponse("Welcome to EASYCLASS. You can find here all information about the students, contact emails and numbers. "   )

from django.shortcuts import render

from .models import studentsinformation

def index(request):
    students=studentsinformation.objects.all()
    context={'students': students}
    return render(request,'students/for.html', context)
