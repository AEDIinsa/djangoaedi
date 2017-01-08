from django.apps import AppConfig

class AedisiteConfig(AppConfig):
    name = 'aedisite'
    def ready(self):
        from aedisite import receivers
