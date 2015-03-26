from django.conf import settings
from markers_fishes_serializer import MarkersFishesSerializer
from rest_framework import serializers
from site_manager.models import Markers


class MarkersSerializer(serializers.ModelSerializer):

    district = serializers.SlugRelatedField(read_only=True, slug_field='name')
    country = serializers.SlugRelatedField(read_only=True, slug_field='name')
    region = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # fishes_set = MarkersFishesSerializer()
    photos = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    def get_photos(self, marker):
        query = '''SELECT
                        CONCAT('%s',g.path,'/',p.filename)
                    FROM
                        wp_ngg_pictures p
                    JOIN
                        wp_ngg_gallery g ON g.gid=p.galleryid
                    JOIN
                        markers m ON g.gid=m.gallery_id
                    WHERE
                        m.marker_id=%d ;''' % (settings.HOST_NAME,
                                               marker.marker_id)
        data = Markers.objects.raw(query)
        return list(sum(list(data.query), ()))

    def get_lake(self, marker):
        query = '''SELECT
                         CONCAT('%s','lakes/',post_name,'/')
                    FROM
                         wp_posts p
                    JOIN
                         markers m ON p.ID=m.post_id
                    where
                        marker_id=%d;''' % (settings.HOST_NAME,
                                            marker.marker_id)
        data = Markers.objects.raw(query)
        return str(list(data.query)[0][0])

    class Meta:
        model = Markers
        fields = ('marker_id', 'name', 'address', 'lat', 'lng', 'area',
                  'content', 'conveniences', 'contact', 'max_depth',
                  'average_depth', 'distance_to_rivne', 'permit', 'price_24h',
                  'dayhour_price', 'boat_usage', 'time_to_fish', 'paid_fish',
                  'note', 'note2', 'photo_url1', 'photo_url2', 'photo_url3',
                  'photo_url4', 'approval', 'create_date', 'modify_date',
                  'author_id', 'post_id', 'gallery_id', 'region', 'district',
                  'country', 'photos', 'url')


class ShortMarkersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Markers
        fields = ('marker_id', 'name', 'address', 'lat', 'lng')
