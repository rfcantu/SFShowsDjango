from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.views import generic

from .models import Venue, Show
from .forms import CustomUserCreationForm
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

def login(request):
    if request.user.is_authenticated:
        return render(request, 'shows/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('shows/index.html')

# Creating a view for new users to register
def register(request):
    if request.user.is_authenticated:
        return redirect('/shows')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            user_login(request, user)
            return redirect('/shows')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})