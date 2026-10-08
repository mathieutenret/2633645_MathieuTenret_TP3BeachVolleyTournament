from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('teams/create/one/', views.create_team_one, name='create_team_one'),
    path('teams/create/two/', views.create_team_two, name='create_team_two'),
    path('teams/<int:team_id>/add-player/', views.add_player, name='add_player'),
    path('teams/<int:team_id>/edit/', views.edit_team, name='edit_team'),
    path('teams/<int:team_id>/delete/', views.delete_team, name='delete_team'),
]