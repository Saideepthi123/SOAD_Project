from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserList.as_view(), name="UserList"),
    path('user/<slug:slug>', views.UserDetail.as_view(), name="UserDetail"),
    path('user/modify/<slug:slug>', views.UserDetail.as_view(), name="UserDetail"),
    path('user/unregister/<slug:slug>', views.UserDetail.as_view(), name="UserDetail"),

    path('booking/user/<slug:slug>', views.BookingDetailUser.as_view(), name="BookingDetailUser"),
    path('booking/guide/<slug:slug>', views.BookingDetailGuide.as_view(), name="BookingDetailGuide"),
    path('booking/<slug:slug>', views.BookingDetail.as_view(), name="BookingDetail"),
    path('booking/cancel/<slug:slug>', views.BookingDetail.as_view(), name="BookingDetail"),
    path('booking', views.BookingList.as_view(), name="BookingList"),

    path('payment/user/<slug:slug>', views.PaymentDetailUser.as_view(), name="PaymentDetailUser"),
    path('payment/guide/<slug:slug>', views.PaymentDetailGuide.as_view(), name="PaymentDetailGuide"),
    path('payment/<slug:slug>', views.PaymentDetail.as_view(), name="PaymentDetail"),
    path('payment/cancel/<slug:slug>', views.PaymentDetail.as_view(), name="PaymentDetail"),
    path('payment', views.PaymentList.as_view(), name="PaymentList"),

    path('userhistory/user/<slug:slug>', views.UserHistoryDetailUser.as_view(), name="UserHistoryDetailUser"),
    path('userhistory', views.UserHistoryList.as_view(), name="UserHistoryList"),
    path('userhistory/<slug:slug>', views.UserHistoryDetail.as_view(), name="UserHistoryDetail"),

    path('skyscanner/list-places', views.sky_scanner_list_places, name="list-places"),
    path('skyscanner/search-flights', views.SkyScannerSearchFlights.as_view(), name="search-flights"),
    path('skyscanner/flight-routes', views.SkyScannerFlightRoutes.as_view(), name="browse-routes"),

    path('zomato/search-city',views.ZomatoRestaurantsCity.as_view(),name="search-restaurants-city"),
    path('zomato/search-locality',views.ZomatoRestaurantsLocality.as_view(),name="search-locality"),
    
    path('hotels/list-places', views.hotel_list_places, name="hotel-list-places"),
    path('hotels/search-hotels', views.SearchHotels.as_view(), name="search-hotels"),

    path('payment/test_payment/', views.TestPayment.as_view(), name="test-payment"),
    path('payment/confirm_intent/', views.ConfirmIntent.as_view(), name="confirm-intent"),
    path('payment/savestripeinfo/', views.SavestripeInfo.as_view(), name="save-stripe-info"),
]

