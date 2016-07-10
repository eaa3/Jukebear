from django.shortcuts import render

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from .models import Song, JukeBox, Stats, PlaylistMembership

from django.views.decorators.csrf import csrf_exempt

import json

from django.http import JsonResponse


# Create your views here.

def getYoutubeVid(url):
    parsed_url = urlparse(url)
    vid = None
    try:
        vid = parsed_url.query.split('=')[1]
    except:
        vid = parsed_url.geturl().split('/')[-1]

    return vid


def index(request,**kwargs):

    # TODO add checks to avoid crashes
    context = {}

    jukebox_id = kwargs['jukebox_id']
    if jukebox_id:
        jukebox = JukeBox.objects.filter(id=jukebox_id)[0]
        songs = jukebox.playlist.songs.all()
        vids = map(lambda s : getYoutubeVid(s.link), songs)
        context = {'hello_message': 'Hello World!',
                   'video_list': vids,
                   'jukebox_id': jukebox_id,
        }

    else:
        print("No jukebox")
        # jukebox = JukeBox()
        # songs = jukebox.songs.all()
        # vids = map(lambda s : getYoutubeVid(s.link), songs)
        # context = {'hello_message': 'Hello World!',
        #            'video_list': vids,
        #            'jukebox_id': jukebox_id,
        # }
    
    return render(request, 'jukebox/index.html', context)

@csrf_exempt
def update_playlist(request):

    try:
        received_data = json.loads(request.body)
    except TypeError:
        received_data = json.loads(request.body.decode('utf-8'))   #support for python 3


    jukebox_id = int(received_data["id"])
    link = received_data["link"]


    jukebox = JukeBox.objects.filter(id=jukebox_id)[0]

    song = None
    try:
        song = Song.objects.get(link=link)
    except:
        song = Song(link=link)
        song.save()

    stat = Stats()
    stat.save()
    playlist_membership = PlaylistMembership(playlist=jukebox.playlist, song=song, stats = stat)
    playlist_membership.save()

    # jukebox.playlist.songs.add(song)


    songs = jukebox.playlist.songs.all()

    vids = map(lambda s : getYoutubeVid(s.link), songs)

    return JsonResponse({'playlist': vids})

@csrf_exempt
def update_stats(request):

    try:
        received_data = json.loads(request.body)
    except TypeError:
        received_data = json.loads(request.body.decode('utf-8'))   #support for python 3

    print("Got this data", received_data["stat"]," from instance ",received_data["id"])

    return JsonResponse({'SomeData':'Data!!'})

def get_playlist(request,**kwargs):

    jukebox_id = kwargs['jukebox_id']

    json_out = {'playlist': []}

    if jukebox_id:
        jukebox = JukeBox.objects.filter(id=jukebox_id)[0]
        songs = jukebox.playlist.songs.all()
        vids = map(lambda s : getYoutubeVid(s.link), songs)
        json_out['playlist'] = vids



    return JsonResponse(json_out)


