from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app_series.models import TvShow, Season, Episode
import requests
import json
import site_series.settings as settings

@login_required(login_url='login')
def index(request):
    params = {
        "sort_by": "popularity.desc",
        "api_key": settings.TMDB_API_KEY
    }
    r = requests.get(settings.TMDB_API_URL+"discover/tv", params=params).content.decode()
    r = json.loads(r)["results"]
    list = []
    for tvs in r:
        list += [TvShow(title = tvs["name"], tmdb_id = tvs["id"])]

    context = {
        "list": list
    }
    return render(request, 'app_series/index.html', context)

@login_required(login_url='login')
def view_serie(request,id):
    serie = TvShow()
    serie.set_series_attributes(id)
    liste_saison = range(1, serie.nb_season+1)
    next_episode = serie.get_next_episode_run_time()
    return render(request, 'app_series/serie.html',locals())

@login_required(login_url='login')
def view_season(request, tv_show, season_nb):
    serie = TvShow(tmdb_id=tv_show)
    objet = Season(tv_show=serie)
    serie.set_series_attributes(tv_show)
    objet.set_attributes(tv_show, season_nb)
    liste_episodes = range(1, objet.nb_episodes+1)
    return render(request, 'app_series/season.html', locals())

@login_required(login_url='login')
def view_episode(request, tv_show, season_nb, episode_nb):
    serie = TvShow(tmdb_id=tv_show)
    season = Season(tv_show= serie, season_nb=season_nb)
    objet = Episode(tv_season=season)
    serie.set_series_attributes(tv_show)
    season.set_attributes(tv_show, season_nb)
    objet.set_attributes(tv_show, season_nb, episode_nb)
    return render(request, 'app_series/episode.html', locals())
