from django.db import models

class HockeyClub(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    number = models.IntegerField()
    nationality = models.CharField(max_length=100)
    hockey_club = models.ForeignKey(HockeyClub, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class CoachingStaff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    hockey_club = models.ForeignKey(HockeyClub, on_delete=models.CASCADE, related_name='coaching_staff')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"