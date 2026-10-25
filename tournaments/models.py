from django.db import models
# Chargement des outils de traduction et traduction des messages avec _(...)  (Point 7)
from django.utils.translation import gettext as _

class Tournament(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Nom du tournoi"))

    date = models.DateField(verbose_name=_("Date du tournoi"))

    location = models.CharField(max_length=100, verbose_name=_("Lieu du tournoi"))

    # Les images envoyées par l'utilisateur sont stockées dans media/tournaments/ (Point 2)
    image = models.ImageField(default="", blank=True, upload_to='tournaments/', verbose_name=_("Image du tournoi"))

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('date', 'id')
        verbose_name = _("tournoi")
        verbose_name_plural = _("tournois")

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Nom de l'équipe"))

    tournament = models.ForeignKey(Tournament, verbose_name=_("Tournoi"), related_name='teams', on_delete=models.CASCADE)

    paid = models.BooleanField(default=False, verbose_name=_("Payé"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', 'id')
        verbose_name = _("équipe")
        verbose_name_plural = _("équipes")

class Player(models.Model):
    firstname = models.CharField(max_length=50, verbose_name=_("Prénom du joueur"))

    lastname = models.CharField(max_length=50, verbose_name=_("Nom du joueur"))

    email = models.EmailField(unique=True, verbose_name=_("Courriel"))

    team = models.ForeignKey(Team, verbose_name=_("Équipe"), related_name="players", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ('lastname', 'firstname')
        verbose_name = _("joueur")
        verbose_name_plural = _("joueurs")