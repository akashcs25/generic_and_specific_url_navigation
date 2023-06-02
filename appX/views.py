from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def csk1(request):
    return HttpResponse('csk 2023 champians')

def csk(request):
    return render(request,'csk.html')