# apps.py
from django.apps import AppConfig
from .mqtt_client import client

class MyappmotorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myappmotor'

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        client.loop_start()