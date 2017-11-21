from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_gitmyseries.models.tv_show import TvShow, TvShowManager
import requests, json
import site_gitmyseries.settings as settings
from app_gitmyseries.forms import SearchForm
from django.views.generic import ListView


class IndexView(ListView):
    """This class is based on ListView special feature in Django"""
    model = TvShow #This view is based on the model TvShow
    template_name = 'app_gitmyseries/index.html' #The template linked to this ListView

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) #Call the method of the parent
        context["search_form"] = SearchForm() #add the form object to the context
        return context

    def get_queryset(self):
        """Method that displays special tv_shows within the homepage, based on the feature Discover in the Tmdb API"""
        params = {
            "sort_by": "popularity.desc",
            "api_key": settings.TMDB_API_KEY
        }
        r = requests.get(settings.TMDB_API_URL+"discover/tv", params=params).content.decode()
        #get the endpoint of tmdb API for the discover feature and decode it to be used
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
        search_form = SearchForm(request.POST) #get the form filled by the user
        # check whether it's valid:
        if search_form.is_valid():
            query = search_form.cleaned_data['search'] #get the query from the user
            return HttpResponseRedirect(reverse("search_url",args=[query])) #redirect to the search_url template
