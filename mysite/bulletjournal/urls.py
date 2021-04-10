from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('home', home, name = 'home'),
    path('profile', profile, name = 'profile'),
    path('key', key, name = 'key'),
    path('thisweek', TaskListView.as_view(), name = 'thisweek'),
    path('addtask', thisweek, name = 'addtask'),
    path('addtoday', today, name = 'addtoday'),
    path('today', TodayListView.as_view(), name = 'today'),
    path('delete', delete_task, name = 'delete'),
    path('task/<int:pk>', TaskDetailView.as_view(), name = 'task_detail'),
    path('today/<int:pk>', TodayDetailView.as_view(), name = 'today_detail')
]