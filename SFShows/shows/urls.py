from django.urls import path
from django.conf.urls import include
from . import views

# Define app name to set application_namespace
app_name = 'shows'

#Mapping views to urls
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.VenueDetailView.as_view(), name='venue_detail'),
    path('<int:pk>/venue_results/', views.ResultsView.as_view(), name='venue_results'),
    path('<int:venue_id>/show/', views.show, name='show'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]
