from django.shortcuts import render
from django.http import HttpResponse
import operator

def drinks(requests):
    return HttpResponse('<h1>Drinking 3l water everyday will keep us hydrated!</h1>')

def foods(requests):
    return HttpResponse('eat healthy food')

# Create your views here.
