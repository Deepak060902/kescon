from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from django.contrib.auth.decorators import login_required
from .forms import SearchForm


def index(request):
    categories = Category.objects.all()[:5]  # Get the first 5 categories
    featured_products = {}
    for category in categories:
        products = Product.objects.filter(category=category)[:10]  # Get the first 10 products of each category
        featured_products[category] = products

    context = {
        'featured_products': featured_products
    }
    return render(request, 'index.html', context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = product.reviews.all()
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm()
    return render(request, 'product/add_review.html', {'form': form, 'product': product})


def search_products(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_result.html', {'form': form, 'query': query, 'results': results})

