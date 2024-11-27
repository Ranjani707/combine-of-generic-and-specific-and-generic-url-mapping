from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ravi(request):
    return HttpResponse('<h1>ravi sir is teaching java course</h1>')
def vicky(request):
    return HttpResponse('<h1>vicky sir is teaching java course</h1>')


