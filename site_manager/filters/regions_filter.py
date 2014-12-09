import django_filters

from site_manager.models import Regions


class RegionsFilter(django_filters.FilterSet):
    class Meta:
        model = Regions
        fields = ['name', 'country_id']
