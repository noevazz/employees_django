from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('person/', lambda arg1:  HttpResponse("You are in the person app")),
]
