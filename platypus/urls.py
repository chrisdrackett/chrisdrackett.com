from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('platypus.app.views',
    # Log-in / out
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    
    (r'^admin/', include(admin.site.urls)),
    
    # Homepage
    url(r'^$', 'home', name='home'),
)


# Assumes that MEDIA_URL = '/static/' or some similar prefix in local_settings

from django.conf import settings

if settings.SERVE_MEDIA:
    if settings.DEBUG:
        if not hasattr(settings, 'ROOT_PATH'):
            import os.path
            settings.ROOT_PATH = os.path.dirname(__file__)

        urlpatterns += patterns('',
                                (r'^static/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/../support/images'}),
                                (r'^static/swf/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/../support/swf'}),
                                (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/../support/'}),

                                )