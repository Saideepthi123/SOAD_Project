from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideList.as_view(), name="GuideList"),
    path('info/', views.GuidePlace.as_view(), name="GuidePlace"),
    path('<slug:slug>', views.GuideDetail.as_view(), name="GuideDetail"),
    path('search/available-guides', views.SearchGuides.as_view(), name="search-guides"),
]
