from modeltranslation.translator import TranslationOptions, register
from .models import Tournament

# Traduction des données des modèles (Point 7)
@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
    fields = ('name', 'location')