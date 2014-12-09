import django_filters

from site_manager.models import Passports


class PassportsFilter(django_filters.FilterSet):
    """
    """

    class Meta:
        model = Passports
        fields = []
