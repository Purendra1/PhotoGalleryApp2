from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'viz'

    def ready(self):
    	import viz.signals
