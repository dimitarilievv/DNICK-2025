from django.apps import AppConfig


class CakeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cakeApp'

    def ready(self):
        from . import signals

