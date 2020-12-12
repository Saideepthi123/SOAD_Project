from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideList.as_view(), name="GuideList"),
    path('info/', views.GuidePlace.as_view(), name="GuidePlace"),
    path('<slug:slug>', views.GuideDetail.as_view(), name="GuideDetail"),
    path('search/available-guides', views.SearchGuides.as_view(), name="search-guides"),
    path('book-guides/<int:guide_id>/<int:user_id>/<int:no_of_days>', views.BookingGuide.as_view(), name="select-guide"),
    path('checkout/complete', views.checkout, name="checkout"),
]
