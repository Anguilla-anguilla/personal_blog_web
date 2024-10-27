from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=125, verbose_name='title')
    summary = models.TextField(verbose_name='summary')
    date = models.DateField(verbose_name='date of publishing')
    text = models.TextField(verbose_name='text')