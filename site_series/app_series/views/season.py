from django.shortcuts import render

from app_series.models.season import Season

def season(request, tmdb_id, season_nb):
    season = Season.objects.create_season(tmdb_id=tmdb_id, season_nb=season_nb)
    episodes_list = range(1, season.nb_of_episodes+1)
    return render(request, 'app_series/season.html', locals())