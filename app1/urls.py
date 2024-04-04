from django.urls import path
from app1.views import *
app_name='hi'

urlpatterns=[
    path('response1/',response1,name='response1'),
]