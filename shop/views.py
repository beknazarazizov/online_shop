from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.forms import CommentModelForm,OrderModelForm
from shop.models import Product, Category, Comment


# Create your views here.

# @login_required
def index(request, category_slug=None):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(Q(name__icontains=search))[:4]
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


def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    product_r = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    comment_list = Comment.objects.filter(product__slug=slug).order_by('-created_at')[:3]
    commentForm = CommentModelForm()
    orderForm = OrderModelForm()
    new_comment = None
    new_order = None
    if request.method == 'POST':
        commentForm = CommentModelForm(data=request.POST)
        orderForm = OrderModelForm(data=request.POST)
        if commentForm.is_valid():
            new_comment = commentForm.save(commit=False)
            new_comment.product = product
            new_comment.save()
        elif orderForm.is_valid():
            new_order = orderForm.save(commit=False)
            new_order.product = product
            new_order.save()

    context = {
        'product': product,
        'product_r': product_r,
        'comment_form': commentForm,
        'comment_list': comment_list,
        'orderform': orderForm,
        'new_comment': new_comment,
        'new_order': new_order,


    }
    return render(request, 'app/detail.html', context)



def logout(request):
    user=User.objects.get()
    user.logout(request)
    return redirect(request , 'app/home.html')