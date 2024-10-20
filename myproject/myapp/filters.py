from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter, BooleanFilter
from .models import Player

class PlayerFilter(FilterSet):
    # Фильтр объединения имени и фамилии
    name = CharFilter(field_name='first_name', method='filter_name', label='Имя/Фамилия')

    # Диапазон номера
    number_min = NumberFilter(field_name='number', lookup_expr='gte', label='Номер от')
    number_max = NumberFilter(field_name='number', lookup_expr='lte', label='Номер до')

    # Фильтр позиции
    position = ChoiceFilter(field_name='position', choices=[
        ('Нападающий', 'Нападающий'),
        ('Защитник', 'Защитник'),
        ('Вратарь', 'Вратарь'),
    ], label='Позиция')


    is_russian = BooleanFilter(field_name='nationality', method='filter_nationality', label='Русский игрок')

    class Meta:
        model = Player
        fields = ['name', 'number_min', 'number_max', 'position', 'is_russian']

    def filter_name(self, queryset, name, value):
        return queryset.filter(first_name__icontains=value) | queryset.filter(last_name__icontains=value)

    def filter_nationality(self, queryset, name, value):
        if value:
            return queryset.filter(nationality='Россия')
        else:
            return queryset.exclude(nationality='Россия')
