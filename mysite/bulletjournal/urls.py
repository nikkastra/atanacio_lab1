from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('home', index_card_view, name = 'home'),
    path('profile', profile, name = 'profile'),
    path('key', key, name = 'key'),
    path('thisweek', thisweek, name = 'thisweek'),
    path('today', today, name = 'today')
]