from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=200)


class Pokemon(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    image_front = models.CharField(max_length=512)
    image_back = models.CharField(max_length=512)
    types = models.ManyToManyField(PokemonType)

    def __str__(self):
        return f"{self.id}) {self.number} {self.name} {self.height} {self.weight}"
