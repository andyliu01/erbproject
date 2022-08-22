

        
from django.shortcuts import render
from django.views import View
# Create your views here.


class BlogGridView(View):
    def get(self,request):
        gretting={"title":"Blog Grid"}
        return render(request,'blog/blog-grid.html',gretting)

class BlogListingView(View):
    def get(self,request):
        gretting={"title":"Blog Listing"}
        return render(request,'blog/blog-listing.html',gretting)

class BlogSinglePostView(View):
    def get(self,request):
        gretting={"title":"Blog Single List"}
        return render(request,'blog/blog-single-post.html',gretting)