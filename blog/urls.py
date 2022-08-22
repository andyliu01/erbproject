from django.urls import path
from blog import views

urlpatterns = [
    path("blog-grid",views.BlogGridView.as_view(),name="blog-grid"),
    path("blog-listing",views.BlogListingView.as_view(),name="blog-listing"),
    path("blog-single-post",views.BlogSinglePostView.as_view(),name="blog-single-post"),

]