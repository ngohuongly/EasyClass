
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse

def Thanks(request):
    return HttpResponse("Thank you for your submission!")

# Create your views here.

from .models import Classes_Desc, submissionForm

def index(request):
    classes=Classes_Desc.objects.all()
    context={'classes': classes}
    return render(request,'classes/for.html', context)

def submission(request):
    if request.method == 'POST':
        form = submissionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Thanks')
    else:
        form = submissionForm()

        return render(request, 'classes/submission.html', {'form': form})
