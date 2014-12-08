from rest_framework import serializers
from django.forms.models import model_to_dict

from models import Countries
from models import Districts
from models import Fishes
from models import Markers
from models import MarkersFishes
from models import MarkersLog
from models import Passports
from models import Regions


class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ('country_id', 'name')


class DistrictsSerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Districts
        fields = ('district_id', 'name', 'region')


class FishesSerializer(serializers.ModelSerializer):
    # This show all markers with fish instance
    # markers_set = serializers.HyperlinkedRelatedField(many=True, view_name='markersfishes-detail')

    class Meta:
        model = Fishes
        fields = ('fish_id', 'name', 'ukr_name', 'icon_url', 'icon_width',
                  'icon_height', 'latin_name', 'eng_name', 'folk_name',
                  'predator', 'redbook', 'picture', 'description',
                  'article_url',
                  )


class MarkersFishesSerializer(serializers.ModelSerializer):
    def get_fish(self, mf, **kwargs):
        return model_to_dict(mf.fish)

    def get_marker(self, mf, **kwargs):
        return model_to_dict(mf.marker)

    fish = serializers.SerializerMethodField('get_fish')
    #marker = serializers.SerializerMethodField('get_marker')

    class Meta:
        model = MarkersFishes
        fields = ('id', 'marker', 'fish', 'weight_avg', 'weight_max',
                  'amount', 'notes')


class MarkersSerializer(serializers.ModelSerializer):
    """
    """

    district = serializers.SlugRelatedField(read_only=True, slug_field='name')
    country = serializers.SlugRelatedField(read_only=True, slug_field='name')
    region = serializers.SlugRelatedField(read_only=True, slug_field='name')
    fishes_set = MarkersFishesSerializer()

    class Meta:
        model = Markers
        fields = ('marker_id', 'name', 'address', 'lat', 'lng', 'area',
                  'content', 'conveniences', 'contact', 'max_depth',
                  'average_deptmh', 'distance_to_rivne', 'permit', 'price_24h',
                  'dayhour_price', 'boat_usage', 'time_to_fish', 'paid_fish',
                  'note', 'note2', 'photo_url1', 'photo_url2', 'photo_url3',
                  'photo_url4', 'approval', 'create_date', 'modify_date',
                  'author_id', 'post_id', 'gallery_id', 'region', 'district',
                  'country',
                  'fishes_set',
                  )


class MarkersLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkersLog
        fields = ('log_id', 'log_text', 'user_info', 'log_date')


class PassportsSerializer(serializers.HyperlinkedModelSerializer):
    marker = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Passports
        fields = ('passport_id', 'marker', 'url_suffix', 'modify_date',
                  'icon_url')


class RegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regions
        fields = ('region_id', 'name', 'country_id')

