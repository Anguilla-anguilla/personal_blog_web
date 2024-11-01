from .models import Categories


def category_navbar_processor(request, slug=None):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return context
