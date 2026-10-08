from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom du tournoi")

    date = models.DateField(verbose_name="Date du tournoi")

    location = models.CharField(max_length=100, verbose_name="Lieu du tournoi")

    image = models.ImageField(default="", upload_to='static/IMAGES/', verbose_name="Image du tournoi")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name = "tournoi"
        verbose_name_plural = "tournois"

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom de l'équipe")

    tournament = models.ForeignKey(Tournament, verbose_name="Tournoi", related_name='teams', on_delete=models.CASCADE)

    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Player(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Prénom du joueur")

    lastname = models.CharField(max_length=50, verbose_name="Nom du joueur")

    email = models.EmailField(unique=True)

    team = models.ForeignKey(Team, verbose_name="Équipe", related_name="players", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ('lastname', 'firstname')
        verbose_name = "joueur"
        verbose_name_plural = "joueurs"