from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('this is our first view function')
  
def propose(request):
    return HttpResponse('I LOVE YOU WILL YOPU MARRY ME')

def rejection(request):
    return HttpResponse('I HATE u')