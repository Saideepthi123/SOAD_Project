from django.urls import path
from authentication.api.views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, PasswordReset, RequestPasswordResetEmail

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('reset-password/<user_id>/', PasswordReset.as_view(), name="reset-password"),
]
