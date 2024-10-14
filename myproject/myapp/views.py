# views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Player, HockeyClub, CoachingStaff


class HockeyClubListView(ListView):
    model = HockeyClub
    template_name = 'team_list.html'
    context_object_name = 'hockey_clubs'

class HockeyClubDetailView(DetailView):
    model = HockeyClub
    template_name = 'hockeyclub_detail.html'
    context_object_name = 'hockey_club'

class PlayerListView(ListView):
    model = Player
    template_name = 'players_list.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.filter(hockey_club_id=self.kwargs['club_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = HockeyClub.objects.get(pk=self.kwargs['club_id'])
        return context

class PlayerCreateView(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'number', 'nationality', 'position']
    template_name = 'player_form.html'

    def form_valid(self, form):
        form.instance.hockey_club_id = self.kwargs['club_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('team-list', kwargs={'club_id': self.kwargs['club_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club_id'] = self.kwargs['club_id']
        return context

class PlayerUpdateView(UpdateView):
    model = Player
    fields = ['first_name', 'last_name', 'number', 'position', 'nationality']
    template_name = 'player_form.html'

    def get_success_url(self):
        return reverse('team-list', kwargs={'club_id': self.object.hockey_club.id})  # Получаем club_id из объекта игрока

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club_id'] = self.object.hockey_club.id  # Передаем club_id в контекст
        return context

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player_confirm_delete.html'

    def get_success_url(self):
        return reverse('team-list', kwargs={'club_id': self.object.hockey_club.id})  # Получаем club_id из объекта игрока

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hockey_club'] = self.object.hockey_club
        return context

class CoachCreateView(CreateView):
    model = CoachingStaff
    template_name = 'coach_form.html'
    fields = ['first_name', 'last_name']

    def form_valid(self, form):
        form.instance.hockey_club_id = self.kwargs['club_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('coaching-staff-list', kwargs={'club_id': self.kwargs['club_id']})

class CoachUpdateView(UpdateView):
    model = CoachingStaff
    template_name = 'coach_form.html'
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        return reverse_lazy('coaching-staff-list', kwargs={'club_id': self.kwargs['club_id']})

class CoachDeleteView(DeleteView):
    model = CoachingStaff
    template_name = 'coach_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('coaching-staff-list', kwargs={'club_id': self.kwargs['club_id']})

class CoachListView(ListView):
    model = CoachingStaff
    template_name = 'coaching_staff_list.html'
    context_object_name = 'coaches'

    def get_queryset(self):
        return CoachingStaff.objects.filter(hockey_club_id=self.kwargs['club_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hockey_club'] = HockeyClub.objects.get(pk=self.kwargs['club_id'])
        return context