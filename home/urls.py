from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home),
    path('/base',views.base,name=  'base'),
    path('/keyboard',views.keyboard,name='keyboard'),

]

