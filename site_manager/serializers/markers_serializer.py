from rest_framework import serializers
from site_manager.models import Markers
from markers_fishes_serializer import MarkersFishesSerializer


class MarkersSerializer(serializers.ModelSerializer):

    district = serializers.SlugRelatedField(read_only=True, slug_field='name')
    country = serializers.SlugRelatedField(read_only=True, slug_field='name')
    region = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # fishes_set = MarkersFishesSerializer()

    class Meta:
        model = Markers
        fields = ('marker_id', 'name', 'address', 'lat', 'lng', 'area',
                  'content', 'conveniences', 'contact', 'max_depth',
                  'average_depth', 'distance_to_rivne', 'permit', 'price_24h',
                  'dayhour_price', 'boat_usage', 'time_to_fish', 'paid_fish',
                  'note', 'note2', 'photo_url1', 'photo_url2', 'photo_url3',
                  'photo_url4', 'approval', 'create_date', 'modify_date',
                  'author_id', 'post_id', 'gallery_id', 'region', 'district',
                  'country')


class ShortMarkersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Markers
        fields = ('marker_id', 'name', 'address', 'lat', 'lng', 'photo_url1',
                  'photo_url2', 'photo_url3', 'photo_url4')
