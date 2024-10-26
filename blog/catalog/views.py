from django.shortcuts import render
from .models import Catalog


def catalog(request):
    template = 'catalog/catalog.html'
    catalog = Catalog.objects.all()

    context = {'catalog': catalog}
    return render(request, template, context)
