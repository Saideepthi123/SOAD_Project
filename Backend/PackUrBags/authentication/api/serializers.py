from rest_framework import serializers
from authentication.models import UserData
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.api.utils import Util

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model = UserData
        fields = ['email', 'username', 'password', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only consists of alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return UserData.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, min_length=6, write_only=True)
    password = serializers.CharField(max_length=64, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=6, read_only=True)
    tokens = serializers.CharField(max_length=64, min_length=6, read_only=True)

    class Meta:
        model = UserData
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user.is_active:
            raise AuthenticationFailed('Account disabled')

        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
        }
        
class ResetPaswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=5)

    class Meta:
        fields=['email']

    def validate(self,attrs):
            email = attrs['data'].ge('email','')
            if UserData.objects.filter(email=email).exists():
                user = UserData.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(user.id)
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request=attrs['data'].request).domain
                relative_link = reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token})
                absurl = 'http://' + current_site + relative_link 
                email_body = 'Hi ' + user.username + ', click the link below to reset your password\n' + absurl
                message = {'email_body': email_body, 'email_subject': 'Reset Password', 'to_email': (user.email,)}
                Util.send_email(message)
        
            return super().validate(attrs)