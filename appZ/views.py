from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mumbai1(request):
    return HttpResponse('mumbai indians')

def mumbai(request):
    return render(request,'mumbai.html')