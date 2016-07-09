from django.shortcuts import render

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from .models import Song
from .models import JukeBox

from django.views.decorators.csrf import csrf_exempt

import json

from django.http import JsonResponse


# Create your views here.

def getYoutubeVid(url):
	parsed_url = urlparse(url)
	
	vid = parsed_url.query.split('=')[1]

	return vid


def index(request,jukebox_id):

    # TODO add checks to avoid crashes
    print("Thats a parameter", jukebox_id)
    jukebox = JukeBox.objects.filter(id=jukebox_id)[0]
    songs = jukebox.songs.all()


    vids = map(lambda s : getYoutubeVid(s.link), songs)
    context = {'hello_message': 'Hello World!',
               'video_list': vids,
               'jukebox_id': jukebox_id,
    }
    return render(request, 'jukebox/index.html', context)

@csrf_exempt
def update_playlist(request):

    try:
        received_data = json.loads(request.body)
    except TypeError:
        received_data = json.loads(request.body.decode('utf-8'))   #support for python 3

    print("oh yes dude! ", received_data["link"])

    return JsonResponse({'SomeData':'Data!!'})

@csrf_exempt
def update_stats(request):

    try:
        received_data = json.loads(request.body)
    except TypeError:
        received_data = json.loads(request.body.decode('utf-8'))   #support for python 3

    print("Got this data", received_data["stat"]," from instance ",received_data["id"])

    return JsonResponse({'SomeData':'Data!!'})


