from django.urls import path
from . import views

urlpatterns = [
    path('', views.MonumentList.as_view(), name="MonumentList"),
    path('info', views.MonumentPlace.as_view(), name="MonumentPlace"),
    path('<slug:slug>', views.MonumentDetail.as_view(), name="MonumentDetail"),
]
