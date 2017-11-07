from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow

def tv_show(request, tmdb_id):
    tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id) #Create the tv_show object if not already existing in the database
    seasons_list = range(1, tv_show.nb_of_seasons+1) #create a list of the seasons in the tv_show, to be used in the template
    next_episode = tv_show.next_episode_run_time #get the next_episode date

    anonymous = request.user.username == '' #boolean indicating if the user is AnonymousUser
    if not anonymous:
        is_in_wishlist = request.user.wishlist.is_in_list(tmdb_id) #get the info if the tv_show is already in the user's wishlist
        if request.method == "POST":
            request.user.wishlist.add_to_list(tmdb_id)  # add the tv_show to the user's wishlist
            return HttpResponseRedirect(reverse("tv_show_url", args=[tmdb_id]))  # redirect to the tv_show_url view

    return render(request, 'app_series/tv_show.html', locals()) #return to the tv_show template
