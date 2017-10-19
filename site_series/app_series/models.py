import json
import requests
import site_series.settings as settings
from django.db import models
from django import utils

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
            url = settings.TMDB_API_URL + "tv/" + str(id)
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
            - a list of episodes within the season"""
        tv_show = models.ForeignKey('TvShow',default=0)
        season_nb = models.IntegerField(default=0)
        tmdb_id = models.IntegerField(default=0)
        title = models.CharField(max_length=100, null=True)
        overview = models.CharField(max_length=1000, null=True)
        broadcast_date = models.DateTimeField(auto_now_add=True, auto_now=False)
        nb_episodes = models.IntegerField(default=0)

        def set_attributes(self, id, season_nb):
            url = "https://api.themoviedb.org/3/tv/" + str(id) + "/season/" + str(season_nb)
            url_cont = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())
            self.season_nb = season_nb
            self.title = url_cont["name"]
            self.overview = url_cont["overview"]
            self.broadcast_date = url_cont["air_date"]
            self.nb_episodes = len(url_cont["episodes"])



class Episode(models.Model):
    """Definition of the class Episode, it contains the following attributes:
                    - id of the TvShow
                    - episode_nb: episode number
                    - id of the episode
                    - name : episode name
                    - overview : the description of the episode
                    - broadcast_date : the release date of the episode
                    - an average score for the episode"""
    tv_show = models.ForeignKey('TvShow', default=0)
    tv_season = models.ForeignKey('Season', default=0)
    episode_nb = models.IntegerField(default=0)
    tmdb_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100, null=True)
    overview = models.CharField(max_length=1000, null=True)
    broadcast_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    vote_average = models.IntegerField(default=0)

    def set_attributes(self, id, season_nb, episode_nb):
        url = "https://api.themoviedb.org/3/tv/" + str(id) + "/season/" + str(season_nb) + "/episode/" + str(episode_nb)
        url_cont = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())
        self.episode_nb = episode_nb
        self.title = url_cont["name"]
        self.overview = url_cont["overview"]
        self.broadcast_date = url_cont["air_date"]
        self.vote_average = url_cont["vote_average"]

