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


class Comments(models.Model):
    name = models.CharField(max_length=125, verbose_name='username')
    comment = models.TextField(verbose_name='comment')
    date = models.DateTimeField(auto_now_add=True, verbose_name='comment creation date')
    article_id = models.ForeignKey(
                                    to=Article,
                                    on_delete=models.CASCADE,
                                    verbose_name='article'
                                    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.name} on {self.article_id.title}'
    