from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_gitmyseries.models.tv_show import TvShow
from django.views.generic import ListView

class WishListView(ListView):
    """This class is based on ListView special feature in Django"""
    model = TvShow #This view is based on the model TvShow
    template_name = "app_gitmyseries/wishlist.html" #The template linked to this ListView

    def get_queryset(self):
        if self.request.user.username == '':
            pass
        else:
            wishes = self.request.user.wishlist.wishes #Get current user's wishlist
            return wishes.order_by("-next_episode_run_time")

    def post(self, request, tmdb_id):
        request.user.wishlist.remove_from_list(tmdb_id) #Call the method to remove the tv_show from the wishlist
        return HttpResponseRedirect(reverse("wishlist_url")) #Redirect to the wishlist_url
