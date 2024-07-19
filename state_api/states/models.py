from django.db import models


class State(models.Model):

    name = models.CharField('Name', max_length=125, unique=True)
    capital = models.CharField('Capital', max_length=125)
    area = models.DecimalField('Area, sq.km', max_digits=15, decimal_places=2)
    population = models.PositiveIntegerField('Population')

    def __str__(self):
        return f'{self.name}, {self.capital}'
