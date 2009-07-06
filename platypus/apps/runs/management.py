from django.db.models import signals

from platypus.apps.runs.sync import nike_sync
from platypus.apps.runs import models as runs_app

signals.post_syncdb.connect(nike_sync, sender=runs_app)