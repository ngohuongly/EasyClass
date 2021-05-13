
def Thanks(request):
    return HttpResponse("Thank you for your cooperation! ")

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse

from .models import studentsinformation,studentsForm

def index(request):
    students=studentsinformation.objects.all()
    context={'students': students}
    return render(request,'students/for.html', context)

def get_info(request):
    if request.method == 'POST':
        form = studentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Thanks')
    else:
        form = studentsForm()

        return render(request, 'students/name.html', {'form': form})
