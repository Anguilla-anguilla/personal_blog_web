from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article, Comments
from .forms import CommentForm
from .utils import search_query


def catalog(request, pk=None):
    template = 'catalog/catalog.html'

    query = request.GET.get('query', None)

    if pk is None:
        catalog = Article.objects.all().order_by('date')
    else:
        catalog = Article.objects.filter(category_id__id=pk).order_by('date')
    
    if query:
        catalog = search_query(query)

    paginator = Paginator(catalog, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'catalog': page_obj}
    return render(request, template, context)


def article(request, pk):
    template = 'catalog/article.html'
    article = get_object_or_404(Article, pk=pk)
    comments = Comments.objects.filter(article_id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article_id = article
            new_comment.save()
            return redirect(to='catalog:article', pk=pk)
    else:
        form = CommentForm()
    context = {'article': article,
               'comments': comments}
    return render(request, template, context)
