from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.search, name='search'),                       #default redirect to search views
    path('Task3_index', views.index_task3, name='task3'),       #pass to index_task3 view
]