from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user_list_view, name="user_list_view"),
    path('user/<slug:slug>', views.user_detail_view, name="user_detail_view"),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]