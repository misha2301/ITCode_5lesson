from django.test import TestCase
from django.urls import reverse
from myapp.models import Player, HockeyClub, CoachingStaff
from myapp.factories import PlayerFactory, HockeyClubFactory, CoachingStaffFactory


class HockeyClubTests(TestCase):
    def setUp(self):

        self.club = HockeyClubFactory()

    def test_club_list_view(self):
        response = self.client.get(reverse('club-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.club.name)
        hockeyclub = HockeyClub.objects.count()
        self.assertEqual(response.context['hockey_clubs'].count(), hockeyclub)

    def test_club_detail_view(self):
        response = self.client.get(reverse('club-detail', args=[self.club.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.club.name)


class PlayerTests(TestCase):
    def setUp(self):

        self.club = HockeyClubFactory()
        self.player = PlayerFactory(hockey_club=self.club)

    def test_player_list_view(self):
        response = self.client.get(reverse('team-list', args=[self.club.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.player.first_name)

    def test_player_create_view(self):
        player_count = Player.objects.count()
        response = self.client.post(reverse('player-create', args=[self.club.id]), {
            'first_name': 'Павел',
            'last_name': 'Датцук',
            'position': 'Нападающий',
            'number': 13,
            'nationality': 'Россия',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Player.objects.count(), player_count + 1)

    def test_player_update_view(self):
        response = self.client.post(reverse('player-update', args=[self.club.id, self.player.id]), {
            'first_name': 'Updated',
            'last_name': self.player.last_name,
            'position': self.player.position,
            'number': self.player.number,
            'nationality': self.player.nationality,
        })
        self.assertEqual(response.status_code, 302)
        self.player.refresh_from_db()
        self.assertEqual(self.player.first_name, 'Updated')

    def test_player_delete_view(self):
        player_count = Player.objects.count()
        response = self.client.post(reverse('player-delete', args=[self.club.id, self.player.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Player.objects.count(), player_count - 1)


class CoachingStaffTests(TestCase):
    def setUp(self):
        # Создаем тестовый клуб и тренера
        self.club = HockeyClubFactory()
        self.coach = CoachingStaffFactory(hockey_club=self.club)

    def test_coach_list_view(self):
        response = self.client.get(reverse('coaching-staff-list', args=[self.club.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.coach.first_name)

    def test_coach_create_view(self):
        coach_count = CoachingStaff.objects.count()
        response = self.client.post(reverse('coach-create', args=[self.club.id]), {
            'first_name': 'Алан',
            'last_name': 'Фатихов',
            'role': 'Тренер вратарей',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CoachingStaff.objects.count(), coach_count + 1)

    def test_coach_update_view(self):
        response = self.client.post(reverse('coach-update', args=[self.club.id, self.coach.id]), {
            'first_name': 'Updated',
            'last_name': self.coach.last_name,
            'role': self.coach.role,
        })
        self.assertEqual(response.status_code, 302)
        self.coach.refresh_from_db()
        self.assertEqual(self.coach.first_name, 'Updated')

    def test_coach_delete_view(self):
        coach_count = CoachingStaff.objects.count()
        response = self.client.post(reverse('coach-delete', args=[self.club.id, self.coach.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CoachingStaff.objects.count(), coach_count - 1)
