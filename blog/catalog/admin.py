from django.contrib import admin
from .models import Article, Comments, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'summary',
                    'text',
                    )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'date',
                    'article_id')

    
