from django.contrib.auth.models import User
from django.db import models
from app_series.models.tv_show import TvShow

class Wishlist(models.Model):
    user = models.OneToOneField(User)
    wishes = models.ManyToManyField(TvShow)

    def is_in_list(self, tmdb_id):
        bool = False
        try:
            self.wishes.get(tmdb_id=tmdb_id)
            bool = True
        except TvShow.DoesNotExist:
            pass
        finally:
            return bool

    def add_to_list(self, tmdb_id):
        if self.is_in_list(tmdb_id):
            pass
        else:
            tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id)
            self.wishes.add(tv_show)

    def remove_from_list(self, tmdb_id):
        if self.is_in_list(tmdb_id):
            tv_show = self.wishes.get(tmdb_id=tmdb_id)
            self.wishes.remove(tv_show)
