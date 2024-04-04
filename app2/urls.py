from django.urls import path
from app2.views import *
app_name='hello'

urlpatterns=[
    path('response2/',response2,name='response2'),
]