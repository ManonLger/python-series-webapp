from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from app_gitmyseries.models.wishlist import Wishlist
from django.views.generic import ListView

def signup(request):
    error = False
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Wishlist.objects.create(user=user) #Each time an user is created, an empty wishlist is linked to this user.
            messages.success(request, "Well done! You can now login to browse all of your favorite tv shows!")
            return HttpResponseRedirect(reverse('login'))
        else:
            error = True
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', locals())