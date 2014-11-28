from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User

from site_manager import views

from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets


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
url(r'^admin/', include(admin.site.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
