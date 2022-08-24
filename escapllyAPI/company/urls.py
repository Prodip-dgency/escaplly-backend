from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompanyHome, name='Home')
]
