from django.urls import path
from . import views


urlpatterns = [
    path('', views.appliance_list, name='appliance_list'),
    path('add/', views.add_appliance, name='add_appliance'),
    path('bill/', views.bill_calculator, name='bill_calculator'),
]