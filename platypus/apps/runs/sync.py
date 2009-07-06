try:
    from xml.etree import cElementTree as ET
except ImportError:
    import cElementTree as ET

import iso8601, urllib
from datetime import datetime
from decimal import Decimal

from django.conf import settings

from platypus import signals
from platypus.apps.runs.models import Run

def nike_sync(*args, **kwargs):
    tree = ET.parse(urllib.urlopen("http://nikerunning.nike.com/nikeplus/v2/services/app/run_list.jsp?userID=%s" % settings.NIKE_PLUS_ID))
    runlist = tree.find('runList')
    
    number = 0
    
    for run in runlist:
        raw_date = iso8601.parse_date(run.find('startTime').text)
        utc = (raw_date - raw_date.utcoffset()).replace(tzinfo=None)
        
        r, created = Run.objects.get_or_create(id=int(run.get('id')), defaults= {
            'date_added': utc,
            'distance': Decimal(run.find('distance').text),
            'duration': int(run.find('duration').text),
            'calories': Decimal(run.find('calories').text),
            'tags': "running nike_plus",
        })
        
        if created:
            number += 1
        
        r.how_felt = run.find('howFelt').text
        r.weather = run.find('weather').text
        r.terrain = run.find('terrain').text
        r.save()
    
    if number:
        signals.sync_complete.send(
            sender=Run,
            source="nike_run",
            number=number
        )