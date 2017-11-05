from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow

def tv_show(request, tmdb_id):
    tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id)
    seasons_list = range(1, tv_show.nb_of_seasons+1)
    next_episode = tv_show.next_episode_run_time
    if request.method == "POST":
        user = request.user
        if len(TvShow.objects.filter(tmdb_id=tmdb_id)) == 0:
            tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id)
            tv_show.save()
            user.wishlist.wishes.add(tv_show)
        if len(user.wishlist.wishes.filter(tmdb_id=tmdb_id)) == 0:
            user.wishlist.wishes.add(tv_show)
        return HttpResponseRedirect(reverse("tv_show_url", args=[tmdb_id]))
    return render(request, 'app_series/tv_show.html',locals())
