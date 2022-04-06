from unicodedata import name
from django.urls import path
from . import views 

# Create your views here.
urlpatterns = [
   	path('device-register/', views.deviceRegister, name="device-register"),
    path('searchDev/', views.SearchDevice, name="searchDev"),
    path('', views.index, name='dashboard-index'),
]
