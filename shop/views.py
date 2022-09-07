# from itertools import product
import logging
from .models import Product
from django.shortcuts import render
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404


def shop(request):
    products = Product.objects.order_by('-list_date')
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'products': paged_listings
    }

    return render(request, 'shop/products.html', context)

# add product(request, product_id) by Matt


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product-detail.html', context)


# def discount(request):
#     if product.discount_percent > 0:
#         discounted_price = product.price - product.price * \
#             product.discount_percent / 100
#     context = {
#         'discounted_price': discounted_price
#     }
#     return render(request, 'shop/products.html', context)


class ProductView(View):
    def get(self, request):
        gretting = {"title": "Product"}
        return render(request, 'shop/products.html', gretting)


# class ProductListView(View):
#     def get(self, request):
#         gretting = {"title": "Product List"}
#         return render(request, 'shop/product-list.html', gretting)


class ProductDetailsView(View):
    def get(self, request):
        gretting = {"title": "Product Details"}
        return render(request, 'shop/product-detail.html', gretting)


class CartView(View):
    def get(self, request):
        gretting = {"title": "Cart "}
        return render(request, 'shop/cart.html', gretting)


class CheckoutView(View):
    def get(self, request):
        gretting = {"title": "Checkout"}
        return render(request, 'shop/checkout.html', gretting)
