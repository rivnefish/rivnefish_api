from rest_framework import viewsets

from site_manager.filters import DistrictsFilter
from site_manager.models import Districts
from site_manager.serializers import DistrictsSerializer


class DistrictsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
