from django.urls import path
from shop import views
urlpatterns = [
    path("products",views.ProductView.as_view(),name="products"),
    path("product-list",views.ProductListView.as_view(),name="product-list"),
    path("product-detail",views.ProductDetailsView.as_view(),name="product-detail"),
    path("product-cart",views.CartView.as_view(),name="product-cart"),
    path("product-checkout",views.CheckoutView.as_view(),name="product-checkout"),


]
