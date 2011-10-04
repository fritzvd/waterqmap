from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'waterqmap.maps.views.index'),
    url(r'^(?P<map_id>\d+)/$', 'waterqmap.maps.views.map_view'),
    url(r'^(?P<map_id>\d+)/days/$', 'maps.views.json_dates'),
)
