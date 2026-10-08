from django import forms
from .models import Team, Player

class OnePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['firstname', 'lastname', 'email']

        labels = {
            'firstname': 'Prénom',
            'lastname': 'Nom',
            'email': 'Email'
        }

class TwoPlayersForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'tournament', 'paid']

        labels = {
            'name': "Nom de l'équipe",
            'tournament': 'Tournoi',
            'paid': 'Payé ?'
        }