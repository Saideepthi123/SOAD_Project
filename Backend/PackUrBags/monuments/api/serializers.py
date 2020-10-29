from rest_framework import serializers
from monuments.models import Monument 
from rest_framework.response import Response


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
        instance.monument_name = validated_data.get('monument_name ', instance.monument_name )
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.basic_info = validated_data.get('basic_info', instance.basic_info)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.save()
        return super().update(instance, validated_data)
