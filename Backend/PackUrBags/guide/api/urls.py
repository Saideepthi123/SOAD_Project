from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_list_view, name="guide_list_view"),
     path('info', views.guide_for_a_place, name= "guide_for_a_place"),
    path('<slug:slug>', views.guide_detail_view, name="guide_detail_view"),
   
]