import django_filters

from site_manager.models import Countries


class CountriesFilter(django_filters.FilterSet):
    class Meta:
        model = Countries
        fields = ['name', 'country_id']
