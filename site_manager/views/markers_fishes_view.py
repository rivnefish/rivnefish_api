from rest_framework import viewsets

from site_manager.filters.markers_fishes_filter import MarkersFishesFilter
from site_manager.models import MarkersFishes
from site_manager.serializers import MarkersFishesSerializer


class MarkersFishesViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = MarkersFishes.objects.all()
    serializer_class = MarkersFishesSerializer
    filter_class = MarkersFishesFilter
