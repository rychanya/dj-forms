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
    reviews = Review.objects.filter(product=product)
    is_review_exist = product.id in request.session.get('reviewed_products', [])
    
    if request.method == 'POST' and not is_review_exist:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            reviewd_list = request.session.get('reviewed_products', [])
            reviewd_list.append(product.id)
            request.session['reviewed_products'] = reviewd_list
            is_review_exist = True
    form = ReviewForm()

    context = {
        'form': form,
        'product': product,
        'is_review_exist': is_review_exist,
        'reviews': reviews
    }

    return render(request, template, context)
