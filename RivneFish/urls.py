from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User

from site_manager import views

from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets


urlpatterns = [
    url(r'^api/', include('site_manager.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
