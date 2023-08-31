from django.db import models


class ConcentrateData(models.Model):
    """
    Качественные показатели железорудного концентрата:
    содержание железа, содержание кремния, содержание алюминия,
    содержание кальция, содержание серы. Данные вносятся ежемесячно"""

    fe = models.FloatField('Содержание железа')
    si = models.FloatField('Содержание кремния')
    al = models.FloatField('Содержание алюминия')
    ca = models.FloatField('Содержание кальция')
    s = models.FloatField('Содержание серы')
    date = models.DateField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return f'Данные от {self.date}'

    class Meta:
        verbose_name = 'Качественные показатели железорудного концентрата'
        verbose_name_plural = 'Качественные показатели железорудного концентрата'
        ordering = ['-date']
