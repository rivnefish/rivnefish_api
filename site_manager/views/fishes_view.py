from rest_framework import viewsets

from site_manager.filters.fishes_filters import FishesFilter
from site_manager.models import Fishes
from site_manager.serializers.fishes_serializer import FishesSerializer


class FishesViewSet(viewsets.ModelViewSet):

    serializer_class = FishesSerializer
    queryset = Fishes.objects.all()
    filter_class = FishesFilter
