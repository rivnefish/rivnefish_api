from rest_framework import viewsets

from site_manager.filters import FishesFilter
from site_manager.models import Fishes
from site_manager.serializers import FishesSerializer


class FishesViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = FishesSerializer
    queryset = Fishes.objects.all()