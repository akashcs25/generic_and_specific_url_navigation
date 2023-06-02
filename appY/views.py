from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def rcb1(request):
    return HttpResponse('royal challengers banglore')

def rcb(request):
    return render(request,'rcb.html')