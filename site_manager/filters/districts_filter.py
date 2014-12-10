import django_filters

from site_manager.models import Districts


class DistrictsFilter(django_filters.FilterSet):

    class Meta:
        region = django_filters.AllValuesFilter('region__region_id')
        model = Districts
        fields = ['district_id']
