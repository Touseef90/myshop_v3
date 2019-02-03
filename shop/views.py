from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from shop.recommender import Recommend, ContentBased
from django.contrib.auth import authenticate, login


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if not request.user.is_authenticated:
        c_based_products = {}
    else:
        c_based_products = {}
        current_user = request.user
        r = ContentBased()
        c_based_products = r.suggest_products_for(current_user.id)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'c_based_products': c_based_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommend()
    recommended_products = r.suggest_products_for(id)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})
