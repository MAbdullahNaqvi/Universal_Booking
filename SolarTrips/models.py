from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class planets(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=1000)
    price = models.IntegerField()
    image = models.URLField()
    passengers = models.ManyToManyField(User, related_name="packages", blank=True)
    wishlist = models.ManyToManyField(User, related_name="wishlist", blank = True)
    
    def __str__(self):
        return(f"{self.name}")


class destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.URLField()
    planet = models.ForeignKey(planets, on_delete = models.CASCADE)

    def __str__(self):
        return (f"{self.name } on {self.planet.name}")