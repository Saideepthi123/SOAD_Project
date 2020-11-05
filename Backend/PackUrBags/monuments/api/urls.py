from django.urls import path
from . import views

urlpatterns = [
    path('monument', views.MonumentList.as_view(), name="MonumentList"),
    path('monument/add', views.MonumentList.as_view(), name="MonumentList"),
    path('monument/<slug:slug>', views.MonumentDetail.as_view(), name="MonumentDetail"),
    path('monument/modify/<slug:slug>', views.MonumentDetail.as_view(), name="MonumentDetail"),
    path('monument/delete/<slug:slug>', views.MonumentDetail.as_view(), name="MonumentDetail"),
    path('monument/navigation/', views.MonumentInfoList.as_view(), name="MonumentInfoList"),
    path('monument/navigation/<slug:slug>', views.MonumentInfoDetail.as_view(), name="MonumentInfoDetail"),

    path('city', views.CityList.as_view(), name="CityList"),
    path('city/add', views.CityList.as_view(), name="CityList"),
    path('city/<slug:slug>', views.CityDetail.as_view(), name="CityDetail"),
    path('city/modify/<slug:slug>', views.CityDetail.as_view(), name="CityDetail"),
    path('city/delete/<slug:slug>', views.CityDetail.as_view(), name="CityDetail"),

]
