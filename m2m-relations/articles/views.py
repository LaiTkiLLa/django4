from django.shortcuts import render

from articles.models import Article,Scope_Aricle

def articles_list(request):
    template = 'articles/news.html'

    context = {'object_list': Article.objects.order_by('-published_at').all(),
             }

    return render(request, template, context)

