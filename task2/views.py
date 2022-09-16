from django.shortcuts import render
from django.http import HttpResponse
from task1 import b_dict                                #from task1 importing function b_dict(a,b)

def index_task2(request, a, b):                         #providing int a and b from dynamic url, a and b are the parameter of the function
    d = b_dict(a, b)                                    #values of a and b being passed to the function b_dict
    dict = '{'
    for i in range(a,b):                                #creating a string called dict represting dictonary key-value pair seperated by commas
        if i>a:
            dict += ", " + str(i) + ": " +str(d[i])
        else:
            dict += str(i) + ": " +str(d[i])
    dict += '}'
    print(d)                                            #printing the dictonary on the terminal
    return HttpResponse(dict)                           #printing the string dict on a page using HttpResponse