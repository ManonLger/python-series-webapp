from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow, TvShowManager
import requests, json
import site_series.settings as settings
from app_series.forms import SearchForm
from django.views.generic import ListView


class IndexView(ListView):
    model = TvShow
    template_name = 'app_series/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["search_form"] = SearchForm()
        return context

    def get_queryset(self):
        params = {
            "sort_by": "popularity.desc",
            "api_key": settings.TMDB_API_KEY
        }
        r = requests.get(settings.TMDB_API_URL+"discover/tv", params=params).content.decode()
        content = json.loads(r)["results"]
        ids_list = [tv_show['id'] for tv_show in content]

        for tv_show in content:
            TvShow.objects.create_tv_show_from_args(
                tmdb_id=tv_show['id'],
                title=tv_show['name'],
                overview=tv_show['overview'],
            )
        return TvShow.objects.filter(tmdb_id__in=ids_list)

    def post(self, request):
        # create a form instance and populate it with data from the request:
        search_form = SearchForm(request.POST)
        # check whether it's valid:
        if search_form.is_valid():
            query = search_form.cleaned_data['search']
            return HttpResponseRedirect(reverse("search_url",args=[query]))

#
# def index(request):
#     params = {
#         "sort_by": "popularity.desc",
#         "api_key": settings.TMDB_API_KEY
#     }
#     r = requests.get(settings.TMDB_API_URL+"discover/tv", params=params).content.decode()
#     r = json.loads(r)["results"]
#     list = []
#     for tvs in r:
#         list += [TvShow(title = tvs["name"], tmdb_id = tvs["id"])]
#
#     # Search Form
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         search_form = SearchForm(request.POST)
#         # check whether it's valid:
#         if search_form.is_valid():
#             query = search_form.cleaned_data['search']
#             return HttpResponseRedirect(reverse("search_url",args=[query]))
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         search_form = SearchForm()
#
#     return render(request, 'app_series/index.html', locals())
