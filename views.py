from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    all_albums = Album.objects.all()

    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album,
    }
    return render(request, 'music/detail.html', context)
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album,
    }
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        print("________________________________")
        print(selected_song)
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,
                                                     'error_message': "you did not enter valid song"})
    else:
        print(selected_song)
        selected_song.is_favorite = True
        selected_song.save()
    return render(request, 'music/detail.html', context)