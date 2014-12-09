from rest_framework import viewsets

from site_manager.filters import RegionsFilter
from site_manager.models import Regions
from site_manager.serializers import RegionsSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer
