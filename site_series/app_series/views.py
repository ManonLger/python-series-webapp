from django.shortcuts import render
from django.http import HttpResponse
from .models import TvShow
import requests
import json
import site_series.settings as settings

def index(request):
    params = {
        "sort_by": "popularity.desc",
        "api_key": settings.TMDB_API_KEY
    }
    r = requests.get(settings.TMDB_API_URL+"discover/tv", params=params).content.decode()
    r = json.loads(r)["results"]
    list = []
    for tvs in r:
        list += [TvShow(title = tvs["name"])]

    context = {
        "list": list
    }
    return render(request, 'app_series/index.html', context)

def view_serie(request,id):
    serie = TvShow()
    serie.set_series_attributes(id)
    liste_saison = range(serie.nb_season)
    return render(request, 'app_series/serie.html',locals())

def view_season(request, tv_show, season_nb):
    objet = Season()
    objet.set_attributes(tv_show, season_nb)
    liste_episodes = range(objet.nb_episodes)
    return render(request, 'app_series/view_season.html', locals())