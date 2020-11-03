from rest_framework import serializers
from authentication.models import UserData
from rest_framework.response import Response
from Tourism.models import Booking, Payment, UserHistory


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('user_id', 'email', 'first_name', 'last_name', 'username', 'phone_number')

    def create(self, validated_data):
        try:
            p = UserData.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.username = validated_data.get('username ', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return super().update(instance, validated_data)


class BookingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id', 'user_email', 'guide_email', 'timestamp')

    def create(self, validated_data):
        try:
            p = Booking.objects.create(**validated_data)
            print(p)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.booking_id = validated_data.get('booking_id', instance.booking_id)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.guide_email = validated_data.get('guide_email', instance.guide_email)
        instance.save()
        return super().update(instance, validated_data)


class PaymentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'booking_id', 'user_email', 'guide_email', 'timestamp', 'mode_of_payment',)

    def create(self, validated_data):
        try:
            p = Payment.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.payment_id = validated_data.get('payment_id', instance.payment_id)
        instance.mode_of_payment = validated_data.get('mode_of_payment', instance.mode_of_payment)
        instance.booking_id = validated_data.get('booking_id', instance.booking_id)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.guide_email = validated_data.get('guide_email', instance.guide_email)
        instance.save()
        return super().update(instance, validated_data)


class UserHistoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = (
            'user_email', 'mode_of_payment', 'timestamp', 'mode_of_travel', 'travel_amount', 'restaurant',
            'food_amount',
            'lodge', 'stay_amount',)

    def create(self, validated_data):
        try:
            p = UserHistory.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.travel_amount = validated_data.get('travel_amount', instance.travel_amount)
        instance.food_amount = validated_data.get('food_amount', instance.food_amount)
        instance.stay_amount = validated_data.get('stay_amount', instance.stay_amount)
        instance.mode_of_travel = validated_data.get('mode_of_travel', instance.mode_of_travel)
        instance.mode_of_payment = validated_data.get('mode_of_payment', instance.mode_of_payment)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.restaurant = validated_data.get('restaurant', instance.restaurant)
        instance.lodge = validated_data.get('lodge', instance.lodge)
        instance.save()
        return super().update(instance, validated_data)
