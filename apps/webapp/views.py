from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic


# Create your views here.
def index(request):
    return render(request,'webapp/index.html')

def AiHC(request):
    return render(request,'webapp/aiInHealthCare.html')

def DbR(request):
    return render(request,'webapp/DR.html')

def diagnosis(request):
    return render(request,'webapp//diagnosis.html')

def deeplearning(request):
    return render(request,'webapp//DeepLearning.html')

def Signs(request):
    return render(request,'webapp/signsymptoms.html')
