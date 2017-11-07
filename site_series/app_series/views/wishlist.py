from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from app_series.models.tv_show import TvShow
from django.views.generic import ListView

class WishListView(ListView):
    """This class is based on ListView special feature in Django"""
    model = TvShow #This view is based on the model TvShow
    template_name = "app_series/wishlist.html" #The template linked to this ListView

    def get_queryset(self):
        user = self.request.user #Get the current user logged 
        return user.wishlist.wishes.order_by("-next_episode_run_time") #Return all the tv_shows in the wishlist of the user

    def post(self, request, tmdb_id):
        request.user.wishlist.remove_from_list(tmdb_id) #Call the method to remove the tv_show from the wishlist
        return HttpResponseRedirect(reverse("wishlist_url")) #Redirect to the wishlist_url
