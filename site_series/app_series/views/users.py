from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render

from app_series.models import Wishlist

def signup(request):
    error = False
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.wishlist = Wishlist(user=user)
            go_to_login = True
        else:
            error = True
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', locals())


