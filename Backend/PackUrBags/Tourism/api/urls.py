from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_list_view, name="user_list_view"),
    path('<slug:slug>', views.user_detail_view, name="user_detail_view"),
]