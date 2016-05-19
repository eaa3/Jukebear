from django.shortcuts import render


from urlparse import urlparse

from .models import Song


# Create your views here.

def getYoutubeVid(url):
	parsed_url = urlparse(url)
	
	vid = parsed_url.query.split('=')[1]

	return vid


def index(request):
    songs = Song.objects.all()
    vids = map(lambda s : getYoutubeVid(s.link), songs)
    context = {'hello_message': 'Hello World!',
               'video_list': vids
    }
    return render(request, 'jukebox/index.html', context)
