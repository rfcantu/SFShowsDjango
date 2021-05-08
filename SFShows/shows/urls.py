from django.urls import path
from . import views

#Mapping views to urls
urlpatterns = [
    path('', views.index, name='index'),
]
