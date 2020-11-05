from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import UserData
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.api.serializers import RegisterSerializer, LoginSerializer, ResetPasswordEmailRequestSerializer, \
    ResetPasswordSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.api.utils import Util
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class HomeView(generics.GenericAPIView):

    def get(self, request):
        return Response({'message': 'Welcome to PackUrBags'}, status=status.HTTP_200_OK)


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
        token = Token.objects.get(user=user)
        uidb64 = urlsafe_base64_encode(smart_bytes(token.user_id))
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify', kwargs={'uidb64': uidb64})
        absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi ' + user.username + ', click the link below to verify your email\n' + absurl
        message = {'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': (user.email,)}
        Util.send_email(message)
        user_data['token'] = token.key
        user_data['user_id'] = user.id
        user_data['is_verified'] = user.is_verified
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):

    def get(self, request, uidb64):
        user_id = smart_str(urlsafe_base64_decode(uidb64))
        user = UserData.objects.get(user_id=user_id)
        if user:
            if not user.is_verified:
                user.is_verified = True
                user.save()
                email_body = 'Your email was successfully verified. Thanks for registering.'
                message = {'email_body': email_body, 'email_subject': 'Welcome to PackUrBags',
                           'to_email': (user.email,)}
                Util.send_email(message)
                return Response({'status': 'Successfully verified'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token authentication failed'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        if request.session.session_key:
            return Response({'error': 'Already another user is logged in'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = request.data
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            account = authenticate(email=user['email'], password=user['password'])
            account.id = account.user_id
            token = Token.objects.get(user=account)
            login(request, account)
            return Response({'success': 'Login successful', 'token': token.key, 'user_id': account.user_id,
                             'username': account.username, 'email': account.email, 'first_name': account.first_name,
                             'last_name': account.last_name, 'phone_number': account.phone_number,
                             'is_verified': account.is_verified}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        if request.session.session_key:
            logout(request)
            return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': "You haven't logged in yet"}, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = UserData.objects.get(email=user['email'])

        if user:
            user.id = user.user_id
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

    def post(self, request, user_id):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = UserData.objects.get(user_id=user_id)
        password = data['password1']
        user.set_password(password)
        user.save()
        return redirect('login')


class PasswordTokenCheckAPI(generics.GenericAPIView):

    def get(self, request, uidb64, token):

        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = UserData.objects.get(user_id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_401_UNAUTHORIZED)
            reset_password_url = reverse('reset-password', kwargs={'user_id': user_id})

            return redirect(reset_password_url)

        except DjangoUnicodeDecodeError:
            return Response({'error': 'Token is not valid, please request a new one'},
                            status=status.HTTP_401_UNAUTHORIZED)


class GoogleAuthentication(generics.GenericAPIView):

    def get(self, request):
        if request.session.session_key:
            return Response({'error': 'You are already logged in. Please logout first.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return redirect('/api/auth/accounts/google/login/?process=login')
