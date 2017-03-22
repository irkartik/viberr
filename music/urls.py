from django.conf.urls import url, include
from . import views

app_name= 'music'

urlpatterns = [
	#/music/
    url(r'^$', views.index, name='index'),

    #/music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), 

    #/music/71/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
