from django.shortcuts import render


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
               'video_list': vids
    }
    return render(request, 'jukebox/index.html', context)

@csrf_exempt
def update_playlist(request):

    received_data = json.loads(request.body)

    print("oh yes dude! ", received_data["link"])



    return JsonResponse({'SomeData':'Data!!'})


