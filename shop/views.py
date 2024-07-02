from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.models import Product, Category


# Create your views here.

# @login_required
def index(request, category_slug=None):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    # products = Product.objects.all()
    hom=Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)


    context = {
        'products': products,
        'categories': categories,
        'home' : hom
    }
    return render(request, 'app/home.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'app/detail.html', {'product': product})



# def comment_add(request):
#     pass
#
#
# def order_add():
#     pass