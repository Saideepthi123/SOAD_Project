from django.urls import path
from . import views

urlpatterns = [
    path('', views.MonumentList.as_view(), name="MonumentList"),
    path('<slug:slug>', views.MonumentDetail.as_view(), name="MonumentDetail"),
    path('navigation/', views.MonumentInfoList.as_view(), name="MonumentInfoList"),
    path('navigation/<slug:slug>', views.MonumentInfoDetail.as_view(), name="MonumentInfoDetail"),
]
