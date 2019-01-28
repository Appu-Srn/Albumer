from music.views import *
from django.urls import path
from django.conf.urls import url

app_name = 'music'


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    #music/712
    url(r'^register/$', UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # /music/album/add
    url(r'album/add/$', AlbumCreate.as_view(), name='album_add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', AlbumUpdate.as_view(), name='album_update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', AlbumDelete.as_view(), name='album_delete'),
]