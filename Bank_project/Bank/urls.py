from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ifsc/', views.get_name, name='get_name'),
    path('branch/', views.branch_name, name='branch_name'),

]
