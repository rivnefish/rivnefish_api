from rest_framework import serializers
from site_manager.models import Districts


class DistrictsSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    region = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Districts
        fields = ('district_id', 'name', 'region')
