from django.urls import path
from . import views

# Define app name to set application_namespace
app_name = 'shows'

#Mapping views to urls
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:venue_id>/', views.venue, name='venue'),
    path('<int:venue_id>/venue_results/', views.venue_results, name='venue_results'),
    path('<int:venue_id>/show/', views.show, name='show'),
    path('<int:venue_id>/', views.detail, name='detail'),
]
