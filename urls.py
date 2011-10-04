from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from base_views import *
admin.autodiscover()
import settings

urlpatterns = patterns('',
    url(r"^$", home_page,),
    (r'^admin/', include(admin.site.urls)),

    (r'^maps/', include("waterqmap.maps.urls")),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

)
