from rest_framework import viewsets

from site_manager.filters import PassportsFilter
from site_manager.models import Passports
from site_manager.serializers import PassportsSerializer


class PassportsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Passports.objects.all()
    serializer_class = PassportsSerializer
