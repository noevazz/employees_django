from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('department/', lambda arg1:  HttpResponse("Hello, you are in the department app")),
]
