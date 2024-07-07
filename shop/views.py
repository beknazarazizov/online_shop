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
# def index(request, category_slug=None):
#     search = request.GET.get('search')
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     filter_expensive = request.GET.get('expensive')
#     filter_cheap = request.GET.get('cheap')
#     if category_slug:
#         products = products.filter(category__slug=category_slug)
#     elif search:
#         products = products.filter(Q(name__icontains=search))[:4]
#
#     elif filter_expensive:
#         products = products.order_by('-price')[:3]
#     elif filter_cheap:
#         products = products.order_by('price')[:3]
#     else :
#         products = Product.objects.all()
#
#
#     context = {
#         'products': products,
#         'categories': categories,
#         'filter_expensive': filter_expensive,
#         'filter_cheap': filter_cheap
#
#     }
#     return render(request, 'app/home.html', context)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request,category_slug=None):
    search = request.GET.get('search')
    filter_expensive = request.GET.get('expensive')
    filter_cheap = request.GET.get('cheap')
    categories = Category.objects.all()
    posts = Product.objects.all()  # fetching all post objects from database
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    if search:
        posts = posts.filter(Q(name__icontains=search))
    if filter_expensive:
        posts = posts.order_by('-price')
    if filter_cheap:
        posts = posts.order_by('-price')
    p = Paginator(posts, 3)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj,
               'categories': categories,}
    # sending the page object to index.html
    return render(request, 'app/home.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    product_r = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    comments = Comment.objects.filter(product__slug=slug).order_by('-created_at')[0:3]
    count = comments.count()
    context = {'product': product,
                'comments': comments,
                'count': count,
                'product_r': product_r, }

    return render(request, 'app/detail.html', context)



def add_comment(request, slug):
    product = Product.objects.get(slug=slug)
    new_comment = None
    form = CommentModelForm()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return redirect('product_detail', slug)
    context = {'product': product, 'comment_form': form, 'new_comment': new_comment}
    return render(request, 'app/detail.html', context)


def add_order(request, slug):
    new_order = None
    product = Product.objects.get(slug=slug)
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.product = product
            new_order.save()
            return redirect('product_detail', slug)
    context = {'form': form, new_order: new_order}
    return render(request, 'app/detail.html', context)





def logout(request):
    user=User.objects.get()
    user.logout(request)
    return redirect(request , 'app/home.html')