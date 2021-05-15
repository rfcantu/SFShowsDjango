from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Venue, Show
# Create your views here.

# List view displays a list of objects
class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'latest_venue_list'

    def get_queryset(self):
        return Venue.objects.order_by('-pub_date') [:5]

# Detail view displays a detail page for a particular type of object
class DetailView(generic.DetailView):
    model = Venue
    template = 'shows/detail.html'

class VenueDetailView(generic.DetailView):
    model = Venue
    show_list = Venue.objects.all()
    template = 'shows/venue_detail.html'

class ResultsView(generic.DetailView):
    model = Venue
    template_name = 'shows/results.html'

# Creating a view for venue responses
def venue_results(request, venue_id):
    response = "Looking at results for venur %s"
    return HttpResponse(response % venue_id)

# Creating a view for a show
def show(request, venue_id):
    return HttpResponse(
        "Looking at a show at venue %s" % venue_id
    )