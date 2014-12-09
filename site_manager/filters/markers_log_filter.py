import django_filters

from site_manager.models import MarkersLog


class MarkersLogFilter(django_filters.FilterSet):
    class Meta:
        model = MarkersLog
        fields = []
