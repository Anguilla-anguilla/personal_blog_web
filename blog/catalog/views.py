from django.shortcuts import render, get_object_or_404
from .models import Article


def catalog(request):
    template = 'catalog/catalog.html'
    catalog = Article.objects.all().order_by('date')

    context = {'catalog': catalog}
    return render(request, template, context)


def article(request, pk):
    template = 'catalog/article.html'
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, template, context)