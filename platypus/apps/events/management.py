from platypus import signals
from platypus.apps.events.models import add_event

signals.sync_complete.connect(add_event)