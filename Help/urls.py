from django.urls import path

from . import views

# added pattern of contacts path
app_name = 'Help'
urlpatterns = [
    path('', views.index, name='Help'),
    path('thanks/', views.thanks, name = 'thanks')
]