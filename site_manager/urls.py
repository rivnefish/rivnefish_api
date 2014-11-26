from django.conf.urls import patterns, url, include
from django.http import HttpResponse
from site_manager import views


def test(request):
    return HttpResponse("it's root page")


urlpatterns = patterns('',
                       url(r'^$', test),
                       url(r'^fish_map_markers/$', views.fish_map_markers,
                           name='fish_map_markers'),
                       url(r'^fish_map_markers/(?P<marker_id>\d+)/$',
                           views.fish_marker, name='fish_marker'),
                       url(r'^add/lake\/?$', views.add_lake, name='add_lake'),
                       url(r'^search-by-filters\/?$',
                           views.search_by_filters, name='search_by_filters'),
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework'))
                       )
