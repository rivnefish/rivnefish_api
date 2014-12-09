from rest_framework import serializers
from site_manager.models import Fishes


class FishesSerializer(serializers.ModelSerializer):
    """
    """

    # markers_set = serializers.HyperlinkedRelatedField(many=True, view_name='markersfishes-detail')

    class Meta:
        model = Fishes
        fields = ('fish_id', 'name', 'ukr_name', 'icon_url', 'icon_width',
                  'icon_height', 'latin_name', 'eng_name', 'folk_name',
                  'predator', 'redbook', 'picture', 'description',
                  'article_url',
                  )
