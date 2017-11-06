from django.contrib.auth.models import User
from django.db import models
from app_series.models.tv_show import TvShow

class Wishlist(models.Model):
    user = models.OneToOneField(User) #a wishlist is linked to an unique user
    wishes = models.ManyToManyField(TvShow) #there are several TvShow objects in a wishlist and a TvShow object can belong to several wishlit

    def is_in_list(self, tmdb_id):
        """Method that checks if a TvShow object is already in the user wishlist"""
        bool = False
        try:
            self.wishes.get(tmdb_id=tmdb_id)
            bool = True
        except TvShow.DoesNotExist:
            pass
        finally:
            return bool

    def add_to_list(self, tmdb_id):
        """Method that adds a TvShow to an user wishlist if it's not already in the wishlist"""
        if self.is_in_list(tmdb_id):
            pass
        else:
            tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id) #creates the Tv_Show object
            self.wishes.add(tv_show) #add it to the user wishlist

    def remove_from_list(self, tmdb_id):
        """Method that remove a TvShow from an user wishlist if it's already in the wishlist"""
        if self.is_in_list(tmdb_id):
            tv_show = self.wishes.get(tmdb_id=tmdb_id) #get the tv_show object we want to remove
            self.wishes.remove(tv_show) #remove it from the user wishlist
