import django_filters

from site_manager.models import Markers
from range_filters import IntegerListFilter
from range_filters import IntegerListFilterUniq
from enum_filters import FilterForEnumField


class MarkersFilter(django_filters.FilterSet):

    """ Filters for markers.

    `/api/markers/?distance_lower=15` - get all merkers with distance to Rivne lower then 15 meters
    `/api/markers/?distance_higher=1` - get all markers with distance to Rivne higher then 1 meters
    `/api/markers/?distance_higher=1&distance_lower=15` - get all markers in Range from 1 to 15 meters
     or
    `/api/markers/?distance_lower=100&distance_higher=1`

    `/api/markers/?fishes=35,34` - get all markers with fish 35 OR 34

    `/api/markers/?name=NAME` - get all markers that contains %NAME%

    `/api/markers/?permit=paid` - get all with specific permit from available
    `/api/markers/?boat=1` - get markers with boat usage True or False
    `/?fish_catch=10000` - get markers woth fish catch >=10000
    """

    distance_lower = django_filters.NumberFilter(name="distance_to_rivne",
                                                 lookup_type="lte")
    distance_higher = django_filters.NumberFilter(name="distance_to_rivne",
                                                  lookup_type="gte")
    fishes = IntegerListFilter(name="fishes_set__fish", lookup_type="in")
    ufishes = IntegerListFilterUniq(name="fishes_set__fish", lookup_type="in")
    name = django_filters.CharFilter(name="name", lookup_type="icontains")
    permit = FilterForEnumField(name="permit", lookup_type="iexact",
                                available=("free", "paid", "prohibited",
                                           "unknown"))
    price = django_filters.NumberFilter(name="price_24h", lookup_type="lte")
    boat = FilterForEnumField(name="boat_usage", lookup_type="exact",
                              available=(1, 0), used_int=True)
    fish_catch = django_filters.NumberFilter(name="fishes_set__weight_avg",
                                             lookup_type="gte")

    class Meta:
        model = Markers
        fields = ["distance_higher", "distance_lower", "fishes", "ufishes",
                  "name", "permit", "price", 'boat', 'fish_catch']
