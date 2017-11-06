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

    def post(self, request, tmdb_id):
        request.user.wishlist.remove_from_list(tmdb_id)
        return HttpResponseRedirect(reverse("wishlist_url"))
