from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow
from django.views.generic import ListView


class WishListView(ListView):
    model = TvShow
    template_name = "app_series/wishlist.html"

    def get_queryset(self):
        user = self.request.user #On récupère l'utilisateur connecté
        return user.wishlist.wishes.all() #On renvoie la liste des wishes de cet utilisateur

@login_required(login_url='login')
def add_to_wishlist(request, tmdb_id):
    tv_show = TvShow.objects.create_tv_show(tmdb_id=tmdb_id)
    if tv_show.save() is True:
        seasons_list = range(1, tv_show.nb_of_seasons)
        return render(request, 'app_series/tv_show.html', locals())
    else:
        tv_show.save()
        seasons_list = range(1, tv_show.nb_of_seasons)
        return render(request, 'app_series/tv_show.html', locals())
    tv_show.save()

    """serie_form= SerieForm()
    if request.method == 'POST':
        form = SerieForm(request.POST)
        form.save()
    return render(request, 'app_series/tv_show.html')"""

@login_required(login_url='login')
def remove_from_wishlist(request, tmdb_id):
    user = request.user
    tv_show = user.wishlist.wishes.filter(tmdb_id=tmdb_id)[0]
    user.wishlist.wishes.remove(tv_show)
    return HttpResponseRedirect(reverse("wishlist_url"))
