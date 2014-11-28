from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from serializers import CountriesSerializer
from serializers import DistrictsSerializer
from serializers import FishesSerializer
from serializers import MarkersSerializer
from serializers import MarkersFishesSerializer
from serializers import MarkersLogSerializer
from serializers import PassportsSerializer
from serializers import RegionsSerializer

from models import Countries
from models import Districts
from models import Fishes
from models import Markers
from models import MarkersFishes
from models import MarkersLog
from models import Passports
from models import Regions


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class DistrictsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer


class FishesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fishes.objects.all()
    serializer_class = FishesSerializer


class MarkersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Markers.objects.all()
    serializer_class = MarkersSerializer


class MarkersFishesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MarkersFishes.objects.all()
    serializer_class = MarkersFishesSerializer


class MarkersLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MarkersLog.objects.all()
    serializer_class = MarkersLogSerializer


class PassportsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passports.objects.all()
    serializer_class = PassportsSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer
