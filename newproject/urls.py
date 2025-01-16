
from django.urls import path
from . import views

app_name='Study'

urlpatterns = [
   
    path('', views.home,name='home'),
    path('Notes/', views.project1,name='notes'),
    path('Stopwatch/', views.Stopwatch,name='stopwatch'),
]