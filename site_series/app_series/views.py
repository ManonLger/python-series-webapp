from django.shortcuts import render

from django.http import HttpResponse
from .models import TvShow

def index(request):
    list = ", ".join([str(tvs) for tvs in TvShow.objects.all()])
    return HttpResponse("Liste de séries : "+list)