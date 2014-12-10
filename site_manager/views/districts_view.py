from rest_framework import viewsets

from site_manager.filters.districts_filter import DistrictsFilter
from site_manager.models import Districts
from site_manager.serializers.districts_serializer import DistrictsSerializer


class DistrictsViewSet(viewsets.ModelViewSet):

    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
    filter_class = DistrictsFilter
