from rest_framework import viewsets
from rest_framework.response import Response

from site_manager.filters.markers_filter import MarkersFilter
from site_manager.models import Markers
from site_manager.serializers.markers_serializer import MarkersSerializer
from site_manager.serializers.markers_serializer import ShortMarkersSerializer


class MarkersViewSet(viewsets.ModelViewSet):

    queryset = Markers.objects.all()
    serializer_class = MarkersSerializer
    #=============================================================
    # This is for disable web ui and return only json
    # from rest_framework import renderers
    # renderer_classes = [renderers.JSONRenderer]
    #=============================================================
    filter_class = MarkersFilter


class ShortMarkersViewSet(viewsets.ModelViewSet):

    queryset = Markers.objects.all()
    serializer_class = ShortMarkersSerializer
    filter_class = MarkersFilter


class LastChangesViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        query = 'SELECT COUNT(*)*MAX(modify_date) FROM `markers`'
        time = Markers.objects.raw(query)
        result = list(time.query)[0][0]
        return Response({"lastchanges": result})
