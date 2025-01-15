from django.shortcuts import render
from .models import deployedProjects
# Create your views here.
def home(request):
    images=deployedProjects.objects.all()
    return render(request,'app1.html',{'images':images});