from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return render(requests,'wcount/home.html',{'name':'Deepthi'})
def aboutus(requests):
    return render(requests,'wcount/about.html',{'name':'Deepthi'})
# Create your views here.
def hobbies(requests):
    return HttpResponse('<h1>My hobbies</h1>')
