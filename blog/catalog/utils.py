from django.db.models import Q
from .models import Article

def search_query(query):
    keywords = [word for word in query.split() if len(word) > 2]
    q_obj = Q()
    for word in keywords:
        q_obj |= Q(title__icontains=word)
        q_obj |= Q(text__icontains=word)
    return Article.objects.filter(q_obj)