from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def trainer1(request):
    return HttpResponse('<h1>joshna mam is teaching python course</h1>')
def trainer2(request):
    return HttpResponse('<h1>ankitha mam is teaching python course</h1>')