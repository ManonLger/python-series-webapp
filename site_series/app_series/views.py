from django.shortcuts import render
from django.http import HttpResponse
from .models import TvShow
import requests
import json

base_url = "https://api.themoviedb.org/3/"

def index(request):
    params = {
        "sort_by": "popularity.desc",
        "api_key": "XXX"
    }
    r = requests.get(base_url+"discover/tv", params=params).content.decode()
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
