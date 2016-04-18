from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'hello_message': 'Hello World!'}
    return render(request, 'jukebox/index.html', context)
