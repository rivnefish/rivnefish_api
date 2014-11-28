from rest_framework import serializers

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
    class Meta:
        model = Districts
        fields = ('district_id', 'name')


class FishesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fishes
        fields = ('fish_id', 'name', 'ukr_name', 'icon_url', 'icon_width',
                  'icon_height', 'latin_name', 'eng_name', 'folk_name',
                  'predator', 'redbook', 'picture', 'description',
                  'article_url')


class MarkersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Markers
        # With out region 'region'
        fields = ('marker_id', 'name', 'address', 'lat', 'lng', 'area',
                  'content', 'conveniences', 'contact', 'max_depth',
                  'average_depth', 'distance_to_rivne', 'permit', 'price_24h',
                  'dayhour_price', 'boat_usage', 'time_to_fish', 'paid_fish',
                  'note', 'note2', 'photo_url1', 'photo_url2', 'photo_url3',
                  'photo_url4', 'approval', 'create_date', 'modify_date',
                  'author_id', 'post_id', 'gallery_id', 'district',
                  'country', )


class MarkersFishesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkersFishes
        fields = ('id', 'marker', 'fish', 'weight_avg', 'weight_max',
                  'amount', 'notes')


class MarkersLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkersLog
        fields = ('log_id', 'log_text', 'user_info', 'log_date')


class PassportsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passports
        fields = ('passport_id', 'marker', 'url_suffix', 'modify_date',
                  'icon_url')


class RegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regions
        fields = ('region_id', 'name', 'country_id')

