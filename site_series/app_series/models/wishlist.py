from django.contrib.auth.models import User
from django.db import models
from app_series.models.tv_show import TvShow

class Wishlist(models.Model):
    user = models.OneToOneField(User)
    wishes = models.ManyToManyField(TvShow)