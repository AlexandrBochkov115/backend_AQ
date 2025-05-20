from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    # Фильтр по популярности (категориальный)
    popularity_status = filters.ChoiceFilter(
        choices=[('popular', 'Popular'), ('unpopular', 'Unpopular'), ('average', 'Average')],
        method='filter_by_popularity',
        label='Popularity Status'
    )

    # Фильтр по диапазону популярности
    popularity_range = filters.NumericRangeFilter(
        field_name='popularity',
        label='Popularity Range (min-max)'
    )

    # Сортировка по имени и популярности
    ordering = filters.OrderingFilter(
        fields=[
            ('name', 'name'),
            ('-name', 'name_desc'),
            ('popularity', 'popularity_asc'),
            ('-popularity', 'popularity_desc'),
        ],
        field_labels={
            'name': 'Name (A-Z)',
            '-name': 'Name (Z-A)',
            'popularity': 'Popularity (Low-High)',
            '-popularity': 'Popularity (High-Low)',
        }
    )

    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'category__name': ['exact'],
            'category__slug': ['exact'],
        }

    def filter_by_popularity(self, queryset, name, value):
        """Кастомный фильтр для статуса популярности"""
        if value == 'popular':
            return queryset.filter(popularity__gte=70)
        elif value == 'unpopular':
            return queryset.filter(popularity__lt=30)
        elif value == 'average':
            return queryset.filter(popularity__gte=30, popularity__lt=70)
        return queryset