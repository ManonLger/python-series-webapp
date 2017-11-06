from django.shortcuts import render

from app_series.models.season import Season

def season(request, tmdb_id, season_nb):
    season = Season.objects.create_season(tmdb_id=tmdb_id, season_nb=season_nb) #Create the season object if not already existing in the database
    episodes_list = range(1, season.nb_of_episodes+1) #create a list of the episodes in the season, to be used in the template
    return render(request, 'app_series/season.html', locals()) #return to the season template
