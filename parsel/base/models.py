from django.db import models


# Create your models here.
class ParselVerileri(models.Model):
    ParselID=models.PositiveIntegerField(null=True)
    ada = models.PositiveIntegerField(null=True)
    parsel =  models.IntegerField(null=True)
    kordinatx = models.FloatField(null=True)
    kordinaty = models.FloatField(null=True)
    alan =  models.IntegerField(null=True)


class SehirMerkezi(models.Model):
    parselid =  models.PositiveIntegerField(null=True)
    kordinatx = models.FloatField(null=True)
    kordinaty = models.FloatField(null=True)
