from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()
    pokedex_id = models.PositiveIntegerField()
    team = models.ForeignKey(Team)