from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import Venue
# Create your views here.

# Creating a view for 404 response error
def detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venus_id)
    return render(request, 'shows/detail.html', {'venue': venue})

# Creating a view for venues
def venue(request, venue_id):
    return HttpResponse("Looking at the venue %s" % venue_id)

# Creating a view for venue responses
def venue_results(request, venue_id):
    response = "Looking at results for venur %s"
    return HttpResponse(response % venue_id)

# Creating a view for a show
def show(request, venue_id):
    return HttpResponse(
        "Looking at a show at venue %s" % venue_id
    )

# Creating a view called index
def index(request):
    latest_venue_list = Venue.objects.order_by('-pub_date')[:5]
    context = {
        'latest_venue_list': latest_venue_list,
    }
    return render(request, 'shows/index.html', context)