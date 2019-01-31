# from django.urls import path,
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^$', views.index1, name='index1')
]
#    include('mainApp.urls')
