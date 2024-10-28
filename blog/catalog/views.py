from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comments
from .forms import CommentForm


def catalog(request):
    template = 'catalog/catalog.html'
    catalog = Article.objects.all().order_by('date')

    context = {'catalog': catalog}
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
