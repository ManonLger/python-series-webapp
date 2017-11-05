import json
import requests
import site_series.settings as settings
from django.db import models
from datetime import datetime

class TvShowManager(models.Manager):
    def create_tv_show_from_args(self, tmdb_id, **kwargs):
        try:
            tv_show = TvShow.objects.filter(tmdb_id=tmdb_id)
            tv_show.update(**kwargs)
            tv_show = tv_show.first()
        except TvShow.DoesNotExist:
            tv_show = TvShow.objects.create(tmdb_id=tmdb_id, **kwargs)
            tv_show.save()
        finally:
            return tv_show

    def create_tv_show(self, tmdb_id):
        url = settings.TMDB_API_URL + "tv/" + str(tmdb_id)
        content = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())

        tv_show = self.create_tv_show_from_args(
            tmdb_id=tmdb_id,
            title=content["name"],
            overview=content["overview"],
            nb_of_seasons=content["number_of_seasons"],
            is_in_production=content["in_production"]
        )
        return tv_show

class TvShow(models.Model):
    """Definition of the class TvShow, it contains the following attributes :
           - id of the tvshow in the API Tmdb
           - name
           - overview : the description of the app_tvshow
           - nb_season : number of seasons in the app_tvshow
           - in_production : if set to True, the app_tvshow is still in production ; if set to False, it's been over"""
    tmdb_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    nb_of_seasons = models.IntegerField(default=0)
    is_in_production = models.BooleanField(default=True)

    objects = TvShowManager()

    def __str__(self):
        return self.title

    @property
    def next_episode_run_time(self):
        """Methode that gets the next episode date in the current season"""
        url = settings.TMDB_API_URL + "tv/" + str(self.tmdb_id)
        last_air_date = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())["last_air_date"]
        if (datetime.strptime(last_air_date, '%Y-%m-%d') > datetime.now()):
            return last_air_date
        else :
            return "Non renseigné"