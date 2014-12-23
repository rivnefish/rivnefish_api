from rest_framework import serializers
from django.forms.models import model_to_dict
from site_manager.models import MarkersFishes


class MarkersFishesSerializer(serializers.ModelSerializer):

    def get_fish(self, mf, **kwargs):
        return model_to_dict(mf.fish)

    def get_marker(self, mf, **kwargs):
        return model_to_dict(mf.marker)

    marker_fish = serializers.SerializerMethodField('get_fish')
    #marker = serializers.SerializerMethodField('get_marker')

    class Meta:
        model = MarkersFishes
        fields = ('markers_fishes_id', 'marker', 'marker_fish', 'weight_avg',
                  'weight_max', 'amount', 'notes')
