from django.urls import path

from . import views

#added pattern of contacts path
app_name = 'contacts'
urlpatterns = [
    path('', views.index , name = 'contacts')
]