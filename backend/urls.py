from django.urls import path
from . import views

urlpatterns = [
    path('', views.run_nba, name='run_nba'),
    path('team-stats/', views.team_stats, name='team_stats'),
    path('team/<str:team_name>/', views.team_detail, name='team_detail'),
]