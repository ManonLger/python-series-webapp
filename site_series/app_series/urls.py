from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^serie/(\d+)$', views.view_serie, name='view_serie')
]