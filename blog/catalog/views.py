from django.shortcuts import render
from .models import Article


def catalog(request):
    template = 'catalog/catalog.html'
    catalog = Article.objects.all()

    context = {'catalog': catalog}
    return render(request, template, context)


def article(request):
    template = 'catalog/catalog.html'
    article = Article.objects.all()

    context = {'article': article}
    return render(request, template, context)