from django.db import models


class Temperature(models.Model):
    value = models.FloatField()
    time = models.TimeField()

    def __str__(self):
        return self.time

class Load(models.Model):
    value = models.FloatField()
    time = models.TimeField()

    def __str__(self):
        return self.time

class Pressure(models.Model):
    value = models.FloatField()
    time = models.TimeField()

    def __str__(self):
        return self.time

class User(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
