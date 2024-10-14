from django.contrib import admin
from .models import HockeyClub, Player, CoachingStaff

@admin.register(HockeyClub)
class HockeyClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded_year')
    search_fields = ('name', 'city')
    list_filter = ('founded_year',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'number', 'nationality', 'hockey_club')
    search_fields = ('first_name', 'last_name', 'position')
    list_filter = ('position', 'hockey_club')

@admin.register(CoachingStaff)
class CoachingStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'hockey_club')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role', 'hockey_club')

