from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:a>/<int:b>/', views.index_task2, name='task2'),          #dynamic url -> change in a url resulting different output
]                                                                       #< type : variable>