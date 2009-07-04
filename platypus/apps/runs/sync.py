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

def sync_runs(*args, **kwargs):
    tree = ET.parse(urllib.urlopen("http://nikerunning.nike.com/nikeplus/v2/services/app/run_list.jsp?userID=%s" % settings.NIKE_PLUS_ID))
    runlist = tree.find('runList')

    for run in runList:
        raw_date = iso8601.parse_date(x.find('startTime').text)
        utc = (raw_date - raw_date.utcoffset()).replace(tzinfo=None)
        
        run, created = Run.objects.get_or_create(id=int(run.get('id')), defaults= {
            'start_date': utc,
            'distance': Decimal(run.find('distance').text),
            'duration': int(run.find('duration').text),
            'calories': Decimal(run.find('calories').text),
            'tags': "running nike_plus",
        })
        
        run.how_felt = run.find('howFelt').text
        run.weather = run.find('weather').text
        run.terrain = run.find('terrain').text