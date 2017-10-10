import json
import requests
import site_series.settings as settings

from django.db import models

class TvShow(models.Model):
        """Definition of the class TvShow, it contains the following attributes :
               - id of the tvshow in the API Tmdb
               - name
               - overview : the description of the app_tvshow
               - nb_season : number of seasons in the app_tvshow
               - in_production : if set to True, the app_tvshow is still in production ; if set to False, it's been over"""
        tmdb_id= models.IntegerField(default=0)
        title = models.CharField(max_length=100)
        overview = models.TextField(null=True)
        nb_season = models.IntegerField(default=0)
        in_production = models.BooleanField(default=True)

        def __str__(self):
            return self.title

        def set_series_attributes(self,id):
            """Method that sets the attributes title, overview, nb_seasons,in_production"""
            api_key = settings.TMDB_API_KEY
            url = settings.TMDB_API_URL + str(id)
            url_content = json.loads(requests.get(url, params={"api_key": api_key}).content.decode())
            self.tmdb_id = id
            self.title = url_content["name"]
            self.overview = url_content["overview"]
            self.nb_season = url_content["number_of_seasons"]
            self.in_production = url_content["in_production"]

class Season(models.Model):
    """Definition of the class TvShowSeason, it contains the following attributes:
            - id of the TvShow
            - season_nb: season number
            - id of the season
            - name : season name
            - overview : the description of the season
            - broadcast_date : the release date of the season
            - a list of episodes within the season
            """

    tv_id = models.IntegerField()
    season_nb = models.IntegerField()
    season_id = models.IntegerField()
    name = models.CharField()
    overview = models.CharField()
    broadcast_date = models.DateTimeField(verbose_name="Release Date")

    def __str__(self):
        return self.tv_id
    def __str__(self):
        return self.season_nb

    def find_name(self):




class Episode(models.Model):
    num = models.IntegerField()

import requests
import json

class TvShowSeason:

        def __init__(self, tv_id=int, season_nb=int):
            url = "https://api.themoviedb.org/3/tv/" + str(self.tv_id) + "season/" + str(self.season_nb)
            url_content = json.loads(requests.get(url, params={"api_key": "3b8efb3a7bff18de4e8641510c6352a5"}).content.decode())
            self.tv_id = tv_id
            self.season_nb = season_nb
            self.id_season = url_content["id"]
            self.name = url_content["name"]
            self.overview = url_content["overview"]
            self.season_nb = url_content["season_number"]
            self.broadcast_date = url_content["air_date"]

            """Definition of the function returning a list of the episodes within the season"""
            def get_episodes_list(self):
                list_episodes=[]
                episodes= url_content["episodes"]
                for elt in episodes:
                    episode_nb =  episodes["episodes_number"]
                    episode_name = episodes["name"]
                    episode_overview = episodes["overview"]
                    l.append(episode_nb, episode_name, episode_overview)
                return list_episodes