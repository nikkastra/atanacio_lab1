from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('home', home, name = 'home'),
    path('profile', profile, name = 'profile'),
    path('key', key, name = 'key'),
    path('this_week', thisweek, name = 'thisweek'),
    path('today', today, name = 'today'),
    path('names', NameListView.as_view(), name = 'name_list'),
    path('name/<int:pk>', NameDetailView.as_view(), name = 'name_detail')
]