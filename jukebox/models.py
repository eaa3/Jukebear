from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

    
class Song(models.Model):
    link = models.URLField(primary_key=True)

    def __unicode__(self):
        return self.link

class Playlist(models.Model):
    songs = models.ManyToManyField('Song', through='PlaylistMembership')

class PlaylistMembership(models.Model):
    playlist = models.ForeignKey(Playlist)
    song = models.ForeignKey(Song)
    date_added = models.DateField(auto_now=True)

    stats = models.OneToOneField(Stats)

    class Meta:
        ordering = ['date_added']


class JukeUser(models.Model):
    
    user = models.OneToOneField(User)

    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)

    def __unicode__(self):
        return "%s %s"%(self.firstname,self.lastname)

class JukeBox(models.Model):
    name = models.CharField(max_length=100,blank=False,default="New Jukebox")
    owner = models.ForeignKey(JukeUser,related_name='jukeboxes')
    is_public = models.BooleanField(blank=False)
    djs = models.ManyToManyField(JukeUser,related_name='subscribed_jukeboxes') 
    playlist = models.ForeignKey(Playlist,blank=True,related_name='playlist')

    stats = models.OneToOneField(Stats)

    def __unicode__(self):
        return "%d"%(self.id)

