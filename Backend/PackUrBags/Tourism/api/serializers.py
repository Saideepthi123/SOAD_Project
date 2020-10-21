from rest_framework import serializers
from Tourism.models import UserData

class UserDataSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    email = serializers.EmailField(max_length=60)
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=200)
    dob = serializers.DateField()
    date_joined = serializers.DateTimeField()
    last_login = serializers.DateTimeField()
    is_admin = serializers.BooleanField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

    def create(self, validated_data):
        return UserData(**validated_data)

    def update(self, instance, validated_data):
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.save()
        return instance  




