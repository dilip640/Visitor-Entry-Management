from django.contrib import admin
from django.urls import path, include
from entryapp.views import home, host, checkout

urlpatterns=[
    path('', home,name='home'),
    path('host/', host,name='host'),
    path('checkout/', checkout,name='checkout'),
]