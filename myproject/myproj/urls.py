from django.contrib import admin
from django.urls import path
from myapp.views import (
    HockeyClubListView,
    HockeyClubDetailView,
    PlayerListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
    CoachListView,
    CoachCreateView,
    CoachUpdateView,
    CoachDeleteView
)

urlpatterns = [
    path('', HockeyClubListView.as_view(), name='club-list'),
    path('club/<int:pk>/', HockeyClubDetailView.as_view(), name='club-detail'),
    path('club/<int:club_id>/players/', PlayerListView.as_view(), name='team-list'),
    path('club/<int:club_id>/players/create/', PlayerCreateView.as_view(), name='player-create'),
    path('club/<int:club_id>/players/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('club/<int:club_id>/players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('club/<int:club_id>/players/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),
    path('club/<int:club_id>/coaches/', CoachListView.as_view(), name='coaching-staff-list'),
    path('club/<int:club_id>/coaches/create/', CoachCreateView.as_view(), name='coach-create'),
    path('club/<int:club_id>/coaches/<int:pk>/update/', CoachUpdateView.as_view(), name='coach-update'),
    path('club/<int:club_id>/coaches/<int:pk>/delete/', CoachDeleteView.as_view(), name='coach-delete'),
]