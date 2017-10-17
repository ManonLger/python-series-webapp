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
    num = models.IntegerField()

class Episode(models.Model):
    num = models.IntegerField()