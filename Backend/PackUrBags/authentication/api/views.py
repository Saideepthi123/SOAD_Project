import jwt
from django.conf import settings
from django.shortcuts import redirect
from authentication.models import UserData
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.api.serializers import RegisterSerializer, LoginSerializer, LogoutSerializer, ResetPasswordEmailRequestSerializer, \
    ResetPasswordSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.api.utils import Util
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.


class HomeView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Welcome to PackUrBags'}, status=status.HTTP_200_OK)


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = UserData.objects.get(email=user_data['email'])
        refresh = RefreshToken.for_user(user)
        access = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://' + current_site + relative_link + "?token=" + str(access)
        email_body = 'Hi ' + user.username + ', click the link below to verify your email\n' + absurl
        message = {'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': (user.email,)}
        Util.send_email(message)
        user_data['refresh'] = str(refresh)
        user_data['access'] = str(access)
        user_data['id'] = user.id
        user_data['is_verified'] = user.is_verified
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')
        secret_key = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, secret_key)
            user = UserData.objects.get(id=payload['user_id'])
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
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        user = UserData.objects.get(email=email)
        refresh = RefreshToken.for_user(user)
        access = RefreshToken.for_user(user).access_token
        return Response({'refresh': str(refresh), 'access': str(access), 'user_id': user.id,
                         'username': user.username, 'email': user.email, 'first_name': user.first_name,
                         'last_name': user.last_name, 'phone_number': user.phone_number,
                         'is_verified': user.is_verified}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = UserData.objects.get(email=user['email'])

        if user:
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relative_link
            email_body = 'Hi ' + user.username + ', click the link below to reset your password\n' + absurl
            message = {'email_body': email_body, 'email_subject': 'Reset Password', 'to_email': (user.email,)}
            Util.send_email(message)
            return Response({'success': 'We have sent you a link to reset password'}, status=status.HTTP_200_OK)


class PasswordReset(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, user_id):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = UserData.objects.get(id=user_id)
        password = data['password1']
        user.set_password(password)
        user.save()
        return redirect('login')


class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):

        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = UserData.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_401_UNAUTHORIZED)
            reset_password_url = reverse('reset-password', kwargs={'user_id': user_id})

            return redirect(reset_password_url)

        except DjangoUnicodeDecodeError:
            return Response({'error': 'Token is not valid, please request a new one'},
                            status=status.HTTP_401_UNAUTHORIZED)


class GoogleAuthentication(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return redirect('/api/auth/accounts/google/login/?process=login')
