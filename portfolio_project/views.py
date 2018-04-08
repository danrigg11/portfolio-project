from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def contactmepage(request):
    return render(request, 'ContactMe.html')

def ARboxingpage(request):
    return render(request, 'ARboxing.html')
