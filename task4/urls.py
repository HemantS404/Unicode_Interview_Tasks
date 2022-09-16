from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),                        
    path('Task4_index', views.index_task4, name ='task4'),
    path('field_input', views.Feild_input, name = 'field_input'),       #If the url have task4/field_input it redirest to view names field_input 
    path('DB_check', views.DB_check, name='DB_check' ),                 #The field named name value which was enter by the user is passed through function DB_check  
    path('top_3', views.top_3, name='top_3' )                           #If the url have task4/top_3 it redirects to view top3
]