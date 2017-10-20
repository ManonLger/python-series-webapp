from django.conf.urls import url
from django.views.generic import ListView


from . import views
from .models import TvShow

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^serie/(\d+)$', views.view_serie, name='Serie'),
    url(r'^season/(?P<tv_show>\d+)/(?P<season_nb>\d+)',views.view_season, name='Season'),
    url(r'^episode/(?P<tv_show>\d+)/(?P<season_nb>\d+)/(?P<episode_nb>\d+)',views.view_episode, name='Episode'),
    url(r'^wishlist$', views.WishList.as_view(), name="Wishlist"),

]