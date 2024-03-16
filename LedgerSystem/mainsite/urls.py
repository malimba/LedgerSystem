from django.urls import path, include
from .views import *
app_name = 'mainsite'

urlpatterns = [
    path('', Home, name='Home')
]