import factory
from myapp import models

class HockeyClubFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    city = factory.Faker('city')
    founded_year = factory.Faker('random_int', min=1875, max=2024)

    class Meta:
        model = models.HockeyClub

class PlayerFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    position = factory.Iterator(['Нападающий', 'Защитник', 'Вратарь'])
    number = factory.Faker('random_int', min=1, max=99)
    nationality = factory.Faker('country')
    hockey_club = factory.SubFactory(HockeyClubFactory)

    class Meta:
        model = models.Player

class CoachingStaffFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    role = factory.Iterator(['Главный тренер', 'Тренер', 'Тренер вратарей', 'Тренер по физической подготовке'])
    hockey_club = factory.SubFactory(HockeyClubFactory)

    class Meta:
        model = models.CoachingStaff
