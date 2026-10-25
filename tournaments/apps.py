from django.apps import AppConfig


class TournamentsConfig(AppConfig):
    name = 'tournaments'

    # Chargement automatique des signaux au démarrage de Django (Point 3)
    def ready(self):
        import tournaments.signals
