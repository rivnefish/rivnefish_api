from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from site_manager.views import CountryView
from site_manager.views import DistrictsView
from site_manager.views import FishesView
from site_manager.views import MarkersFishesView
from site_manager.views import MarkersLogView
from site_manager.views import MarkersView
from site_manager.views import PasportsView
from site_manager.views import RegionsView


router = routers.DefaultRouter()
router.register(r'countries', CountryView.CountryViewSet)
router.register(r'regions', RegionsView.RegionsViewSet)
router.register(r'districs', DistrictsView.DistrictsViewSet)
router.register(r'fishes', FishesView.FishesViewSet)
router.register(r'markers', MarkersView.MarkersViewSet)
router.register(r'markers-fishes', MarkersFishesView.MarkersFishesViewSet)
router.register(r'markers-log', MarkersLogView.MarkersLogViewSet)
router.register(r'passports', PasportsView.PassportsViewSet)

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
