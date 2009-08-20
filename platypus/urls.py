from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('platypus.views',
    # Log-in / out
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^temp_sync/$', 'temp_sync', name='temp_sync'),
    
    # Homepage
    url(r'^$', 'home', name='home'),
)


# Assumes that MEDIA_URL = '/static/' or some similar prefix in local_settings

# This will allow the local media resources to be served from the Django dev
# server without running a second web server
if settings.DEBUG and settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^static/(.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )