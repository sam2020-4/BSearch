from django.apps import AppConfig


class BsearchConfig(AppConfig):
    name = 'bsearch'

    def ready(self):
        import bsearch.signals

