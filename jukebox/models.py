from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    up = models.IntegerField()
    down = models.IntegerField()

    
class Song(models.Model):
    link = models.URLField(primary_key=True)
    stats = models.OneToOneField(Stats)

    def __unicode__(self):
        return self.link

class JukeUser(models.Model):
    
    user = models.OneToOneField(User)

    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)

    def __unicode__(self):
        return "%s %s"%(self.firstname,self.lastname)

class JukeBox(models.Model):
    name = models.CharField(max_length=100,blank=False)
    owner = models.ForeignKey(JukeUser,related_name='jukeboxes')
    is_public = models.BooleanField(blank=False)
    djs = models.ManyToManyField(JukeUser,related_name='subscribed_jukeboxes') 
    songs = models.ManyToManyField(Song, blank=True)

    stats = models.OneToOneField(Stats)

    def __unicode__(self):
        return "%d"%(self.id)

