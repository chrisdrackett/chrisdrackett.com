import logging

from django.core.cache import cache
from django.conf import settings

log = logging.getLogger('global.context_processors')

def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL.rstrip('/')}