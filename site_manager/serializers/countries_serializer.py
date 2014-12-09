from rest_framework import serializers
from site_manager.models import Countries


class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    class Meta:
        model = Countries
        fields = ('country_id', 'name')
