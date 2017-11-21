import json
import requests
import site_gitmyseries.settings as settings
from django.db import models
from datetime import datetime
import time

def date_formatter(e): #Helper to avoid errors later
    try:
        return datetime.strptime(e["air_date"], '%Y-%m-%d')
    except TypeError:
        return '0'

class TvShowManager(models.Manager):
    def create_tv_show_from_args(self, tmdb_id, **kwargs):
        tv_show = TvShow.objects.filter(tmdb_id=tmdb_id) #check if tv_show is already in TvShow database, based on tmdb_id
        if len(tv_show) == 0:
            tv_show = TvShow.objects.create(tmdb_id=tmdb_id, **kwargs) #create the tv_show if it's not in database
            tv_show.save() #save it - it's a sort of cache - if an user browse to a tv_show view, we store it in database
        else:
            tv_show.update(**kwargs) #update if changes are observed (especially number of season, or in_production attributes)
            tv_show = tv_show.first() #get the first element of the collection (TvShow.objects is a collection)
        return tv_show

    def create_tv_show(self, tmdb_id):
        """Method that enables us to overide the __init__method of the class TvShow"""
        url = settings.TMDB_API_URL + "tv/" + str(tmdb_id) 
        content = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())
        url_image_tv_show = url + "/images" 
        content_image_tv_show = json.loads(requests.get(url_image_tv_show, params={"api_key": settings.TMDB_API_KEY}).content.decode())
        #get the endpoint of tmdb API for the tvshow and decode it to be used

        tv_show = self.create_tv_show_from_args(
            tmdb_id=tmdb_id,
            title=content["name"],
            overview=content["overview"],
            nb_of_seasons=content["number_of_seasons"],
            is_in_production=content["in_production"],
            url_image= settings.TMDB_API_IMAGE + content_image_tv_show['posters'][0]['file_path']
        )
        #set the attributes of the TvShow object while creating the object

        # Get next episode run time (not immediately available in the API response)
        url_season = settings.TMDB_API_URL + "tv/" + str(tmdb_id)\
                                    + "/season/" + str(tv_show.nb_of_seasons)
        content_season = json.loads(requests.get(url_season, params={"api_key": settings.TMDB_API_KEY}).content.decode())
        episodes_dates = [ date_formatter(e) for e in content_season["episodes"] ]

        if episodes_dates[-1] < datetime.now():
            next_episode = '0'
        else:
            for e in episodes_dates:
                if e < datetime.now():
                    pass
                else:
                    next_episode = e.date()
                    break

        # Set next episode run time
        tv_show.next_episode_run_time = next_episode

        return tv_show

class TvShow(models.Model):
    """Definition of the class TvShow, it contains the following attributes :
           - id of the tvshow in the API Tmdb
           - title
           - overview : the description of the app_tvshow
           - nb_season : number of seasons in the app_tvshow
           - in_production : if set to True, the app_tvshow is still in production ; if set to False, it's been over"""
    tmdb_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    nb_of_seasons = models.IntegerField(default=0)
    is_in_production = models.BooleanField(default=True)
    next_episode_run_time = models.CharField(max_length=10, null=True)
    url_image=models.TextField(null=True)

    objects = TvShowManager()

    def __str__(self):
        return self.title

    # Impossible d'utiliser des Property si on veut pouvoir utiliser des QuerySet.
    # Et il faut traiter avec des QuerySet pour WishlistView notamment.

    # @property
    # def next_episode_run_time(self):
    #     url = settings.TMDB_API_URL + "tv/" + str(self.tmdb_id)
    #     content = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())
    #     date = datetime.strptime(content["last_air_date"], '%Y-%m-%d').date()
    #     if date > datetime.now().date():
    #         return date
    #     else:
    #         return "Not scheduled yet!"
    #
    # @next_episode_run_time.setter
    # def next_episode_run_time(self, value):
    #     self._next_episode_run_time = value