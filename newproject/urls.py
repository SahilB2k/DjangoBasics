
from django.urls import path
from . import views

app_name='Study'

urlpatterns = [
   
    path('', views.home,name='home'),
    path('project1/', views.project1),
]