from rest_framework import serializers
from monuments.models import Monument, MonumentInfo, City


class MonumentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monument
        fields = ('monument_id', 'monument_name', 'country', 'basic_info', 'city')

    def create(self, validated_data):
        try:
            p = Monument.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.monument_id = validated_data.get('monument_id', instance.monument_id)
        instance.monument_name = validated_data.get('monument_name ', instance.monument_name)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.basic_info = validated_data.get('basic_info', instance.basic_info)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.save()
        return super().update(instance, validated_data)


class MonumentInfoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonumentInfo
        fields = ('monument_info_id', 'monument_name', 'category', 'info')

    def create(self, validated_data):
        try:
            p = MonumentInfo.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.monument_info_id = validated_data.get('monument_info_id', instance.monument_info_id)
        instance.monument_name = validated_data.get('monument_name ', instance.monument_name)
        instance.info = validated_data.get('info', instance.info)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return super().update(instance, validated_data)


class CityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_name', 'state', 'country', 'pin_code')

    def create(self, validated_data):
        try:
            p = City.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.city_id = validated_data.get('city_id', instance.city_id)
        instance.city_name = validated_data.get('city_name ', instance.city_name)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.save()
        return super().update(instance, validated_data)
