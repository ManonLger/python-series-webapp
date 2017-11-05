import json
import requests
import site_series.settings as settings
from django.db import models

from app_series.models.tv_show import TvShow

class SeasonManager(models.Manager):
    def create_season(self, tmdb_id, season_nb):
        url = settings.TMDB_API_URL + "tv/" + str(tmdb_id) + "/season/" + str(season_nb)
        content = json.loads(requests.get(url, params={"api_key": settings.TMDB_API_KEY}).content.decode())

        season = self.create(
            tv_show=TvShow.objects.create_tv_show(tmdb_id=tmdb_id),
            season_nb=season_nb,
            title=content["name"],
            overview=content["overview"],
            nb_of_episodes=len(content["episodes"])
        )
        return season

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
    title = models.CharField(max_length=100, null=True)
    overview = models.CharField(max_length=1000, null=True)
    nb_of_episodes = models.IntegerField(default=0)

    objects = SeasonManager()