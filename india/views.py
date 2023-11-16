from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<center><h1>Virat has Scored 50 centuries in ODI</h1></center>')

def msd(request):
    return render(request,'msd.html')
