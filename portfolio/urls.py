from django.urls import path
from portfolio import views
urlpatterns = [
    path("work",views.WorkView.as_view(),name="work"),
    path("work-detail",views.WorkDetailsView.as_view(),name="work-detail"),
]
