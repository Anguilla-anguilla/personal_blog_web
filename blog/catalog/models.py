from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=125, verbose_name='title')
    summary = models.TextField(verbose_name='summary')
    date = models.DateField(verbose_name='date of publishing')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(blank=True,
                              upload_to='img',
                              verbose_name='image')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
    
    def __str__(self):
        title = self.title
        return title