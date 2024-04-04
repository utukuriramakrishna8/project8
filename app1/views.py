from django.shortcuts import render
from django.http import HttpResponse

def response1(request):
    return HttpResponse('How are you')

# Create your views here.
