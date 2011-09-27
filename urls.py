from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
#    (r'^$', 'portal.maps.views.map_view', name='map'),
    (r'^admin/', include(admin.site.urls)),
    (r'^maps/(?P<map_id>\d+)/$', 'maps.views.map_view'),
    (r'^maps/(?P<map_id>\d+)/days/$', 'maps.views.json_dates'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

)
