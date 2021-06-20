from django.urls import path
from django.contrib import admin
from points import views
from django.urls import include

app_name = 'points'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('team/<slug:team_name_slug>/',
         views.show_team, name='show_team'),
    path('team/<slug:team_name_slug>/add_5points/', views.add_5points, name='add_5points'),
    path('team/<slug:team_name_slug>/remove_5points/', views.remove_5points, name='remove_5points'),
    path('team/<slug:team_name_slug>/late/', views.late, name='late'),
    path('team/<slug:team_name_slug>/third/', views.third, name='third'),
    path('team/<slug:team_name_slug>/first/', views.first, name='first'),
    path('team/<slug:team_name_slug>/second/', views.second, name='second'),
]
