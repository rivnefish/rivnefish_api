from rest_framework import serializers
from site_manager.models import Passports


class PassportsSerializer(serializers.HyperlinkedModelSerializer):
    """
    """

    marker = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Passports
        fields = ('passport_id', 'marker', 'url_suffix', 'modify_date',
                  'icon_url')
