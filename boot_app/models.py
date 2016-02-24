from django.db import models

# Create your models here.


class Puppy(models.Model):
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    size = models.CharField(max_length=15)

    def __str__(self):
        return self.breed


class Owner(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name