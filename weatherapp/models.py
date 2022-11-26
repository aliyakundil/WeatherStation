from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __srt__(self):
        return self.name

class Metcast(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Прогноз погоды'
        verbose_name = 'Прогноз погоды'

    def __srt__(self):
        return self.name