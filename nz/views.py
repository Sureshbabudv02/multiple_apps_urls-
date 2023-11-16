from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def williamson(request):
    return HttpResponse('<h1>Williamson scores 50 in semis</h1>')

def philips(request):
    return render(request,'philips.html')