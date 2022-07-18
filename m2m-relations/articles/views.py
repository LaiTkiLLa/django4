from django.shortcuts import render

from articles.models import Article, Scope_Aricle


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all(),' article.scopes.all': Scope_Aricle.objects.all()}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
