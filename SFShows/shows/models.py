from django.db import models
from django.forms import ModelForm
# Create your models here.
'''
Models containing data about our database
    - each class variable in a model is a database field in the model
'''
# Venue:
#     venue_text - venue name
#     pub_date - last day listing was updated
class Venue(models.Model):
    venue_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.venue_text

# Show:
#     venue - the venue this show is attached to
#     info_text - information about the show
class Show(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    info_text = models.CharField(max_length=300)
    venue_id = Venue.objects.get(id=3) 
    artist = models.CharField(max_length=30)
    date = models.CharField(max_length=80)
    def __str__(self):
        return self.info_text

class Attending(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    attendee = models.CharField(max_length=30)

    def __str__(self):
        return self.attendee