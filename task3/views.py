from cgitb import html
from urllib import response
from django.shortcuts import render
import requests                                                               #importing request module of python
from django.http import HttpResponse

def search(request):                                                          #this view render input.html file having a custom form
    return render(request = request, template_name = 'task3/input.html')      #which ask user for a city name
#after pressing submit button it redirect to url.py to search for view named task3(done by Django {% url %} template tag)

def index_task3(request):                                                     #the request parameter has variable called city which was input by the user 
    city = request.GET['city']                                                #accesing the city name from parameter request
    url = "https://weatherapi-com.p.rapidapi.com/current.json"                
    querystring = {"q": city}
    headers = {
	"X-RapidAPI-Key": "KEY",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    respond = requests.request("GET", url, headers=headers, params=querystring)         #requesting the data from the server through a wheather-API
    if(respond.ok):                                                                     #response.ok returns True if status_code is less than 400
        respond = respond.json()                                                        #coverting QuerySet to JSON format
        return render(request = request, template_name = 'task3/Task3_index.html', context=respond)     #rendring Task3_index.html and passing the respond dictonary
    else:
        return HttpResponse('<h1>Some error has occured</h1>')
    
