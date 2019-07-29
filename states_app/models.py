from django.db import models

# Create your models here.


class Municipality(models.Model):

    code = models.PositiveIntegerField(verbose_name='Código', blank=False, unique=True)
    name = models.CharField('Nombre', max_length = 40)
    status = models.BooleanField('Estado', default=True)


class Region(models.Model):
    code = models.PositiveIntegerField(verbose_name='Código', blank=False, unique=True)
    name = models.CharField('Nombre', max_length = 40)
    municipality_id = models.ManyToManyField(Municipality, verbose_name = 'Municipio')


    status = models.BooleanField('Estado', default=True)



