from rest_framework import serializers
from authentication.models import UserData
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


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

    class Meta:
        model = UserData
        fields = ['email', 'password', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user.is_active:
            raise AuthenticationFailed('Account disabled')

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return attrs


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')

        user = authenticate(email=email)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return attrs

    def create(self, validated_data):
        return UserData.objects.create_user(**validated_data)
