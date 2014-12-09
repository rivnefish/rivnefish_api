import django_filters

from site_manager.models import Markers
from range_filters import IntegerListFilter
from range_filters import IntegerListFilterUniq


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
