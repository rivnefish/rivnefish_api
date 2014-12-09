from rest_framework import viewsets

from site_manager.filters import MarkersLogFilter
from site_manager.models import MarkersLog
from site_manager.serializers import MarkersLogSerializer


class MarkersLogViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = MarkersLog.objects.all()
    serializer_class = MarkersLogSerializer
