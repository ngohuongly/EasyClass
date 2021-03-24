from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("This page contains main classes and extracurricular classes. Students can find all details of the class and the zoom links for meeting here.")

# Create your views here.
