import django_filters

from site_manager.models import MarkersFishes


class MarkersFishesFilter(django_filters.FilterSet):
    """
    """

    class Meta:
        model = MarkersFishes
        fields = ['marker']
