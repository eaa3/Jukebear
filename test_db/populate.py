from jukebox.models import Song, JukeBox, JukeUser, Stats, PlaylistMembership, Playlist
from django.contrib.auth.models import User
u = User.objects.all()[0]
# JukeUser.objects.all()[0]
user = JukeUser(user=u,firstname="Sir",lastname="Dummy")
user.save()
jb = JukeBox(name="DummyJuke",owner=user,is_public=True)
playlist = Playlist()
playlist.save()
stats = Stats()
stats.save()
jb.djs.add(user)
jb.playlist = playlist
jb.stats = stats
jb.save()