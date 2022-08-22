from django.shortcuts import render
from django.views import View
# Create your views here.


class ProductView(View):
    def get(self,request):
        gretting={"title":"Product"}
        return render(request,'shop/products.html',gretting)

class ProductListView(View):
    def get(self,request):
        gretting={"title":"Product List"}
        return render(request,'shop/product-list.html',gretting)

class ProductDetailsView(View):
    def get(self,request):
        gretting={"title":"Product Details"}
        return render(request,'shop/product-detail.html',gretting)

class CartView(View):
    def get(self,request):
        gretting={"title":"Cart "}
        return render(request,'shop/cart.html',gretting)

class CheckoutView(View):
    def get(self,request):
        gretting={"title":"Checkout"}
        return render(request,'shop/checkout.html',gretting)