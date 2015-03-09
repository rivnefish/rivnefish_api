from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from site_manager.views import country_view
from site_manager.views import districts_view
from site_manager.views import fishes_view
from site_manager.views import markers_fishes_view
from site_manager.views import markers_log_view
from site_manager.views import markers_view
from site_manager.views import passports_view
from site_manager.views import regions_view


router = routers.DefaultRouter()
router.register(r'countries', country_view.CountryViewSet)
router.register(r'regions', regions_view.RegionsViewSet)
router.register(r'districs', districts_view.DistrictsViewSet)
router.register(r'fishes', fishes_view.FishesViewSet)
router.register(r'markers', markers_view.MarkersViewSet)
router.register(r'short/markers', markers_view.ShortMarkersViewSet)
router.register(r'markers-fishes', markers_fishes_view.MarkersFishesViewSet)
router.register(r'markers-log', markers_log_view.MarkersLogViewSet)
router.register(r'passports', passports_view.PassportsViewSet)

urlpatterns = router.urls
#===============================================================================
# urlpatterns = [
#
#  url(r'^', include(router.urls)),
#  #url(r'^fishes/$', FishesList.as_view(), name='fishes-list'),
#  #url(r'^fishes/(?P<pk>[^/.]+)/$', FishesList.as_view(), name='fish-detail'),
#
#  ]
#===============================================================================
