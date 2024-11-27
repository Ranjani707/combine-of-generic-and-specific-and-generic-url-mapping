from django.urls import path
from pythonn.views import *

urlpatterns=[
    path('trainer1/',trainer1,name='trainer1'),
    path('trainer2/',trainer2,name='trainer2'),

]