from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< Updated upstream
=======
    url(r'^serie/(\d+)$', views.view_season, name='view_season')
>>>>>>> Stashed changes
]