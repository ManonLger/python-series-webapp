from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^serie/(\d+)$', views.view_serie, name='view_serie'),
    url(r'^season/(?P<tv_show.tmdb_id>\d+)/(?P<season_nb>\d+)',views.view_season, name='Season')

]