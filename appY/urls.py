from django.urls import path
from appY.views import *
app_name='appY'

urlpatterns=[
    path('rcb/',rcb,name='rcb'),
    path('rcb1',rcb1,name='rcb1'),
]