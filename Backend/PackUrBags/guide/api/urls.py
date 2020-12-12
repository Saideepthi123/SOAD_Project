from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideList.as_view(), name="GuideList"),
    path('info/', views.GuidePlace.as_view(), name="GuidePlace"),
    path('<slug:slug>', views.GuideDetail.as_view(), name="GuideDetail"),
    path('search/available-guides', views.SearchGuides.as_view(), name="search-guides"),
<<<<<<< HEAD
    path('book-guides/<int:guide_id>/<int:user_id>/<int:no_of_days>', views.BookingGuide.as_view(), name="select-guide"),
    path('checkout/complete', views.checkout, name="checkout"),
=======
    path('get-token/', views.getToken.as_view(), name="get-token"),
    path('expose/', views.ExposeGuidesService.as_view(), name="expose-guides"),
>>>>>>> 7a19abb95a3ad893e9a321f5007323e9e5a21e4d
]
