from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def project1(request):
    return render(request,'notes.html')

def Stopwatch(request):
    return render(request,'watch.html')