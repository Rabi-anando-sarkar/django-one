from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    print("Home Page Requested")
    return HttpResponse("<h1>This is Home Page</h1>")