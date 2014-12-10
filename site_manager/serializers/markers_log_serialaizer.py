from rest_framework import serializers
from site_manager.models import MarkersLog


class MarkersLogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MarkersLog
        fields = ('log_id', 'log_text', 'user_info', 'log_date')
