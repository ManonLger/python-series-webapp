from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from .models import TvShow,Wishlist
from .views import tv, user

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^signup', user.signup, name='signup'),
    url(r'^$', tv.index, name='index'),
    url(r'^tvshow/(\d+)$', tv.tvshow, name='tvshow_url'),
    url(r'^season/(?P<tv_show>\d+)/(?P<season_nb>\d+)', tv.season, name='season_url'),
    url(r'^episode/(?P<tv_show>\d+)/(?P<season_nb>\d+)/(?P<episode_nb>\d+)', tv.episode, name='episode_url'),
    url(r'^wishlist$', user.WishListView.as_view(), name='wishlist_url'),
    url(r'^search/(?P<query>((\w+).+)+)$', tv.search, name='search_url'),
    url(r'^search/(?P<query>((\w+).+)+)/(?P<page>\d+)$', tv.search, name='search_url'),
    url(r'^season_saved/(\d+)', user.wishlist, name='save'),
    url(r'^season/delete/(\d+)', user.delete, name='delete')
]