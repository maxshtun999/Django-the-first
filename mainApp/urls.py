# from django.urls import path,
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # url(r'^contact/$', include('contact.urls')),

    # url(r'^news/$', include('news.urls')),

    # url(r'^help/$', include('help.urls')),
]
#    include('mainApp.urls')
