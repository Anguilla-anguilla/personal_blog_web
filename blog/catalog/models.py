from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=125, verbose_name='title')
    summary = models.TextField(verbose_name='summary')
    date = models.DateField(verbose_name='date of publishing')
