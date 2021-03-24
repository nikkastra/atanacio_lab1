from django.urls import path

from .views import HomePageView, index_card_view


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('home', index_card_view, name = 'home')
]