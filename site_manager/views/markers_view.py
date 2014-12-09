from rest_framework import viewsets

from site_manager.filters.markers_filter import MarkersFilter
from site_manager.models import Markers
from site_manager.serializers.markers_serializer import MarkersSerializer


class MarkersViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Markers.objects.all()
    serializer_class = MarkersSerializer
    #=============================================================
    # This is for disable web ui and return only json
    # from rest_framework import renderers
    # renderer_classes = [renderers.JSONRenderer]
    #=============================================================
    filter_class = MarkersFilter
