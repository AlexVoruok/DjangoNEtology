from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort', 'id')
    catalog = Phone.objects.order_by(sort)

    return render(request, template, context={'phones_list': catalog})


def show_product(request, slug):
    template = 'product.html'

    models = Phone.objects.filter(slug=slug)

    context = {'models': models,
               }
    return render(request, template, context)
