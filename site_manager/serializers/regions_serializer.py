from rest_framework import serializers
from site_manager.models import Regions


class RegionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions
        fields = ('region_id', 'name', 'country_id')
