from rest_framework import viewsets

from site_manager.filters.markers_log_filter import MarkersLogFilter
from site_manager.models import MarkersLog
from site_manager.serializers.markers_log_serialaizer import MarkersLogSerializer


class MarkersLogViewSet(viewsets.ModelViewSet):

    queryset = MarkersLog.objects.all()
    serializer_class = MarkersLogSerializer
    filter_class = MarkersLogFilter
