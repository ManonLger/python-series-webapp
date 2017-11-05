from django.conf.urls import url, include
from .views.signup import signup
from .views.tv_show import tv_show
from .views.index import index
from .views.season import season
from .views.episode import episode
from .views.search import search
from .views.wishlist import WishListView#, remove_from_wishlist#, add_to_wishlist

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^signup', signup, name='signup'),
    url(r'^$', index, name='index'),
    url(r'^tv_show/(\d+)$', tv_show, name='tv_show_url'),
    url(r'^season/(?P<tmdb_id>\d+)/(?P<season_nb>\d+)', season, name='season_url'),
    url(r'^episode/(?P<tmdb_id>\d+)/(?P<season_nb>\d+)/(?P<episode_nb>\d+)', episode, name='episode_url'),
    url(r'^wishlist$', WishListView.as_view(), name='wishlist_url'),
    url(r'^wishlist/(?P<tmdb_id>\d+)', WishListView.as_view(), name='wishlist_url'),
    url(r'^search/(?P<query>((\w+).+)+)$', search, name='search_url'),
    url(r'^search/(?P<query>((\w+).+)+)/(?P<page>\d+)$', search, name='search_url'),
]