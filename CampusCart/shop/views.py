from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q
from .models import Product
from .filters import ProductFilter
import operator
from django.views.generic import ListView

# q is used to search multiple columns of the database


# def search(request):
#     product_list = Product.objects.all()
#     product_filter = ProductFilter(request.GET, queryset=product_list)
#     return render(request, 'shop/product/search_results.html' , {'filter': product_filter})


def search(request):
    qs = Product.objects.all()
    search_contains_query = request.GET.get('search_contains')
    if search_contains_query != '' and search_contains_query is not None:
        qs = qs.filter(name__icontains=search_contains_query)

    return render(request, 'shop/product/search_results.html', {'queryset' : qs})



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # qs = Product.objects.all()
    # search_contains_query = request.GET.get('search_contains')
    # if search_contains_query != '' and search_contains_query is not None:
    #     qs = qs.filter(name__icontains=search_contains_query)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})




# we define a function for getting a query set based on a particular search

# def get_blog_queryset(query=None):
#     queryset=[]
#     queries =query.split(" ")
#     for q in queries:
#         products = Product.objects.filter(
#             Q(name__icontains=q)|
#             Q(price__icontains=q)
#         ).distinct()
#
#         for product in products:
#             queryset.append(product)
#
#         return list(set(queryset))



