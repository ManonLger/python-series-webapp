from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from .models import TvShow,Wishlist
from .views import tv, users

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^signup', users.signup, name='signup'),
    url(r'^$', tv.index, name='index'),
    url(r'^serie/(\d+)$', tv.view_serie, name='Serie'),
    url(r'^season/(?P<tv_show>\d+)/(?P<season_nb>\d+)', tv.view_season, name='Season'),
    url(r'^episode/(?P<tv_show>\d+)/(?P<season_nb>\d+)/(?P<episode_nb>\d+)', tv.view_episode, name='Episode'),
    url(r'^wishlist$', users.WishListView.as_view(), name="Wishlistview"),
    url(r'^search/(?P<query>((\w+).+)+)$', tv.view_search, name="ViewSearch"),
    url(r'^search/(?P<query>((\w+).+)+)/(?P<page>\d+)$', tv.view_search, name="ViewSearch")
]