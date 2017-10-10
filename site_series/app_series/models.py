from django.db import models

class TvShow(models.Model):
    title = models.CharField(max_length=100)

class Season(models.Model):
    num = models.IntegerField()

class Episode(models.Model):
    num = models.IntegerField()