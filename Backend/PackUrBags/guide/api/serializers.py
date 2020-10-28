from rest_framework import serializers
from guide.models import GuideData 
from rest_framework.response import Response

class GuideDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideData
        fields = ('guide_id', 'email', 'first_name', 'last_name', 'username', 'phone_number')
    def create(self, validated_data):
        try:
            p = GuideData.objects.create(**validated_data)
            return p
        except:
            return {'message': 'Error during creation'}

    def update(self, instance, validated_data):
        instance.guide_id = validated_data.get('guide_id', instance.guide_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        # instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.username = validated_data.get('username ', instance.username)
        print(instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        print(validated_data.get('username', instance.username))
        return super().update(instance, validated_data)
