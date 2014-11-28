from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^api/', include('site_manager.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
