from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>/', views.catalog, name='catalog_filtered'),
    path('article/<int:pk>/', views.article, name='article')
]
