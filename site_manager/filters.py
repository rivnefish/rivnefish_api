import django_filters

from models import Countries
from models import Districts
from models import Regions
from models import Fishes
from models import Markers
from models import MarkersFishes
from models import MarkersLog
from models import Passports


class CountriesFilter(django_filters.FilterSet):
    class Meta:
        model = Countries
        fields = ['name', 'country_id']


class DistrictsFilter(django_filters.FilterSet):
    class Meta:
        region = django_filters.AllValuesFilter('region__region_id')
        model = Districts
        fields = ['district_id']


class RegionsFilter(django_filters.FilterSet):
    class Meta:
        model = Regions
        fields = ['name', 'country_id']


class FishesFilter(django_filters.FilterSet):

    class Meta:
        model = Fishes
        fields = ['eng_name', 'fish_id']


# Get example of custom filters here http://bit.ly/1ythc3Z
class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',') if v]
            qs.filter(**{'%s__%s' % (self.name,
                                     self.lookup_type): integers})
        return qs


class IntegerListFilterUniq(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            for _id in set([int(v) for v in value.split(',') if v]):
                qs = qs.filter(fishes_set__fish=_id)
        return qs


class MarkersFilter(django_filters.FilterSet):
    """ Filters for markers.

    `/api/markers/?distance_lower=15` - get all merkers with distance to Rivne lower then 15 meters
    `/api/markers/?distance_higher=1` - get all markers with distance to Rivne higher then 1 meters
    `/api/markers/?distance_higher=1&distance_lower=15` - get all markers in Range from 1 to 15 meters
    or `/api/markers/?distance_lower=100&distance_higher=1`

    `/api/markers/?fishes=35,34` - get all markers with fish 35 OR 34

    !!! I do not use `django_filters.RangeFilter` because it`s not working!!!


    For filter markers by fish/fishes.
    Markers.objects.filter(fishes_set__fish__in=[35,34])
    """

    distance_lower = django_filters.NumberFilter(name="distance_to_rivne", lookup_type='lte')
    distance_higher = django_filters.NumberFilter(name="distance_to_rivne", lookup_type='gte')
    fishes = IntegerListFilter(name="fishes_set__fish", lookup_type='in')
    ufishes = IntegerListFilterUniq(name="fishes_set__fish", lookup_type='in')

    class Meta:
        model = Markers
        fields = ['distance_higher', 'distance_lower', 'fishes', 'ufishes']

    #===========================================================================
    # def __init__(self, *args, **kwargs):
    #     print args
    #     print kwargs
    #     super(MarkersFilter, self).__init__(*args, **kwargs)
    #===========================================================================


class MarkersFishesFilter(django_filters.FilterSet):

    class Meta:
        model = MarkersFishes
        fields = ['marker']


class MarkersLogFilter(django_filters.FilterSet):
    class Meta:
        model = MarkersLog
        fields = []


class PassportsFilter(django_filters.FilterSet):
    class Meta:
        model = Passports
        fields = []
