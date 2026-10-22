from django.db import models
# Rend les noms de champs et modèles traduisibles (Point 7)
from django.utils.translation import gettext_lazy as _

class Tournament(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom du tournoi")

    date = models.DateField(verbose_name="Date du tournoi")

    location = models.CharField(verbose_name="Lieu du tournoi")

    image = models.ImageField(default="", blank=True, upload_to='static/IMAGES/', verbose_name="Image du tournoi")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('date', 'id')
        verbose_name = "tournoi"
        verbose_name_plural = "tournois"

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom de l'équipe")

    tournament = models.ForeignKey(Tournament, verbose_name="Tournoi", related_name='teams', on_delete=models.CASCADE)

    paid = models.BooleanField(default=False, verbose_name="Payé")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', 'id')
        verbose_name = "équipe"
        verbose_name_plural = "équipes"

class Player(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Prénom du joueur")

    lastname = models.CharField(max_length=50, verbose_name="Nom du joueur")

    email = models.EmailField(unique=True, verbose_name="Courriel")

    team = models.ForeignKey(Team, verbose_name="Équipe", related_name="players", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ('lastname', 'firstname')
        verbose_name = "joueur"
        verbose_name_plural = "joueurs"