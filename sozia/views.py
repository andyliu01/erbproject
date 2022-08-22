from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

class DashboardView(View):
    def get(self,request):
        gretting = {"title":"Home"}
        return render(request,"dashboard/index.html",gretting)
class AboutView(View):
    def get(self,request):
        gretting = {"title":"About"}
        return render(request,"dashboard/about.html",gretting)
class ServicesView(View):
    def get(self,request):
        gretting = {"title":"Services"}
        return render(request,"dashboard/services.html",gretting)    
