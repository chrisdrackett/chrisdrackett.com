from django.dispatch import Signal

sync_complete = Signal(providing_args=["source", "number"])