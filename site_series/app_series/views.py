from django.shortcuts import render
from django.http import HttpResponse
from .models import TvShow
import requests
import json
import site_series.settings as settings

base_url = "https://api.themoviedb.org/3/"

def index(request):
    params = {
        "sort_by": "popularity.desc",
        "api_key": settings.TMDB_API_KEY
    }
    r = requests.get(base_url+"discover/tv", params=params).content.decode()
    r = json.loads(r)["results"]
    list = []
    for tvs in r:
        list += [TvShow(title = tvs["name"], id = tvs[])]

    context = {
        "list": list
    }
    return render(request, 'app_series/index.html', context)