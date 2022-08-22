from django.shortcuts import render
from django.views import View
 
# Create your views here.
class WorkView(View):
    def get(self,request):
        gretting={"title":"Work"}
        return render(request,'portfolio/work.html',gretting)

class WorkDetailsView(View):
    def get(self,request):
        gretting={"title":"Work Details"}
        return render(request,'portfolio/work-detail.html',gretting)


