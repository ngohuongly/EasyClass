from django.views.generic import TemplateView
from django.shortcuts import render

#class Home(TemplateView):
#    template_name = 'home.html'

def Home(request):
    return render(request, 'EasyClass/home.html')
