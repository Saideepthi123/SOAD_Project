from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name="UserList"),
    path('<slug:slug>', views.UserDetail.as_view(), name="UserDetail"),
    path('booking/user/<slug:slug>', views.BookingDetailUser.as_view(), name = "BookingDetailUser"), 
    path('booking/guide/<slug:slug>', views.BookingDetailGuide.as_view(), name = "BookingDetailGuide"),
    path('booking/<slug:slug>', views.BookingDetail.as_view(), name="BookingDetail"),
    path('booking/', views.BookingList.as_view(), name="BookingList")
]