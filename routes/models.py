from django.db import models
from trains.models import Train


class Route(models.Model):
    name = models.CharField(verbose_name='Название маршрута', max_length=100, unique=True)
    from_city = models.CharField(verbose_name='Откуда', max_length=50)
    to_city = models.CharField(verbose_name='Куда', max_length=50)
    across_cities = models.ManyToManyField(Train, blank=True, verbose_name='Через города')
    travel_times = models.IntegerField(verbose_name='Время пути')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name', ]
