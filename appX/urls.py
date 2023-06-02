from django.urls import path
from appX.views import *
app_name='appX'

urlpatterns=[
    path('csk/',csk,name='csk'),
    path('csk1',csk1,name='csk1')
]