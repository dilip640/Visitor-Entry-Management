from django.contrib import admin
from django.urls import path, include
from entryapp.views import home

urlpatterns=[
    path('', home,name='home'),
]