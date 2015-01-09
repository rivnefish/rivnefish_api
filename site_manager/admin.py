from django.contrib import admin

from models import Countries
from models import Districts
from models import Fishes
from models import Markers
from models import MarkersFishes
from models import MarkersLog
from models import Passports
from models import Regions


class CountriesManager(admin.ModelAdmin):

    fields = ['name', 'country_id']
    list_display = ('name', 'country_id')


class RegionsManager(admin.ModelAdmin):

    fields = ['name', 'country_id', 'region_id']
    list_display = ('name', 'country_id', 'region_id')


class DistrictsManager(admin.ModelAdmin):

    #fields = []
    list_display = ('name', 'district_id')


class FishesManager(admin.ModelAdmin):

    fields = ('fish_id', 'name', 'ukr_name', 'latin_name', 'eng_name',
                    'folk_name', 'description', 'picture', 'article_url',
                    'icon_url', 'icon_width', 'icon_height', 'predator',
                    'redbook')
    list_display = ['name', 'description', 'fish_id']


class MarkersFishesInline(admin.TabularInline):
    model = MarkersFishes
    extra = 0
    fk_name = "marker"


class MarkersManager(admin.ModelAdmin):

    #fields = []
    list_display = ('name', 'marker_id', 'address', 'country', 'region')
    inlines = [MarkersFishesInline]


class MarkersFishesManager(admin.ModelAdmin):

    #fields = []
    list_display = ('fish', 'marker', 'amount', 'weight_avg',
                    'weight_max', 'notes')


class MarkersLogManager(admin.ModelAdmin):

    fields = ['log_id', 'log_text', 'user_info', 'log_date']
    list_display = ('log_id', 'log_text', 'user_info', 'log_date')


class PassportsManager(admin.ModelAdmin):

    list_display = ('marker', 'url_suffix', 'modify_date', 'icon_url',
                    'passport_id')

admin.site.register(Countries, CountriesManager)
admin.site.register(Regions, RegionsManager)
admin.site.register(Districts, DistrictsManager)
admin.site.register(Fishes, FishesManager)
admin.site.register(Markers, MarkersManager)
admin.site.register(MarkersFishes, MarkersFishesManager)
admin.site.register(MarkersLog, MarkersLogManager)
admin.site.register(Passports, PassportsManager)
