from rest_framework import serializers
from authentication.models import UserData
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=6, write_only=True, style={'input_type': 'password'})

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
    password = serializers.CharField(max_length=64, min_length=6, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = UserData
        fields = ['email', 'password', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)
        if user:
            if not user.is_active:
                raise AuthenticationFailed('Account disabled')
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return attrs


class ResetPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = UserData
        fields = ['email', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        user = UserData.objects.get(email=email)
        if not user:
            raise AuthenticationFailed('Email does not exist, please check again')
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(label='Password', max_length=64, min_length=6, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(label='Confirm password', max_length=64, min_length=6, write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ['password1', 'password2', ]

    def validate(self, attrs):
        password1 = attrs.get('password1', '')
        password2 = attrs.get('password2', '')

        if password1 == password2:
            return attrs
        elif password1 != password2:
            raise serializers.ValidationError("Passwords don't match")
