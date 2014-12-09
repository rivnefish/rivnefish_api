from rest_framework import viewsets

from site_manager.filters.passports_filter import PassportsFilter
from site_manager.models import Passports
from site_manager.serializers.passport_serializer import PassportsSerializer


class PassportsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Passports.objects.all()
    serializer_class = PassportsSerializer
