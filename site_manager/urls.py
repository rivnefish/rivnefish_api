from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from site_manager import views


router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'regions', views.RegionsViewSet)
router.register(r'districs', views.DistrictsViewSet)
router.register(r'fishes', views.FishesViewSet)
router.register(r'markers', views.MarkersViewSet)
router.register(r'markers-fishes', views.MarkersFishesViewSet)
router.register(r'markers-log', views.MarkersLogViewSet)
router.register(r'passports', views.PassportsViewSet)

urlpatterns = [

url(r'^', include(router.urls)),

]
