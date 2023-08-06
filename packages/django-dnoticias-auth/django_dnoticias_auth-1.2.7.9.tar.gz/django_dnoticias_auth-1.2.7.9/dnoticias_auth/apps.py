from django.apps import AppConfig


class DnoticiasAuthConfig(AppConfig):
    name = 'dnoticias_auth'

    def ready(self):
        import dnoticias_auth.signals
