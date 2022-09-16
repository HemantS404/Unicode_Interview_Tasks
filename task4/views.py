from django.shortcuts import render
import requests
from django.http import HttpResponse
from task4 import models
from task4.models import WheatherReport

#As this is a modification of the task3, some viwes will be explained in task3 views.py
def search(request):                                                                
    return render(request = request, template_name = 'task4/input_task4.html')

def index_task4(request):
    city = request.GET['city']
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}
    headers = {
	"X-RapidAPI-Key": "a5e5a759aemshc162066ebc55c0dp18b555jsn6dc327404420",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    respond = requests.request("GET", url, headers=headers, params=querystring)
    if(respond.ok):
        respond = respond.json()
        i = WheatherReport(                                             #variable i is storing the data in a form of a django-model class name WheatherReport
            name = respond['location']['name'],
            region = respond['location']['region'],
            country = respond['location']['country'],
            tz_id = respond['location']['tz_id'],                   
            localtime = respond['location']['localtime'],
            lat = respond['location']['lat'],
            lon = respond['location']['lon'],
            last_updated = respond['current']['last_updated'],
            temp_c = respond['current']['temp_c'],
            humidity = respond['current']['humidity'],
            feelslike_c = respond['current']['feelslike_c'],
            wind_dir = respond['current']['wind_dir']
        )
        i.save()                                                        #.save() stores the data in database 
        return HttpResponse('<h1>Data Stored Sucessfully</h1>')
    else:
        return HttpResponse('<h1>Some error has occured</h1>')
    
def Feild_input(request):                                               #if user typed Field_input in url it will ask a city name from user
    return render(request, 'task4/field_input.html')                    #render the field_input.html file which ask for a city name

def DB_check(request):                                                  #request parameter contains a data of name city
    city = request.GET['city']
    city = city.capitalize()
    Data = WheatherReport.objects.filter(name = city)                   #.object.filter check the feild value in the database (it return a list of entities having same field value in form of a QuerySet whereas .object.get returns only one entity)
    for d  in Data:
        d.countfield += 1                                               #update count field by 1
        d.save()
    return render(request, 'task4/DB_check.html',{ "d" : Data.values()})     #rendering DB_check.html file, passing a dictonary have the entities 

def top_3(request):                                                         #this function render the top 3 most quered city in the database 
    Data = WheatherReport.objects.order_by('-countfield')[0:3]              #order_by used to order the data ,(-) denote desending order and [:] denotes slicing of the tuple
    return render(request, 'task4/top_3.html',{ "d" : Data})                #rendering DB_check.html file, passing a dictonary have the entities