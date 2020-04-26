from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product_id=pk)
    this_user_reviewed = request.session.get(f'{pk}', False)

    print(this_user_reviewed)
    if request.method == 'POST' and not this_user_reviewed:

        review = Review(product_id=pk)
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            request.session[f'{pk}'] = True
    else:
        form = ReviewForm

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': this_user_reviewed
        }

    return render(request, template, context)
