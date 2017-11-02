from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_series.models import TvShow, Season, Episode
import requests
import json
import site_series.settings as settings
from app_series.forms.search import SearchForm

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

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            query = form.cleaned_data['search']
            return HttpResponseRedirect(reverse("ViewSearch",args=[query]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {
        "list": list,
        "form": form
    }
    return render(request, 'app_series/index.html', context)

@login_required(login_url='login')
def view_serie(request,id):
    serie = TvShow()
    serie.set_series_attributes(id)
    liste_saison = range(1, serie.nb_season+1)
    next_episode = serie.get_next_episode_run_time()
    if request.method == "POST":
        user = request.user
        if len(TvShow.objects.filter(tmdb_id=id)) == 0:
            serie = TvShow()
            serie.set_series_attributes(id)
            serie.save()
            user.wishlist.wishes.add(serie)
        if len(user.wishlist.wishes.filter(tmdb_id=id)) == 0:
            user.wishlist.wishes.add(serie)
        return HttpResponseRedirect(reverse("Serie", args=[id]))
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

def view_search(request, query, page=1):
    params = {
        "query": query,
        "api_key": settings.TMDB_API_KEY,
        "language": "en-US"
    }
    r = requests.get(settings.TMDB_API_URL + "search/tv", params=params).content.decode()
    result_list = json.loads(r)["results"]

    paginator = Paginator(result_list, 5)  # 10 liens par page
    page = request.GET.get('page')
    try:
        # La définition de nos URL autorise comme argument « page » uniquement
        # des entiers, nous n'avons pas à nous soucier de PageNotAnInteger
        result = paginator.page(page)
    except EmptyPage:
        # Nous vérifions toutefois que nous ne dépassons pas la limite de page
        # Par convention, nous renvoyons la dernière page dans ce cas
        result = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result = paginator.page(1)
    return render(request, 'app_series/search.html', locals())

def view_my_list(request, id):
    serie = TvShow()
    serie.set_series_attributes(id)
    if serie.save() is True:
        liste_saison = range(1, serie.nb_season)
        return render(request, 'app_series/serie.html', locals())
    else:
        serie.add_to_db()
        liste_saison = range(1, serie.nb_season)
        return render(request, 'app_series/serie.html', locals())
    serie.add_to_db()

    """serie_form= SerieForm()
    if request.method == 'POST':
        form = SerieForm(request.POST)
        form.save()
    return render(request, 'app_series/serie.html')"""

