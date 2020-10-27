from django.urls import path, include
from authentication.views import RegisterView, VerifyEmail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('api/', include('authentication.api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
