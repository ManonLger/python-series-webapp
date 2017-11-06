from django.shortcuts import render

from app_series.models.episode import Episode

def episode(request, tmdb_id, season_nb, episode_nb):
    """The view of the Episode"""
    episode = Episode.objects.create_episode(tmdb_id=tmdb_id, season_nb=season_nb, episode_nb=episode_nb) #Create the episode object if not already existing in the database
    return render(request, 'app_series/episode.html', locals()) #return to the episode template