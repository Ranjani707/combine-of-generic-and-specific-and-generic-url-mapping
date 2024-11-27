from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def trainer1(request):
    return HttpResponse('<h1>harshad sir is teaching python course</h1>')
def trainer2(request):
    return HttpResponse('<h1>pranay sir is teaching python course</h1>')
