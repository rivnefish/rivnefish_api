from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.authtoken import views


urlpatterns = [
    url(r'^', include('site_manager.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token/', views.obtain_auth_token)
]

urlpatterns += staticfiles_urlpatterns()