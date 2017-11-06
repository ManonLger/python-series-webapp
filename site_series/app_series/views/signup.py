from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render

from app_series.models.wishlist import Wishlist
from django.views.generic import ListView

def signup(request):
    error = False
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Wishlist.objects.create(user=user) #A chaque fois qu'un utilisateur est créée, on lui associe une wishlist vide
            go_to_login = True
        else:
            error = True
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', locals())