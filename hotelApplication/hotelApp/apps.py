from django.apps import AppConfig


class HotelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotelApp'
    def ready(self):
        from . import signals
