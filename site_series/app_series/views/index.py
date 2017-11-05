from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow
import requests, json
import site_series.settings as settings
from app_series.forms import SearchForm

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

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            query = form.cleaned_data['search']
            return HttpResponseRedirect(reverse("search_url",args=[query]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {
        "list": list,
        "form": form
    }
    return render(request, 'app_series/index.html', context)
