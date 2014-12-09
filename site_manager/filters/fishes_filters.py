import django_filters

from site_manager.models import Fishes


class FishesFilter(django_filters.FilterSet):
    """
    """

    class Meta:
        model = Fishes
        fields = ['eng_name', 'fish_id']
