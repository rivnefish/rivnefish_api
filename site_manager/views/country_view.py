from rest_framework import viewsets

from site_manager.filters.countries_filter import CountriesFilter
from site_manager.models import Countries
from site_manager.serializers import CountriesSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    """

    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
