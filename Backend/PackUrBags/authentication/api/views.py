import jwt
from django.urls import reverse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import UserData
from authentication.api.utils import Util
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.api.serializers import RegisterSerializer, LoginSerializer


# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = UserData.objects.get(email=user_data['email'])
        user.id = user.user_id
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi ' + user.username + ', click the link below to verify your email\n' + absurl
        message = {'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': (user.email,)}
        Util.send_email(message)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):

    def get(self, request):
        token = request.GET.get('token')
        secret_key = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, secret_key)
            user = UserData.objects.get(user_id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                email_body = 'Your email was successfully verified. Thanks for registering.'
                message = {'email_body': email_body, 'email_subject': 'Welcome to PackUrBags',
                           'to_email': (user.email,)}
                Util.send_email(message)
                return Response({'status': 'Successfully verified'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
