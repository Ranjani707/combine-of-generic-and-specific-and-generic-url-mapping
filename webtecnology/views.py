from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kishore(request):
    return HttpResponse('<h1>kishore sir is teaching javascript course</h1>')
def dhuruv(request):
    return HttpResponse('<h1>dhuruv sir is teaching html and css course</h1>')

