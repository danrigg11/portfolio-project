from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def contactmepage(request):
    return render(request, 'ContactMe.html')

def ARboxingpage(request):
    return render(request, 'ARboxing.html')

def ChildrensBookpage(request):
    return render(request, 'ChildrensBook.html')

def LostSandspage(request):
    return render(request, 'LostSands.html')

def MakingCreaturespage(request):
    return render(request, 'MakingCreatures.html')

def ProjectsWithPythonpage(request):
    return render(request, 'ProjectsWithPython.html')

def SculptingFacespage(request):
    return render(request, 'SculptingFaces.html')
