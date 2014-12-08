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

from filters import CountriesFilter
from filters import DistrictsFilter
from filters import FishesFilter
from filters import MarkersFilter
from filters import MarkersFishesFilter
from filters import MarkersLogFilter
from filters import PassportsFilter
from filters import RegionsFilter


class CountryViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class DistrictsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer


class FishesViewSet(viewsets.ModelViewSet):
    """
    """

    serializer_class = FishesSerializer
    queryset = Fishes.objects.all()


class MarkersViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Markers.objects.all()
    serializer_class = MarkersSerializer

    #=============================================================
    # This is for disable web ui and return only json
    # from rest_framework import renderers
    # renderer_classes = [renderers.JSONRenderer]
    #=============================================================
    filter_class = MarkersFilter


class MarkersFishesViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = MarkersFishes.objects.all()
    serializer_class = MarkersFishesSerializer
    filter_class = MarkersFishesFilter


class MarkersLogViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = MarkersLog.objects.all()
    serializer_class = MarkersLogSerializer


class PassportsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Passports.objects.all()
    serializer_class = PassportsSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer
