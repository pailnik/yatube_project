from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('', views.index),
    path('group/', views.group_list, name='group_list'),
    path('group/<slug:slug>/',
         views.group_detail)
]
