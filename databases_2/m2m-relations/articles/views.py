from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, Tags



def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.prefetch_related('tagrelation_set', 'tagrelation_set__tags').order_by(ordering)

    context = {'object_list': articles,
              }

    return render(request, template, context)

